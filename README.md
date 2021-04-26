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
* Sqlite Online

## Como Utilizar 
Caso não tenha o Python instalado em sua máquina, por favor consulte a documentação [aqui], caso já o tenha é interessante criar um ambiente virtual para não atrapalhar seus outros projetos, para isto utilizei o [Venv].

Com todo seu ambiente configurado vamos dar início.
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
![Tree Project](https://github.com/btiagor/Fato-ou-Fake/blob/master/fato_fake/fato_fake/readme_imagens/tree_project.png)
* Essa é a estrutura básica gerada pelo Scrapy.

## Web Crawler
* Para criar uma spider precisamos dar um nome (aosfatos) e o Domínio (aosfatos.org) onde ela irá atuar.
```python
 $ scrapy genspider aosfatos aosfatos.org
```
* Esse comando irá criar um arquivo chamado aosfatos.py no diretório spiders do nosso projeto com esse formato.
![Model Spyderr](https://github.com/btiagor/Fato-ou-Fake/blob/master/fato_fake/fato_fake/readme_imagens/modelo_spider.png)
* Com auxílio do seu editor favorito altere o código para está forma e salve.
```python
start_urls = ['https://www.aosfatos.org/noticias']

def parse(self, response):
    # retorna o título da página
    self.log(response.xpath('//title/text()').extract_first())
```
* Pronto agora basta executar
```python
$ scrapy crawl aosfatos
```
* Caso encontre o erro abaixo, que foi o nosso caso, quer dizer que o site não tem o arquivo robots.txt, arquivo de configuração onde sites podem colocar restrições para bots. Para resolver esse problema vamos no arquivo settings.py que fica localizado na raiz do nosso projeto e alterar a linha ROBOTSTXT_OBEY para False, por default ela vem True.
![Erro Falta do robot.txt](https://github.com/btiagor/Fato-ou-Fake/blob/master/fato_fake/fato_fake/readme_imagens/erro%20301.png) 
* Como uma boa prática é necessário limitar a velocidade com que o Scrapy faz requisições. Dependendo da quantidade de requisições feitas você pode congestionar o servidor target, então alteramos mais uma propriedade no settings.py DOWNLOAD_DELAY = 3 (por padrão ela está comentada). Esse valor é referente ao tempo em segundos entre as requisições, deixaremos ele em 1.5 para nosso teste.
* Depois das auterações execute o comando anterior novamente e deve receber uma resposta positiva.
* A versão final dessa spyder está comentada e completa no projeto.
* Para persistir os dados utilizamos o [Sqlite].

![Criando Tabela](https://github.com/btiagor/Fato-ou-Fake/blob/master/fato_fake/fato_fake/readme_imagens/criando%20banco.png)

> Linha 1: Importando Sqlite que é nativo no Python
> Linha 2: Nome do nosso Banco
> Linha 3: Criando uma conexão com o nosso banco, caso ele não exista é criado.
> Linha 5: Fazemos uma validação de segurança para checar se nossa tabela já existe no banco.
> Linha 8 à 19: Campos que iremos criar.
> Linha 21: Fechando a conexão com o banco.

## Item Pipeline
* Utilizamos o Item Pipeline para fazer o processamento dos dados obtidos pelo Web Crawler. Vamos novamente no settings.py e descomentar o ITEM_PIPELINES e editar como mostrado abaixo:
```python
ITEM_PIPELINES = {
    'fato_fake.pipelines.AosFatosPipeline': 300,
 }
```
* Vamos no arquivo pipeline.py editar desta forma:
![Pipeline](https://github.com/btiagor/Fato-ou-Fake/blob/master/fato_fake/fato_fake/readme_imagens/pipeline.png) 


## Web Scraping
* Vamos raspar o site em busca de URLs agora.
* Criando nosso CrawlSpider

```python
 $ scrapy genspider -t crawl aosfatos_scraping aosfatos.org
```
* -t significa que queremos o template crawl
* Após criação editamos para que ele fique dessa forma.
![Modelo Scraping](https://github.com/btiagor/Fato-ou-Fake/blob/master/fato_fake/fato_fake/readme_imagens/scraping.png)
> Linha 8: Domínio do site
> Linha 9: URL inicial da pesquisa 
> Linha 11: Outra forma de limitar o tempo entre as requisições
> Linha 15: Regras para fazer a pesquisa, o **allow=noticias** será nossa base de pesquisa, toda URL da página que contiver o **noticias** ira ser lida, **callback=parse_news** é nossa função de extração de links e por fim **follow=True** informa que devemos seguir o sistes dado match pelo **LinkExtractor**
> Linha 21: Nosso retorno da função contendo o link encontrado
* Com edição feita basta executar dessa forma.
```python
 $ scrapy crawl aosfatos_scraping -o links_aosfatos.json
```
* A novidade desse comando é que estamos escrevendo um arquivo de saída no formato JSON


## Versão

1.0.0.0


## Autor

* **Tiago Bezerra**: [@btiagor]

## Referências
* **[Scrapy]**
* **[Venv]**
* **[Sqlite]**
* **[Sqlite Online]**

Qualquer dúvida ou sugestões pode entrar em contato, estou a disposição.

[//]: # (Estes são so links utilizados no corpo desse note e os sites de refeência para produzir o conteúdo.)
[aqui]: <https://www.python.org/doc/>
[@btiagor]: <https://github.com/btiagor>
[Venv]: <https://docs.python.org/3/tutorial/venv.html>
[Sqlite]: <https://www.sqlitetutorial.net/>
[Scrapy]: <https://www.tutorialspoint.com/scrapy/index.htm>
[Sqlite Online]: <https://sqliteonline.com/>
