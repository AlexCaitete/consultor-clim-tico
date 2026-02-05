import requests
import os
import sqlite3
from datetime import datetime


API_KEY = [COLOQUE SUA CHAVE AQUI]
IDIOMA = "pt_br"


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def criar_banco():
    conexao = sqlite3.connect('historico_clima.db')
    cursor = conexao.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS consultas
                   (
                       id INTEGER PRIMARY KEY AUTOINCREMENT, cidade TEXT, temperatura REAL, condicao TEXT, data_hora TEXT)''')
    conexao.commit()
    conexao.close()
    


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


if __name__ == "__main__":

    consultar_clima()

