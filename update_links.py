from pymongo import MongoClient
from db import CLIENT
from datetime import datetime
links = []
op = ''
while op != 'nao':
    i = input('Forneça o link: ')
    links.append(i)
    op = input('Deseja inserir mais algum link?')

client = MongoClient(CLIENT)
db = client['AMZ']
collection_name = db['links']

'''for link in links:
    db['links'].update_one({'Links': 'Lista de Links'}, {'$push':{'link' : link }}, upsert=True)'''


#mostra os links disponíveis no database
busca = collection_name.find_one()

for chave, valor in busca.items():
    if chave == 'link':
        for link in links:
            if link not in valor:
                db['links'].update_one({'Links': 'Lista de Links'}, {'$push':{'link' : link }}, upsert=True)
