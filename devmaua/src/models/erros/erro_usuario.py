

class ErroDadosUsuarioInvalidos(Exception):
    def __init__(self):
        super().__init__("Os dados fornecidos não puderam ser convertidos em um Usuario válido")