import rclpy
from rclpy.node import Node

import re

# Dicionários de intenções e ações
intentions = {
    "go_to_secretary": ["secretaria", "vá para a secretaria", "dirija-se à secretaria"],
    "go_to_library": ["biblioteca", "me leve para a biblioteca", "vá para a biblioteca"],
    "go_to_lab": ["laboratório", "vá para o laboratório", "dirija-se ao laboratório"],
}

actions = {
    "go_to_secretary": lambda: "Robô indo para a secretaria...",
    "go_to_library": lambda: "Robô indo para a biblioteca...",
    "go_to_lab": lambda: "Robô indo para o laboratório...",
}

class ChatbotNode(Node):
    def __init__(self):
        super().__init__('chatbot_node')
        self.get_logger().info("Chatbot iniciado! Digite 'sair' para encerrar.")
        self.run_chatbot()

    def process_command(self, command):

        for intention, phrases in intentions.items():
            for phrase in phrases:
                if re.search(phrase, command, re.IGNORECASE):
                    response = actions[intention]()  # Executa a ação
                    return f"Ação reconhecida: {response}"
        return "Comando não reconhecido. Por favor, tente novamente."

    def run_chatbot(self):

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
