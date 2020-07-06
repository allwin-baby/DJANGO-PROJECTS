from bs4 import BeautifulSoup 
from twilio.rest import Client 
import requests 
import re
from urllib.request import urlopen
import os  #for env varible

account_sid = 'ACbeaff05cb6617af6feac4ac0ab7eb3fc' 
client = Client(account_sid, os.environ.get('AUTH_TOKEN'))

url= [
    'https://www.flipkart.com/motorola-one-fusion-twilight-blue-128-gb/p/itm9c0e4b9b56acd?pid=MOBFRFXHZRMXDDNZ&lid=LSTMOBFRFXHZRMXDDNZOJ0LCZ&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_10_sc_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_10_sc_na_na&fm=SEARCH&iid=aaccc752-0cc9-4816-a744-eb47a1709f64.MOBFRFXHZRMXDDNZ.SEARCH&ppt=sp&ppn=sp&ssid=c0ky5llqv40000001593615239489&qH=cd4b251cae4b64cd',
    'https://www.flipkart.com/motorola-one-fusion-moonlight-white-128-gb/p/itm07749a481ee89?pid=MOBFRFXHHWBM6BRR&lid=LSTMOBFRFXHHWBM6BRRZXH93F&marketplace=FLIPKART&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_2_10_sc_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_10_sc_na_na&fm=SEARCH&iid=aaccc752-0cc9-4816-a744-eb47a1709f64.MOBFRFXHHWBM6BRR.SEARCH&ppt=sp&ppn=sp&ssid=c0ky5llqv40000001593615239489&qH=cd4b251cae4b64cd', 
]

def motoOneFusion(): 
    for each in url:
        r = requests.get(each)
        soup = BeautifulSoup(r.content, 'html5lib')
        pri = soup.find('div', attrs={'class':'_1vC4OE _3qQ9m1'})
        if (soup.body.findAll(text=re.compile('^BUY NOW$'))) :
            pri= pri.get_text().replace("₹","").replace(",","")
            message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Your appointment is coming up on {} at {}'.format(each,pri),      
                                to='whatsapp:+919744889488' 
                            ) 

