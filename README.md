# 🌦️ Consultor Climático Inteligente (Python + SQL)

Um sistema de consulta meteorológica desenvolvido em **Python** que integra consumo de APIs RESTful com persistência de dados em Banco Relacional (SQLite).

O projeto não apenas exibe dados brutos, mas aplica uma **lógica de negócios** para fornecer recomendações personalizadas ao usuário baseadas nas condições climáticas atuais, além de manter um histórico de todas as consultas realizadas.

## 🚀 Funcionalidades

- **Consumo de API:** Conexão com a `OpenWeatherMap` para extração de dados em tempo real (JSON).
- **Tratamento de Dados:** Parsing de JSON para extrair temperatura, sensação térmica e descrições.
- **Lógica Condicional:** Sistema de "Conselheiro" que sugere ações (levar guarda-chuva, beber água, etc.) com base em parâmetros climáticos.
- **Persistência de Dados (SQL):** Integração com **SQLite** para salvar automaticamente cada consulta (Cidade, Temperatura, Data/Hora) em um banco de dados local.
- **Tratamento de Erros:** Gestão de erros HTTP (404 - Cidade não encontrada).

## 🛠️ Tecnologias Utilizadas

- **Python 3.12+**
- **Requests** (Requisições HTTP/REST)
- **SQLite3** (Banco de Dados Relacional)
- **Datetime** (Manipulação Temporal)
- **JSON** (Intercâmbio de dados)

## 📦 Como rodar o projeto

### Pré-requisitos
Você precisa ter o Python instalado.

```bash
# 1. Clone o repositório
git clone [https://github.com/SEU-USUARIO/consultor-climatico.git](https://github.com/SEU-USUARIO/consultor-climatico.git)

# 2. Entre na pasta
cd consultor-climatico

# 3. Instale a biblioteca de requisições
pip install requests
