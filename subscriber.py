import zmq
import threading
import sys
from constPS import *

# --- Thread para Receber Mensagens ---
def receive_messages(topic, sub_socket):
    """
    Função que roda em background, escutando por mensagens
    no tópico inscrito e imprimindo-as.
    """
    print(f"--- Você entrou no grupo: {topic} ---")
    try:
        while True:
            # Recebe a mensagem (que vem com o tópico)
            full_message = sub_socket.recv_string()
            
            # Formato esperado: "TOPICO [Usuario]: Mensagem"
            # Separa o tópico do resto da mensagem
            message_parts = full_message.split(' ', 1)
            
            if len(message_parts) > 1:
                # Imprime apenas a parte da mensagem (ex: "[Usuario]: Mensagem")
                # \r limpa a linha, > re-imprime o prompt
                print(f"\r{message_parts[1]}\n> ", end="")
            
    except zmq.ContextTerminated:
        pass # Contexto foi encerrado, thread pode parar
    except Exception as e:
        print(f"\nErro ao receber: {e}")

# --- Configuração Principal ---
if __name__ == "__main__":
    try:
        # Pede ao usuário seu nome e o tópico (grupo)
        username = input("Digite seu nome de usuário: ")
        topic = input("Digite o nome do grupo (tópico) para entrar: ")

        if not username or not topic:
            print("Nome de usuário e tópico não podem estar vazios.")
            sys.exit(1)

        context = zmq.Context()

        # 1. Socket para PUBLICAR (enviar nossas mensagens)
        # Conecta ao frontend do broker (publisher.py)
        pub_socket = context.socket(zmq.PUB)
        pub_socket.connect(f"tcp://{HOST}:{PUB_PORT}")

        # 2. Socket para ASSINAR (receber mensagens)
        # Conecta ao backend do broker (publisher.py)
        sub_socket = context.socket(zmq.SUB)
        sub_socket.connect(f"tcp://{HOST}:{SUB_PORT}")
        # Inscreve-se no tópico desejado
        sub_socket.setsockopt_string(zmq.SUBSCRIBE, topic)

        # Inicia a thread que fica escutando por mensagens
        receiver_thread = threading.Thread(
            target=receive_messages, 
            args=(topic, sub_socket),
            daemon=True  # Permite que o programa feche sem esperar a thread
        )
        receiver_thread.start()

        print("\nConectado! Digite suas mensagens e pressione Enter (Ctrl+C para sair).")
        print("> ", end="")
        
        while True:
            # Lê a mensagem do teclado no loop principal
            message_text = input()
            
            # Formata a mensagem com o tópico e nome de usuário
            full_message = f"{topic} [{username}]: {message_text}"
            
            # Envia (publica) a mensagem para o broker
            pub_socket.send_string(full_message)
            print("> ", end="") # Prompt para nova mensagem

    except KeyboardInterrupt:
        print("\nDesconectando...")
    finally:
        # Fecha os sockets e termina o contexto
        pub_socket.close()
        sub_socket.close()
        context.term()
        print("Saída completa.")
