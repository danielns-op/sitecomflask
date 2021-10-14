from random import randint, choice

# Constantes.
# caracteres que serão utilizados para gerar a senha.
LETRAS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']

NUMEROS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

SIMBOLOS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class GeraSenha():
    def __init__(self, quant_letras=0, quant_numeros=0, quant_simbolos=0):
        self.quant_letras = quant_letras
        self.quant_numeros = quant_numeros
        self.quant_simbolos = quant_simbolos
    
    def gerando_senha(self):
        """Gera uma senha conforme a quantidade de caracteristicas selecionadas
            quant_letras - define o número de letras que a senha irá conter.
            quant_numeros - define a quantidade de números que a senha irá conter.
            quant_simbolos - define a quantidade de simbolos que a senha irá conter.
            
            Caso algum desses valores não sejam informados será assumido o valor 0
            como padrão.
        Returns:
            [str]: Retorna uma váriavel contendo uma senha com as caracteristicas
                    definidas nas varáveis relacionada a quantidade.
        """
        senha_lista = []
        senha = ''
        
        for _ in range(1, self.quant_letras + 1):
            letra_escolhida = choice(LETRAS)  # escolhe uma letra de forma alatória.
            senha_lista.append(letra_escolhida)  # adiciona o número escolhido a lista.
        
        for _ in range(1, self.quant_numeros + 1):
            numero_escolhido = choice(NUMEROS)  # escolhe um número de forma alatória.
            # pega o tamanho da lista para que possa ser selecionado um número aleatório
            # onde esse número será a posição para a inserção do novo caractere.
            index = randint(0, len(senha_lista) - 1)
            senha_lista.insert(index, numero_escolhido)
        
        for _ in range(1, self.quant_simbolos + 1):
            simbolo_escolhido = choice(SIMBOLOS)  # escolhe um símbolo de forma alatória.
            # pega o tamanho da lista para que possa ser selecionado um número aleatório
            # onde esse número será a posição para a inserção do novo caractere.
            index = randint(0, len(senha_lista) -1)
            senha_lista.insert(index, simbolo_escolhido)
        
        senha = ''.join(senha_lista)
        
        return senha
