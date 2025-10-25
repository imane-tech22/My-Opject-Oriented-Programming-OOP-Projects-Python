
#Project one
import datetime
import time
print('Starting project number one.....\n\n')
time.sleep(3)
class Message:
    def __init__(self, sender, receiver, content, date_now=datetime.datetime.today()):
        self.sender = sender
        self.receiver= receiver
        self.content = content
        self.date_now = date_now
    def display_message(self):
        print(f'Sender: {self.sender}\nReceiver: {self.receiver}\nContent: {self.content}\nDate Now: {self.date_now}')

def create_message():
    while True:
       sender=input('Enter the name of sender')
       if sender:
           break
       else:
           print('Please enter a sender')
    while True:
        receiver=input('Enter the name of receiver')
        if receiver:
            break
        else:
            print('Enter a value')
    while True:
        content=input('Enter the content of message')
        if content:
            break
        else:
            print('Enter a value')

    return Message(sender,receiver,content)
message_info=create_message()
message_info.display_message()





#Project 2
print('\n\n\nStarting project number two.....\n\n')
time.sleep(3)

class Profile:
   def __init__(self, user_names, emails, languages):
      self.emails = emails
      self.user_names = user_names
      self.languages = languages
   def display_profile(self):
       print(f'User name :{self.user_names}\nEmail : {self.emails}\nLanguage: {self.languages}')

def create_profile():
    while True:
        user_names = input('Enter your name')
        if user_names:
            break
        else:
            print('Please enter your name')
    while True:
        emails = input('Enter your email address:')
        if '.' in emails and '@' in emails:
            break
        else:
            print('Please enter a right email')
    while True:
        languages = input('Enter the language that you want to learn')
        if languages:
            break
        else:
            print('Please enter a language')
    return Profile(user_names, emails,languages)

user_info=create_profile()
user_info.display_profile()



#project 3:
import time
print('\n\n\nStarting project number three.....\n\n')
time.sleep(3)
time.sleep(3)
class Product:
    def __init__(self,name,price,quality,rating):
        self.name=name
        self.price=price
        self.quality=quality
        self.rating=rating
    def display_product(self):
        print(f'Name:{self.name}\nPrice: {self.price}\nQuality: {self.quality}\nRating:{self.rating}')

drone=Product('Drone','2000$','high quality','five')
iphone=Product('Iphone','500$','High Quality','fifty')
laptop=Product('lab','600$','high quality','forty')
print(f'{'-'*10}')
drone.display_product()
print(f'\n\n{'-'*10}')
iphone.display_product()
print(f'\n\n{'-'*10}')
laptop.display_product()















