# Fato ou Fake

Este projeto tem como objetivo pôr em prática conhecimentos em Web Crawlers, Web Scraping, SQL, Engenharia de dados e Ciência dos dados.
Utilizamos os sites abaixo para fazer o estudo:
| Organização | URL |
| ------ | ------ |
| Ministério da Saúde | https://antigo.saude.gov.br/fakenews/ |
| AosFatos | https://www.aosfatos.org/ |


## Tecnologias

Aqui estão as tecnologias utilizadas no projeto

* Python 3.
* Scrapy 


## Serviços Utilizados

* Github
* Dillinger

## Como Utilizar
Caso não tenha o Python instalado em sua máquina, por favor consulte a documentação [aqui], caso já o tenha é interessante criar um ambiente virtual para não atrapalhar seus outros projetos, para isto utilizei o [Venv].

Contudo seu ambiente configurado vamos dar incício.
* Instalando Scrapy
```python
$ pip install scrapy
```
* Caso tenha mais de uma versão do Python é necessário fazer a identificação do pip
```python
$ pip3 install scrapy
```
* Após a instalação, vamos criar nosso projeto em um diretório de sua preferência chamado fato_ou_fake
```python
$ scrapy startproject fato_ou_fake
```
* Com isso é criado uma pasta chamada fato_ou_fake no diretório atual com essa estrutura:
![tree project](tree_project)
* Essa é a estrutura básica gerada pelo Scrapy

## Web Crawler
* Para criar uma spider precisamos dar um nome (aosfatos) a ela e o Domínio (aosfatos.org) onde ela irá atuar.
```python
 $ scrapy genspider aosfatos aosfatos.org
```
* Esse comando irá criar um arquivo chamado aosfatos.py no diretório spiders do nosso projeto com esse formato.
![model spider](modelo_spider)
* Com auxílio do seu editor favorito altere o código para está forma e salve a alteração
```python
start_urls = ['https://www.aosfatos.org/noticias']

def parse(self, response):
    # retorna o título da página
    self.log(response.xpath('//title/text()').extract_first())
```
* Pronto agora basta executar
```python
$ spider crawl aosfatos
```
* Caso encontre o erro abaixo, que foi o nosso caso, quer dizer que o site não tem o arquivo robots.txt, arquivo de configuração onde sites podem colocar restrições para bots. Para resolver esse problema vamos no arquivo settings.py que fica localizado na raiz do nosso projeto e alterar a linha ROBOTSTXT_OBEY para False, por default ela vem True.
![erro robot](erro) 
* Como uma boa prática é necessário limitar a velocidade com que o Scrapy faz requisições. Dependendo da quantidade de requisições feitas você pode congestionar o servidor target, então alteramos mais uma propriedade no settings.py DOWNLOAD_DELAY = 3 (por padrão ela está comentada). Esse valor é referente ao tempo em segundos entre as requisições, deixaremos ele em 1.5 para nosso teste.
* Depois das auterações execute o comando anterior novamente e deve receber uma resposta como esta.
![tudo certo](tudo certo) 
* Depois desses passos basta estudar o HTML do site e buscar os dados que deseja salvar com a spyder.
* Para persistir os dados utilizamos o [Sqlite].
![criando banco](criando banco)



## Features

  - Here will be the features.


## Links

  - Link of deployed application: (if has been deployed)
  - Repository: https://link_of_repository
    - In case of sensitive bugs like security vulnerabilities, please contact
      YOUR EMAIL directly instead of using issue tracker. We value your effort
      to improve the security and privacy of this project!


## Versão

1.0.0.0


## Autor

* **Tiago Bezerra**: [@btiagor]

## Referências
* **[Scrapy]**
* **[Venv]**
* **[Sqlite]**

[//]: # (Estes são so links utilizados no corpo desse note e os sites de refeência para produzir o conteúdo.)
[aqui]: <https://www.python.org/doc/>
[@btiagor]: <https://github.com/btiagor>
[Venv]: <https://docs.python.org/3/tutorial/venv.html>
[Sqlite]: <https://www.sqlitetutorial.net/>
[Scrapy]: <https://www.tutorialspoint.com/scrapy/index.htm>
