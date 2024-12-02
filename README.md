# **Chatbot-Regras**

Este projeto implementa um nó de ROS2 que atua como um chatbot baseado em regras, capaz de interpretar comandos escritos em linguagem natural. O chatbot foi desenvolvido para interagir com um robô de serviço fictício, simulando a execução de ações baseadas nos comandos recebidos.

---

## **Objetivo**
O objetivo deste projeto é criar um nó ROS que:
- Entenda comandos em linguagem natural, como "Vá para a secretaria".
- Extraia a intenção do usuário a partir de um dicionário de intenções usando expressões regulares.
- Execute ações predefinidas vinculadas às intenções e forneça feedback ao usuário.

---

## **Funcionalidades**
- **Reconhecimento de Intenções**: O chatbot compreende variações de comandos usando expressões regulares.
- **Execução de Ações**: Cada intenção é mapeada para uma ação específica (simulada).
- **Feedback ao Usuário**: O chatbot informa o usuário sobre o status da ação solicitada ou se o comando não foi reconhecido.
- **Interface via Terminal**: O usuário interage com o chatbot diretamente pelo terminal.

---

## **Comandos Reconhecidos**

O chatbot reconhece as seguintes intenções e suas variações:

| Comando Reconhecido          | Intenção              | Ação Simulada                     |
|------------------------------|-----------------------|------------------------------------|
| "Vá para a secretaria"       | `go_to_secretary`     | Robô indo para a secretaria...     |
| "Me leve para a biblioteca"  | `go_to_library`       | Robô indo para a biblioteca...     |
| "Dirija-se ao laboratório"   | `go_to_lab`           | Robô indo para o laboratório...    |

---

## **Instalação**

### **1. Configure o Ambiente ROS**
Certifique-se de que o ROS2 está instalado no sistema. [Instruções de instalação](https://docs.ros.org/en/).

### **2. Clone este Repositório**
No terminal, execute:
```bash
git clone https://github.com/seu-usuario/Chatbot-Regras.git
cd Chatbot-Regras
```

Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

### **3. Compile o Workspace ROS**
Certifique-se de estar no diretório do workspace e compile o pacote:
```bash
cd ~/Chatbot-Regras
colcon build
source install/setup.bash
```

---

## **Execução**

### **1. Iniciar o Nó Chatbot**
Execute o nó no terminal:
```bash
ros2 run chatbot_node chatbot
```

### **2. Interagir com o Chatbot**
Digite os comandos diretamente no terminal. Exemplos:
```plaintext
Você: Vá para a secretaria
Chatbot: Ação reconhecida: Robô indo para a secretaria...

Você: Me leve para a biblioteca
Chatbot: Ação reconhecida: Robô indo para a biblioteca...

Você: Vá para Marte
Chatbot: Comando não reconhecido. Por favor, tente novamente.
```

### **3. Encerrar o Chatbot**
Digite `sair`, `exit` ou `quit` para encerrar o nó:
```plaintext
Você: sair
Chatbot: Encerrando o chatbot. Até logo!
```

---

## **Como Funciona**
1. **Reconhecimento de Intenções**:
   - O chatbot usa expressões regulares para identificar a intenção do comando.
2. **Execução de Ações**:
   - Cada intenção é mapeada para uma subrotina (simulada neste projeto).
3. **Feedback ao Usuário**:
   - Informa o sucesso ou a falha no reconhecimento do comando.
