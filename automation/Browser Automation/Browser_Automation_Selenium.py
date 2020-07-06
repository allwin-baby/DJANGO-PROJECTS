from selenium import webdriver
import time
browser =webdriver.Chrome(r"E:\django\trialprojects\chromedriver.exe") 
# Add ----->        E:\django\trialprojects\    envoronment varibale because -> E:\django\trialprojects\chromedriver.exe
# chromedriver --v
#  #browser =webdriver.Chrome('E:\django\trialprojects\chromedriver.exe') didnt work 
browser.get('https://www.flipkart.com/motorola-one-fusion-moonlight-white-128-gb/p/itm07749a481ee89?pid=MOBFRFXHHWBM6BRR&lid=LSTMOBFRFXHHWBM6BRRZXH93F&marketplace=FLIPKART&srno=s_1_2&otracker=AS_Query_HistoryAutoSuggest_1_5_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_5_na_na_na&fm=SEARCH&iid=2f1383a8-6bc1-49a3-95c2-f790838101db.MOBFRFXHHWBM6BRR.SEARCH&ppt=sp&ppn=sp&ssid=8hdwcdwpi80000001593585920695&qH=446d563d7c6f2f52')
# before opening the new window
#if (browser.find_element_by_class_name("_2AkmmA _29YdH8")):
   # print("yes")
 
if(browser.find_elements_by_link_text('Get notified when this item comes back in stock.')):
   print("found")


