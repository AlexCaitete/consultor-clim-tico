# 🌦️ Consultor Climático + Histórico SQL

Uma ferramenta de engenharia de dados que consome a API da OpenWeatherMap, processa as informações climáticas e **persiste os dados** em um banco de dados relacional local.

Este projeto simula um pipeline de dados simples: **Extração** (API), **Transformação** (Lógica de conselhos) e **Carregamento** (SQLite).

## 🚀 Funcionalidades

- **Monitoramento em Tempo Real:** Consulta temperatura, sensação térmica e condições do clima.
- **Persistência de Dados (SQL):** Cada consulta é salva automaticamente em um arquivo `historico_clima.db`.
- **Inteligência Condicional:** O sistema analisa os dados e oferece recomendações (ex: "Leve guarda-chuva", "Beba água").
- **Tratamento de Erros:** Gestão robusta de respostas HTTP (404, 401).

## 🛠️ Stack Tecnológica

- **Python 3.12**
- **SQLite3** (Banco de Dados embutido)
- **Requests** (Consumo de API REST)
- **Datetime** (Log temporal)

## 📦 Como usar

### 1. Instalação
```bash
git clone [https://github.com/SEU-USUARIO/consultor-climatico.git](https://github.com/SEU-USUARIO/consultor-climatico.git)
cd consultor-climatico
pip install requests
