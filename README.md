[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/mrIsNMKU)
# Pub-Sub-Basics-with-ZeroMQ

This is a very simple pub-sub app implemented with ZeroMQ. Use it as an example for the pub-sub assignment (topic-based chat system).

### First, install ZeroMQ (on each machine):

    sudo apt update

    sudo apt install python3-zmq

### Or, with virtual environments (also on each machine -- only install pip3 and venv if not yet installed):

    sudo apt update
    sudo apt install python3-pip
    sudo apt install python3-venv
    python3 -m venv myvenv
    source myvenv/bin/activate
    pip3 install pyzmq

### Next, configure the IP address and port number of the publisher's machine in the constPS.py file

Note: Make sure that this repo is cloned in all the machines used for this experiment.

### Then, run the publisher and subscriber:

On the machine for which the IP address was configured:

    python3 publisher.py

On another machine:

    python3 subscriber.py

### Now, add other topics for in the publisher and create subscribers for the new topics.

Modificação para poder testar a nova versão

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/mrIsNMKU)
# Pub-Sub-Basics-with-ZeroMQ (Chat em Grupo)

Esta aplicação utiliza o padrão Publish-Subscribe do ZeroMQ para implementar um sistema de chat em grupo baseado em tópicos.

A arquitetura consiste em:
* `publisher.py`: Atua como o **Broker/Servidor** central. Ele recebe mensagens de todos os clientes e as retransmite para os assinantes corretos.
* `subscriber.py`: Atua como o **Cliente de Chat**. Cada usuário executa este script. Ele pode enviar (publicar) e receber (assinar) mensagens simultaneamente.
* `constPS.py`: Arquivo de configuração que define o IP do servidor e as portas de comunicação.

### 1. Instalação do ZeroMQ (on each machine)

    sudo apt update

    sudo apt install python3-zmq
    
(Ou utilize as instruções de ambiente virtual (venv) do README original, se preferir).

### 2. Configuração

Antes de executar, edite o arquivo `constPS.py`:
* Defina a variável `HOST` para o endereço IP da máquina que executará o `publisher.py` (o servidor).
* Use `HOST = "127.0.0.1"` se for testar tudo na mesma máquina.

### 3. Executando o Chat

O processo requer pelo menos dois terminais (um para o servidor e um para o primeiro cliente).

**Passo 1: Iniciar o Servidor (Broker)**

Na máquina servidora (cujo IP está em `constPS.py`), execute:

    python3 publisher.py

O servidor ficará ativo, esperando por conexões.

**Passo 2: Iniciar os Clientes (Assinantes)**

Em outra(s) máquina(s) ou em novo(s) terminal(is), execute `subscriber.py` para cada usuário:

    python3 subscriber.py

O script solicitará:
1.  **Nome de usuário:** O nome que aparecerá no chat.
2.  **Nome do grupo (tópico):** O nome da sala de chat.

**Exemplo de Teste:**

1.  **Servidor (Terminal 1):**
    * `python3 publisher.py`
2.  **Cliente 1 (Terminal 2):**
    * `python3 subscriber.py`
    * Nome: `Alice`
    * Grupo: `geral`
3.  **Cliente 2 (Terminal 3):**
    * `python3 subscriber.py`
    * Nome: `Bob`
    * Grupo: `geral`
4.  **Cliente 3 (Terminal 4):**
    * `python3 subscriber.py`
    * Nome: `Carlos`
    * Grupo: `dev`

*Resultado:* Mensagens enviadas por Alice só serão vistas por Bob (e vice-versa), pois estão no mesmo tópico (`geral`). Carlos está em um tópico diferente (`dev`) e só verá mensagens desse grupo.

    
