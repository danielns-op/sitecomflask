import requests
from googletrans import Translator
from random import choice

# tradutor
tradutor = Translator()


def pega_conselho(assunto=False):
    """ A função acessa a API e retorna um conselho

    Args:
        assunto (bool, optional): Se tiver uma palavra como
        argumento será retornado um conselho que tenha o assunto
        relacionado com o argumento passado. Por defaults o
        argumento é falso para que a função retorne um conselho
        de forma aleatória.

    Returns:
        frase_traduzida: Retorna o conselho traduzido para o
        idioma português.
    """
    if assunto:
        assunto_traduzido = tradutor.translate(assunto, dest='en').text
        response = requests.get(f"https://api.adviceslip.com/advice/search/{assunto_traduzido}")
        
        if response.json()['total_results']:
            frase_escolhida = choice(response.json()['slips'])['advice']
        else:
            frase_escolhida = response.json()['message']['text']
    else:
        response = requests.get('https://api.adviceslip.com/advice')
        frase_escolhida = response.json()['slip']['advice']
        
    frase_traduzida = tradutor.translate(frase_escolhida, dest='pt').text
        
    return frase_traduzida


def jogo_de_cartas():
    """Acessa uma API e pega os dados de duas cartas em um baralho de 52 cartas.
    Returns:
        pega_carta_jogador e pega_carta_bot: Retorna duas variáveis cada uma contendo um dicionário com os dados das cartas, como código, imagem, entre outros.
        Abaixo segue os valores das chaves contidas nesse dicionário:
        code, image, images, value e suit.
    """
    LISTA_NIPE = ['HEARTS', 'CLUBS', 'DIAMONDS', 'SPADES']
    LISTA_NIPE_TRADUZIDO = ['Coração', 'Paus', 'Ouro', 'Espadas']
    VALOR_CARTA = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
    VALOR_CARTA_TRADUZIDO = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    
    pega_baralho = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1').json()
    id_baralho = pega_baralho['deck_id']
    
    # pegando os dados da carta do jogador -------------------- #
    pega_carta_jogador = requests.get(f'https://deckofcardsapi.com/api/deck/{id_baralho}/draw/?count=1').json()['cards'][0]
    ## convertendo o nipe
    nipe_carta_jogador = pega_carta_jogador['suit']
    pega_carta_jogador['suit'] = LISTA_NIPE_TRADUZIDO[LISTA_NIPE.index(nipe_carta_jogador)]
    ### convertendo o valor
    valor_carta_jogador = pega_carta_jogador['value']
    pega_carta_jogador['value'] = VALOR_CARTA_TRADUZIDO[VALOR_CARTA.index(valor_carta_jogador)]
    
    # pegando os dados da carta d0 bot -------------------- #
    pega_carta_bot = requests.get(f'https://deckofcardsapi.com/api/deck/{id_baralho}/draw/?count=1').json()['cards'][0]
    ## convertendo o nipe
    nipe_carta_bot = pega_carta_bot['suit']
    pega_carta_bot['suit'] = LISTA_NIPE_TRADUZIDO[LISTA_NIPE.index(nipe_carta_bot)]
    ### convertendo o valor
    valor_carta_bot = pega_carta_bot['value']
    pega_carta_bot['value'] = VALOR_CARTA_TRADUZIDO[VALOR_CARTA.index(valor_carta_bot)]
    
    return pega_carta_jogador, pega_carta_bot
