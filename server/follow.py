import requests
from bs4 import BeautifulSoup
import time
from db.databeConnection import collection
from dotenv import load_dotenv
import os
load_dotenv()
def followProduct(url):
    url1 = os.getenv("URL") + url
    userAgent = os.getenv("USER_AGENT") + url
    headers= {
        "User-Agents":userAgent
    }

    page = ''
    while page == '':
        try:
            page = requests.get(url1, headers=headers)
            break
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            
        continue


    htmlPage =  BeautifulSoup(page.content , "html.parser")
    bookImage = htmlPage.select(".js-prd-first-image")
    bookTitle = htmlPage.findAll("h1" , "fs-7")
    bookPrice = htmlPage.findAll("span" , "current-price")
    bookFeatures = htmlPage.select('.product-property > ul.nav')
    productDescription = htmlPage.findAll("div" , "product-description-header")


    for item0 in productDescription:
        product_description = item0.prettify()
    for item1 in bookFeatures:
        book_features = item1.prettify()
    for item2 in bookPrice:
        book_price = item2.get_text()
    for item3 in bookTitle:
        book_title = item3.get_text()
    for item4 in bookImage:
        book_img = item4["src"][44:]

    insertProduct = {
        "book_img":book_img,
        "book_title":book_title,
        "book_price":book_price,
        "book_features":book_features,
        "product_description":product_description,
        "url":url1
    }


    return collection.insert(insertProduct);



