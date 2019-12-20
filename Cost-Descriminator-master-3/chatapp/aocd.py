import bs4
from chatapp import Links
import urllib
#Importing everything needed for scraping the platforms
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
Platforms = {
    'amazon':0,
    'flipkart':0,
    'bajaj':0
}
#Define the product you intend to search for
productSearch = 'Apple Airpods'

print('Checking Online Stores...') 
def AOCD(productSearch):
	my_a_url = Links.Amazon[productSearch]
	my_f_url = Links.Flipkart[productSearch]
	my_b_url = Links.Bajaj[productSearch]
	#Scraping Amazon Product Price Tag
	#print("Here")
	bestPrice = []
	def Az(my_a_url,Platforms):
		#uAClient = uReq(my_a_url)
		opener = urllib.request.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		#page = requests.get(my_a_url)
		#html_contents = page.text
		response = opener.open(my_a_url)
		html_contents = response.read()
		#print(html_contents)
		#page_a_html = uAClient.read()
		#uAClient.close()
		page_a_soup = soup(html_contents, "html.parser") #Parsing the webpage
		priceA = page_a_soup.find(class_="a-size-medium a-color-price priceBlockBuyingPriceString")#Identifying the pricetag string from html using local class name.
		#print(priceA)
		priceA = priceA.text
		priceA= priceA.strip('₹') #Stripping characters off the scraped result
		priceA = priceA.strip('\xa0')
		priceA = priceA.strip(" ' ")   
		AmazonPrice = priceA.replace(',','')
		bestPrice.append(AmazonPrice)
		Am = 'You can get it on Amazon for Rs.'+ AmazonPrice
		return Am
    #Scraping Flipkart Product Price Tag
	def Fp(my_f_url,Platforms):
		uFClient = uReq(my_f_url)
		page_f_html = uFClient.read()
		uFClient.close()
		page_f_soup = soup(page_f_html, "html.parser") #Parsing the webpage
		priceF = page_f_soup.find(class_="_1vC4OE _3qQ9m1")#Identifying the pricetag string from html using local class name.
		priceF = priceF.text
		priceF = priceF.strip('₹')
		FlipkartPrice = priceF.replace(',','')
		FlipkartPrice= FlipkartPrice
		bestPrice.append(FlipkartPrice)
		Fk = 'You can get it on Flipkart for Rs.'+ FlipkartPrice
		return Fk

	def bj(my_b_url,Platforms):
		ubClient = uReq(my_b_url)
		page_b_html = ubClient.read()
		ubClient.close()
		page_b_soup = soup(page_b_html, "html.parser")
		priceB = page_b_soup.find(class_="pro-details actual-price")
		priceB = priceB.text
		BajajPrice = priceB.strip('₹')
		BajajPrice = BajajPrice.strip('Rs.')
		BajajPrice = BajajPrice.replace(',','')
		bestPrice.append(BajajPrice)
		be = 'You can get it on Bajaj Electronics for Rs.'+ BajajPrice
		return be  
	A = Az(my_a_url,Platforms)
	F = Fp(my_f_url,Platforms)
	print('Checking Offline Stores...')
	B = bj(my_b_url,Platforms)
	C = A+F + B
	return C
#print(AOCD(my_a_url,my_f_url,my_b_url))