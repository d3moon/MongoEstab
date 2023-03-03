
# Desafio 4 - MongoEstab

Este é um desafio que propõe criar uma tela onde dever ser realizado um CRUD utilizando o MongoDB como banco de dados, utilizando o a biblioteca Pymongo. 
A tela deve conter a lista dos estabelecimentos salvos no primeiro desafio, com os botões de adicionar, editar e excluir esses registros. 
O formulário para Adicionar e Editar os dados podem ser em outra tela ou em modal. Os campos de inputs do formulário devem conter máscaras e validação antes de salvar os dados.  

## Instalação


**Instalação via Docker do Desafio 1:**


*Por problemas de conexão de container não consegui conectar a tempo os registros do MongoDB do desafio1 via container com o desafio 4, porém funciona acessando de maneira local o desafio 4 e subindo a imagem do desafio 1 normalmente*

```bash
  cd EstabProcess
  docker stop $(docker ps -q) 
  docker-compose build
  docker-compose up
```

## Variáveis de Ambiente

Crie um .env na raiz do diretório do projeto e adicione essas variáveis:

```bash 
  SECRET_KEY=mysecretkey
  MONGODB_URI=mongodb://localhost:27017/
```


**Instalação local do Desafio 4:**

```bash
  cd MongoEstab
  pip install -r requirements.txt
  python app.py
```
    
## Authors

- [@João Victor F. Braga](https://www.linkedin.com/in/d3moon)

