import rclpy
from rclpy.node import Node
import re

# Mapeamento de ações baseadas em locais
actions = {
    "secretaria": lambda: "Robô indo para a secretaria...",
    "biblioteca": lambda: "Robô indo para a biblioteca...",
    "laboratório": lambda: "Robô indo para o laboratório...",
}

# Padrão regex para capturar a intenção e o local
command_pattern = re.compile(r"(vá para|me leve para|dirija-se à|dirija-se ao)\s+(.*)", re.IGNORECASE)

class ChatbotNode(Node):
    def __init__(self):
        super().__init__('chatbot_node')
        self.get_logger().info("Chatbot iniciado! Digite 'sair' para encerrar.")
        self.run_chatbot()

    def clean_location(self, location):
        """
        Remove caracteres irrelevantes do local capturado.
        """
        # Filtra apenas palavras alfabéticas
        words = re.findall(r"\b\w+\b", location)
        if words:
            return words[-1].lower()  # Retorna a última palavra relevante
        return None

    def process_command(self, command):
        """
        Processa o comando do usuário usando regex para capturar a intenção e o local.
        """
        match = command_pattern.search(command)  # Procura o padrão no comando
        if match:
            _, location = match.groups()  # Captura a intenção e o local
            cleaned_location = self.clean_location(location)  # Limpa o local
            if cleaned_location and cleaned_location in actions:
                response = actions[cleaned_location]()  # Executa a ação associada ao local
                return f"Ação reconhecida: {response}"
            else:
                return f"Local '{cleaned_location}' não reconhecido."
        return "Comando não reconhecido. Por favor, tente novamente."

    def run_chatbot(self):
        """
        Inicia o chatbot para interação com o usuário.
        """
        while rclpy.ok():
            command = input("Você: ")
            if command.lower() in ["sair", "exit", "quit"]:
                self.get_logger().info("Encerrando o chatbot. Até logo!")
                break
            response = self.process_command(command)
            self.get_logger().info(f"Chatbot: {response}")

def main(args=None):
    rclpy.init(args=args)
    chatbot_node = ChatbotNode()
    rclpy.spin(chatbot_node)
    chatbot_node.destroy_node()
    rclpy.shutdown()
