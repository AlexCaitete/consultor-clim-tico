import requests
import os

API_KEY = "Sua_chave_aqui"
IDIOMA = "pt_br"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def consultar_clima():
    limpar_tela()
    CIDADE = input('Insira o nome da cidade que deseja saber o clima: ').upper().strip()

    link = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&lang={IDIOMA}&units=metric"
    resposta = requests.get(link) #nessa linha estamos dando a ordem dada de ir buscar as informações dadas na variavel link na biblioteca request e tranformando em uma nova variavel chamada resposta

    if resposta.status_code == 200:
        dados = resposta.json()

        #agora vamos entrar nas gavetas do json e extrair os dados que queremos
        nome = dados['name']
        temperatura = dados ['main']['temp']
        sensacao = dados ['main']['feels_like']
        descricao = dados['weather'][0]['description']

        #como vamos mostrar na tela
        print("-" * 30)
        print(f"🌆 Cidade: {nome}")
        print(f"🌡️ Temperatura: {temperatura:.1f}°C")
        print(f"🔥 Sensação Térmica: {sensacao:.1f}°C")
        print(f"☁️ Condição: {descricao.capitalize()}")
        print("-" * 30)

        #o conselho do BOT

        print("\n📢 CONSELHO DO BOT:")

        if "chuva" in descricao or "garoa" in descricao:
            print("☔ Leve um guarda-chuva! Vai molhar.")
        elif temperatura > 30:
            print("🥵 Está muito quente! Beba água e use roupas leves.")
        elif temperatura < 18:
            print(f"🥶 Que frio é esse em {nome}? Pegue um casaco!")
        else:
            print("😎 O clima está agradável. Aproveite o dia!")

    else:
        print(f"❌ Erro: {resposta.status_code}")


if __name__ == "__main__":
    consultar_clima()