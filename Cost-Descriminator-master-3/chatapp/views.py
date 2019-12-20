from django.shortcuts import render
import json
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
from chatapp import aocd,Links
# Create your views here.
def index(request):
	return render(request,'chatbot.html')

from chatterbot import ChatBot
from chatapp import extract_url
from chatterbot.comparisons import JaccardSimilarity
from chatterbot.response_selection import get_most_frequent_response

import logging

class ChatterBotApiView(View):
	chatterbot = ChatBot(
		'Chatterbot',
		storage_adapter='chatterbot.storage.SQLStorageAdapter',
		database_uri='sqlite:///django_chatterbot_statement.sqlite3',
		logic_adapters=[
			{
				"import_path": "chatterbot.logic.BestMatch",
				"statement_comparison_function": JaccardSimilarity,
				"response_selection_method":get_most_frequent_response,
				'default_response': 'I am sorry, but I do not understand.',
				'minimum_similarity_threshold': 0.10
			}
		]
	)
	try:
		def post(self, request, *args, **kwargs):
			print('post')
			input_data = json.loads(request.body.decode('utf-8'))
			print(input_data)
			y=["Apple iPhone XS","Apple Airpods","Samsung S10+","Fitbit Smartwatch","iPad  air", "Macbook air",
			 "Samsung Note 10+","Apple smartwatch","Lenovo ideapad","Samung S9+"]
			print(input_data['text'])		
			if input_data['text'] in y:
				#print("Here")
				x=aocd.AOCD(input_data['text'])
				#print(x)
				return JsonResponse({
					'text':x,
				})
			#extract_url.myfun(input_data)
			else:
			#self.chatterbot.
				response = self.chatterbot.get_response(input_data)
				print(response.confidence)
				response_data=extract_url.url_extract(response.text)
				print(response_data)
				logging.basicConfig(filename="./log.txt", format='%(asctime)s - %(message)s', datefmt="%d-%b-%y	 %H:%M:%S",
									level=logging.INFO)
				logging.info(f"{response_data} in response to {input_data}")
				if len(response_data)==2:
					return JsonResponse({
						'text':response_data['text'],
						'url':response_data['url']
					})
				else:
					return JsonResponse({
						'text':response_data['text']
					})
	except:
		#print("jiijjij")
		pass
	def get(self, request, *args, **kwargs):
		print('get')
		return JsonResponse({
			'name': self.chatterbot.name
		})