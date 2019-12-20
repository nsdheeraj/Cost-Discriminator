from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ListTrainer
#initializing chatbot
chatbot = ChatBot('Chatterbot',trainer='chatterbot.trainers.ListTrainer',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  database_uri='sqlite:///django_chatterbot_statement.sqlite3' )
#intializing trainer for chatbot
trainer = ListTrainer(chatbot)

#function for getting user input as yes or no
def get_feedback():
    text = input()
    if 'yes' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    else:
        print('Please type either "Yes" or "No"')

        return get_feedback()

#giving the responses to the user and asking him whether it is correct or not
while True:
    try:
        input_statement = Statement(text=input("user input:"))
        response = chatbot.generate_response(input_statement)
        print('\n Is "{}" a correct response to "{}" selected with confidence {} ? \n'.format(
            response.text,
            input_statement.text,
            response.confidence
        ))
        if not get_feedback():
            print('please input the correct one')
            correct_response = Statement(text=input())
            trainer.train([input_statement.text,correct_response.text])
            print('Responses added to bot!')


    except (KeyboardInterrupt, EOFError, SystemExit):
        break