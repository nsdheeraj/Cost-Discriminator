import bs4
import Links
global AmazonPrice
global FlipkartPrice
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
#Define the product you intend to search for
productSearch = 'Apple iPhone XS'
my_a_url = Links.Amazon[productSearch]
my_f_url = Links.Flipkart[productSearch]
my_b_url = Links.Bajaj[productSearch]
print('Checking Online Stores...')
def AOCD(my_a_url,my_f_url,my_b_url):
#Scraping Amazon Product Price Tag
    uAClient = uReq(my_a_url)
    page_a_html = uAClient.read()
    uAClient.close()
    page_a_soup = soup(page_a_html, "html.parser") #Parsing the webpage
    priceA = page_a_soup.find(class_="a-size-medium a-color-price priceBlockBuyingPriceString")#Identifying the pricetag string from html using local class name.
    priceA = priceA.text
    priceA= priceA.strip('₹') #Stripping characters off the scraped result
    priceA = priceA.strip('\xa0')
    priceA = priceA.strip(" ' ")   
    AmazonPrice = priceA.replace(',','')
    AmazonPrice = float(AmazonPrice)
    print('You can get it in Flipkart for Rs.',AmazonPrice)
#Scraping Flipkart Product Price Tag
    uFClient = uReq(my_f_url)
    page_f_html = uFClient.read()
    uFClient.close()
    page_f_soup = soup(page_f_html, "html.parser") #Parsing the webpage
    priceF = page_f_soup.find(class_="_1vC4OE _3qQ9m1")#Identifying the pricetag string from html using local class name.
    priceF = priceF.text
    priceF = priceF.strip('₹')
    FlipkartPrice = priceF.replace(',','')
    FlipkartPrice= float(FlipkartPrice)
    print('You can get it in Flipkart for Rs.',FlipkartPrice)
#Comparing Price tags
    if AmazonPrice < FlipkartPrice:
        bestPrice = AmazonPrice
        print('Amazon is Cheaper at', bestPrice)

    if AmazonPrice > FlipkartPrice:   
        bestPrice = FlipkartPrice
        print('Flipkart  is Cheaper at', bestPrice)
        
    if AmazonPrice == FlipkartPrice:   
        bestPrice = AmazonPrice
        print('Both Products have same price at Amazon and Flipkart at',bestPrice)
    print('Checking Offline Stores...')
    try:
        ubClient = uReq(my_b_url)
        page_b_html = ubClient.read()
        ubClient.close()
        page_b_soup = soup(page_b_html, "html.parser")
        priceB = page_b_soup.find(class_="pro-details actual-price")
        priceB = priceB.text
        BajajPrice = priceB.strip('₹')
        BajajPrice = BajajPrice.strip('Rs.')
        BajajPrice = BajajPrice.replace(',','')
        print('Bajaj Electronics is selling it for ',BajajPrice)
        if BajajPrice < bestPrice:
            print('The product is cheaper offline at Bajaj Electronics than online platforms ')
    except:
        print('This product is temporarily unavailable in offline stores')

AOCD(my_a_url,my_f_url,my_b_url) 
