from apis import apis, gerar_senha
from datetime import datetime
from flask import Flask, render_template, request
from flask.wrappers import Request


app = Flask(__name__)

ANO = datetime.today().year

# Rotas
@app.route('/')
def home():
    return render_template('index.html', ano_site=ANO)


@app.route('/conselho')
def pega_conselho_api():
    frase = apis.pega_conselho()
    print(frase)
    return render_template('conselho.html', frase_aleatoria=frase)


@app.route('/cartas')
def jogo_cartas():
    lista_nipes_apos_10 = ['valete', 'dama', 'rei', 'ás']
    vencedor = None
    
    carta_jogador, carta_bot = apis.jogo_de_cartas()
    
    # dados jogador
    carta_jogador_image = carta_jogador['image']
    carta_jogador_valor = carta_jogador['value']
    carta_jogador_nipe = carta_jogador['suit']
    
    # dados bot
    carta_bot_image = carta_bot['image']
    carta_bot_valor = carta_bot['value']
    carta_bot_nipe = carta_bot['suit']
        
    if carta_jogador_valor > carta_bot_valor: vencedor = "Jogador"
    elif carta_bot_valor > carta_jogador_valor: vencedor = "Bot"
    else: vencedor = "empate"
    
    return render_template('jogo_cartas.html',
                        image_jogador=carta_jogador_image,
                        valor_jogador=carta_jogador_valor,
                        nipe_jogador=carta_jogador_nipe,
                        image_bot=carta_bot_image,
                        valor_bot=carta_bot_valor,
                        nipe_bot=carta_bot_nipe,
                        vencedor=vencedor
                        )

@app.route('/gerador_senha', methods=['GET', 'POST'])
def gera_senha():
    if request.method == 'POST':
        senha = gerar_senha.GeraSenha()
        senha.quant_letras = int(request.form['letras'])
        senha.quant_numeros = int(request.form['numeros'])
        senha.quant_simbolos = int(request.form['simbolos'])
        
        senha_gerada = senha.gerando_senha()
        print(senha_gerada)
        
        return render_template('gerador.html', resultado_senha=senha_gerada)
    
    return render_template('gerador.html')


@app.route('/animacao_com_css')
def animation():
    return render_template('animation.html')


# Execução
if __name__ == '__main__':
    app.run()
