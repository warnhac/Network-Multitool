import os

def userInput():
    user_input = raw_input("Please enter URL. Please do not include http://: ")
    os.system("scrapy runspider -a user_input='http://" + user_input + "' crawler_prod.py")

userInput()