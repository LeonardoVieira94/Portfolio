from bs4 import BeautifulSoup
import requests
import win32com.client as win32
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import pymongo
from db import CLIENT
import pythoncom


sched = BlockingScheduler()


#Função que busca os preços baseado nos links fornecidos no mongoDB
def precos(URL):

    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36" }
    site = requests.get(URL, headers=headers)

    soup = BeautifulSoup(site.content, 'html.parser')

    title = soup.find("h1", class_ ='MuiTypography-root').get_text()

    price = soup.find('div',class_ ="jss82" ).get_text()

    data = lambda: datetime.now().strftime('%d-%m-%Y %H:%M:%S')

   

    num_price = price[2:7]
    num_price = num_price.replace(',', '')

    num_price = float(num_price)

    return title, num_price, data

#definindo variaveis globais para enviar Email de notificação apenas uma vez
precoProc = False
precoPlaca = False

@sched.scheduled_job('interval', seconds=10)
def update_database():
    global precoProc, precoPlaca
    client = pymongo.MongoClient(CLIENT)
    db = client['AMZ']
    collection_name = db['links']
    busca = collection_name.find_one()
    #Busca links disponibilizados no mongo DB
    for chave, valor in busca.items():
        if chave == 'link':
            i = valor
            produtos = []
    for item in i:
        if item not in produtos:
            title, num_price, data = precos(item)
            if 'Processador' in title:
                if num_price < 1100 and precoProc == False:
                    send_email(item, num_price, title)
                    precoProc = True
            elif 'Placa' in title and precoPlaca == False:
                if num_price < 2000:
                    send_email(item, num_price, title)
                    precoPlaca = True
            produtos.append(item) # Envia link para lista, evitando que repita o mesmo produto várias vezes
            atualizacao = 'monitor'
            db[atualizacao].update_one({'Produto': title}, {'$push' : {'Data' : data(), 'Preço' : num_price}}, upsert = True)
    client.close()



def send_email(URL, price, name):
   # criar a integração com o outlook
    outlook = win32.Dispatch('outlook.application', pythoncom.CoInitialize())
    send_account = None
    for account in outlook.Session.Accounts:
        if account.DisplayName == 'leonardovieira_94@hotmail.com':
            send_account = account
            break

    destino = 'leonardovieira_94@hotmail.com'
    # criar um email
    email = outlook.CreateItem(0)

    email._oleobj_.Invoke(*(64209, 0, 8, 0, send_account))

    # configurar as informações do seu e-mail
    email.To = f'{destino}'
    if 'Processador' in name:
        email.Subject = 'Preço do processador baixou!'
        email.HTMLBody = f"""O preço do processador <b>baixou!</b> está custando {price}.<br>Segue link: {URL}
    """
    elif 'Placa' in name:
        email.Subject = 'Preço da placa baixou!'
        email.HTMLBody = f"""O preço da placa <b>baixou!</b> está custando {price}.<br>Segue link: {URL}
    """


    email.send()
    print("Email Enviado")

sched.start()