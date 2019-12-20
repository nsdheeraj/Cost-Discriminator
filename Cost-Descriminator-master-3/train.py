from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#initializing chatbot
chatbot = ChatBot('Chatterbot',trainer='chatterbot.trainers.CorpusTrainer',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  database_uri='sqlite:///django_chatterbot_statement.sqlite3' )
import logging
#initializing trainer
trainer = ChatterBotCorpusTrainer(chatbot)

#training the chatbot with yml files present in the location specified
trainer.train( './training_data/' )

#logging to the console when the data is entered
logging.basicConfig(filename="./log.txt",format='%(asctime)s - %(message)s', datefmt="%d-%b-%y  %H:%M:%S",level=logging.INFO)
logging.info('Training data added to database')