import requests
import os
import sqlite3
from datetime import datetime

#CRIAÇÃO DA CHAVE DE ACESSO QUE VOCÊ PRECISA GERAR NO SITE https://openweathermap.org/ E ESCOLHA DO IDIOMA
API_KEY = "COLOQUE SUA CHAVE AQUI"
IDIOMA = "pt_br"

#FUNÇÃO PRA LIMPAR A TELA
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#FUNÇÃO PRA CRIAR O BANCO DE DADOS AS FUNÇÕES E COMANDO QUE ESTÃO DENTRO DESSA FUNÇÃO, SÃO FUNÇÕES JÁ DETERMINADAS PELO DICIONÁRIO SQLITE3
def criar_banco():
    conexao = sqlite3.connect('historico_clima.db')
    cursor = conexao.cursor()

# AQUI ESTAMOS DANDO OS COMANDO PARA MONTAR A PLANILHA EXATAMENTE COMO QUEREMOS COM AS COLUNAS EXATAS E SÓ COM OS DADOS DESEJADO
    # id: nome da coluna(identificador), INTEGER: só aceita números.
    # PRIMARY: é o CPF da linha. significa que esse número nunca pode se repetir
    #AUTOINCREMETE:Você não precisa dizer o número. O banco conta sozinho: 1, 2, 3... Se você apagar o 2, o próximo continua sendo o 4.
    #cidade TEXT - Cria uma coluna chamada "cidade" que só aceita Texto.
    #temperatura REAL - Cria uma coluna "temperatura" E O REAL: Significa "Número Real" (com vírgula/ponto). Se fosse INTEGER, ele arredondaria 29.5 para 29. Aqui ele aceita o decimal.
    #condicao TEXT e data_hora TEXT - Colunas de texto simples para guardar a descrição ("Céu limpo") e a data.
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS consultas #CRIE UMA TABELA CHAMA CONSULTA
                   (id INTEGER PRIMARY KEY AUTOINCREMENT, cidade TEXT, temperatura REAL, condicao TEXT, data_hora TEXT)''')
    conexao.commit()
    conexao.close()


#função para salvar no BD
def salvar_no_banco(cidade, temp, condicao):
    conexao = sqlite3.connect('historico_clima.db')
    cursor = conexao.cursor()

    data_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    cursor.execute('''
                   INSERT INTO consultas (cidade, temperatura, condicao, data_hora)
                   VALUES (?, ?, ?, ?)
                   ''', (cidade, temp, condicao, data_atual))

    conexao.commit()
    conexao.close()
    
    print("💾 Dados salvos no histórico com sucesso!")

#função para consultar o BD
def consultar_clima():
    limpar_tela()
    criar_banco()  # Garante o banco, mas fica em silêncio

    CIDADE = input('Insira o nome da cidade que deseja saber o clima: ').upper().strip()

    print(f"\n📡 Buscando dados para {CIDADE}...")

    link = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&lang={IDIOMA}&units=metric"
    resposta = requests.get(link)

    if resposta.status_code == 200:
        dados = resposta.json()

        nome = dados['name']
        temperatura = dados['main']['temp']
        sensacao = dados['main']['feels_like']
        descricao = dados['weather'][0]['description']

        print("-" * 30)
        print(f"🌆 Cidade: {nome}")
        print(f"🌡️ Temperatura: {temperatura:.1f}°C")
        print(f"🔥 Sensação Térmica: {sensacao:.1f}°C")
        print(f"☁️ Condição: {descricao.capitalize()}")
        print("-" * 30)

        # Salva no banco e avisa
        salvar_no_banco(nome, temperatura, descricao)

        print("\n📢 CONSELHO DO BOT:")

        if "chuva" in descricao or "garoa" in descricao:
            print("☔ Leve um guarda-chuva! Vai molhar.")
        elif temperatura > 30:
            print("🥵 Está muito quente! Beba água e use roupas leves.")
        elif temperatura < 18:
            print(f"🥶 Que frio é esse em {nome}? Pegue um casaco!")
        else:
            print("😎 O clima está agradável. Aproveite o dia!")

    elif resposta.status_code == 404:
        print("❌ Cidade não encontrada.")
    else:
        print(f"❌ Erro: {resposta.status_code}")

#executar o programa
if __name__ == "__main__":

    consultar_clima()
