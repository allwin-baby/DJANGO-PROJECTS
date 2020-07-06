from bs4 import BeautifulSoup 
from twilio.rest import Client 
import requests 
import re
from urllib.request import urlopen
import os  #for env varible

account_sid = 'ACbeaff05cb6617af6feac4ac0ab7eb3fc' 
client = Client(account_sid, os.environ.get('AUTH_TOKEN')) # AUTH_TOKEN IS ENV VARIABLE IN HEROKU DEPLOYMENT

url= [
    'https://www.flipkart.com/motorola-one-fusion-twilight-blue-128-gb/p/itm9c0e4b9b56acd?pid=MOBFRFXHZRMXDDNZ&lid=LSTMOBFRFXHZRMXDDNZOJ0LCZ&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=4afdbdf7-1003-48ea-a6dc-f6f9f8194135.MOBFRFXHZRMXDDNZ.SEARCH&ppt=sp&ppn=sp&ssid=5awtwrhw08k7fuo01593614857456&qH=446d563d7c6f2f52',
    'https://www.flipkart.com/motorola-one-fusion-moonlight-white-128-gb/p/itm07749a481ee89?pid=MOBFRFXHHWBM6BRR&lid=LSTMOBFRFXHHWBM6BRRZXH93F&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=4afdbdf7-1003-48ea-a6dc-f6f9f8194135.MOBFRFXHHWBM6BRR.SEARCH&ppt=sp&ppn=sp&ssid=5awtwrhw08k7fuo01593614857456&qH=446d563d7c6f2f52',
    'https://www.flipkart.com/motorola-one-fusion-twilight-blue-128-gb/p/itm9c0e4b9b56acd',
    'https://www.flipkart.com/motorola-one-fusion-moonlight-white-128-gb/p/itm07749a481ee89',
    'https://www.flipkart.com/search?q=motorola%20one%20fusion&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',
    'https://www.flipkart.com/motorola-one-fusion-twilight-blue-128-gb/p/itm9c0e4b9b56acd?pid=MOBFRFXHZRMXDDNZ&lid=LSTMOBFRFXHZRMXDDNZOJ0LCZ&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_10_sc_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_10_sc_na_na&fm=SEARCH&iid=aaccc752-0cc9-4816-a744-eb47a1709f64.MOBFRFXHZRMXDDNZ.SEARCH&ppt=sp&ppn=sp&ssid=c0ky5llqv40000001593615239489&qH=cd4b251cae4b64cd',
    'https://www.flipkart.com/motorola-one-fusion-moonlight-white-128-gb/p/itm07749a481ee89?pid=MOBFRFXHHWBM6BRR&lid=LSTMOBFRFXHHWBM6BRRZXH93F&marketplace=FLIPKART&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_2_10_sc_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_10_sc_na_na&fm=SEARCH&iid=aaccc752-0cc9-4816-a744-eb47a1709f64.MOBFRFXHHWBM6BRR.SEARCH&ppt=sp&ppn=sp&ssid=c0ky5llqv40000001593615239489&qH=cd4b251cae4b64cd',
    'https://www.flipkart.com/poco-x2-matrix-purple-64-gb/p/itm2db9fa45189d2?pid=MOBFZGJ6HY6H4JHU&lid=LSTMOBFZGJ6HY6H4JHU7XKMPX&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&fm=SEARCH&iid=96b5d03a-6494-42a8-b379-cec316d51b09.MOBFZGJ6HY6H4JHU.SEARCH&ppt=sp&ppn=sp&ssid=que6tkd9kw0000001593618977402&qH=4e0be2db3051d600',
    'https://www.flipkart.com/realme-narzo-10a-so-white-32-gb/p/itmbeb412dade152?pid=MOBFQ36ASQHV3UGW&lid=LSTMOBFQ36ASQHV3UGWL3NPOI&fm=neo%2Fmerchandising&iid=M_f4ba9f72-d142-4681-81a2-a4d66eac8a00_14.4O0MZVDSXAQX&ppt=clp&ppn=mobile-phones-store&otracker=clp_omu_Best%2BBattery%2BPhones_2_14.dealCard.OMU_Best%2BBattery%2BPhones_mobile-phones-store_4O0MZVDSXAQX_10&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Best%2BBattery%2BPhones_NA_dealCard_cc_2_NA_view-all_10&cid=4O0MZVDSXAQX',
    'https://www.flipkart.com/infinix-hot-9-violet-64-gb/p/itm9d816e65b5dc4?pid=MOBFQ3DPMQHHTMBZ&lid=LSTMOBFQ3DPMQHHTMBZTNJSFM&marketplace=FLIPKART&srno=b_1_1&otracker=hp_reco_Top%2BSelection_1_21.dealCard.OMU_Top%2BSelection_cid%3AS_F_N_tyy_4io__bs___NONE_ALL%3Bnid%3Atyy_4io_%3Bet%3AS%3Beid%3Atyy_4io_%3Bmp%3AF%3Bct%3Ab%3B_16&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2FC6_Top%2BSelection_DESKTOP_HORIZONTAL_dealCard_cc_1_NA_view-all_16&fm=personalisedRecommendation%2FC6&iid=32eb742a-e1c9-458b-9fbe-20ceaed33eb5.MOBFQ3DPMQHHTMBZ.SEARCH&ppt=browse&ppn=browse&ssid=qetpwlj4vk0000001593616008870',
    'https://www.flipkart.com/motorola-g8-power-lite-royal-blue-64-gb/p/itm8a408329ff3d2?pid=MOBFZ5EXNSGJJ2ZR&lid=LSTMOBFZ5EXNSGJJ2ZRBFFMHB&marketplace=FLIPKART&srno=b_2_37&otracker=hp_reco_Top%2BSelection_1_21.dealCard.OMU_Top%2BSelection_cid%3AS_F_N_tyy_4io__bs___NONE_ALL%3Bnid%3Atyy_4io_%3Bet%3AS%3Beid%3Atyy_4io_%3Bmp%3AF%3Bct%3Ab%3B_16&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2FC6_Top%2BSelection_DESKTOP_HORIZONTAL_dealCard_cc_1_NA_view-all_16&fm=personalisedRecommendation%2FC6&iid=e16ef4a2-9a9c-4043-a5eb-af2b3cb17595.MOBFZ5EXNSGJJ2ZR.SEARCH&ppt=browse&ppn=browse',
    'https://www.flipkart.com/mi-a3-kind-grey-64-gb/p/itm280ef520ac1d9?pid=MOBFJM4ZZW6NTSZH&lid=LSTMOBFJM4ZZW6NTSZHU6DTVH&marketplace=FLIPKART&srno=b_1_23&otracker=nmenu_sub_Electronics_0_Mi&fm=SEARCH&iid=5e19ef6c-ff53-41f9-900d-005fd44a983b.MOBFJM4ZZW6NTSZH.SEARCH&ppt=browse&ppn=browse&ssid=n5p9zn1jhc0000001593621332253',
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

