import requests
import io
url = 'https://www.amazon.in/Redmi-Note-Pro-Storage-Processor/dp/B07X4PKGSN/ref=lp_20303904031_1_4?s=electronics&ie=UTF8&qid=1593676744&sr=1-4'
url2 = 'https://www.amazon.in/Redmi-Note-Space-Black-Storage/dp/B07X4PXKZ7'
response = requests.get('http://api.scrapestack.com/scrape?access_key=YOUR SCRAPSTRACK API HERE={}'.format(url2))
# xiaomittom 
#fname = open("myfile.txt", "w")
#f.write(response.content.decode("utf-8") )
#with io.open('myfile.txt', "w", encoding="utf-8") as f:     WORKING CODE
    #f.write(response.content.decode("utf-8"))
print(response.content.decode("utf-8").find('In stock.'))