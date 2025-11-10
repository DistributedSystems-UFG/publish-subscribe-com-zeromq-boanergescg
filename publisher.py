import zmq
from constPS import *

print(f"Iniciando o Broker/Servidor de Chat em {HOST}...")
print(f"Clientes devem ENVIAR para a porta: {PUB_PORT}")
print(f"Clientes devem RECEBER da porta: {SUB_PORT}")

context = zmq.Context()

# Socket XSUB: Clientes (subscribers) se conectam aqui para *enviar* mensagens
frontend = context.socket(zmq.XSUB)
frontend.bind(f"tcp://*:{PUB_PORT}")

# Socket XPUB: Clientes (subscribers) se conectam aqui para *receber* mensagens
backend = context.socket(zmq.XPUB)
backend.bind(f"tcp://*:{SUB_PORT}")

# Inicia o proxy que liga o frontend ao backend
# O ZMQ cuida de todo o roteamento de mensagens
try:
    zmq.proxy(frontend, backend)
except KeyboardInterrupt:
    print("\nServidor (Publisher) encerrado.")
finally:
    frontend.close()
    backend.close()
    context.term()
