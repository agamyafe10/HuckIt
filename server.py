from flask import Flask, render_template, url_for, request
import time
import random
#create flask object with file name
app = Flask(__name__)

#route index page to root of web site

@app.route('/<string:given_pass>', methods = ['GET', 'POST'])
def index(given_pass=""):
    if given_pass == "":
        return render_template('index.html')
    if verify(given_pass):
        return '1'
    else:
        return '0'

def verify(given_password):
    
    len_delay_values = [11, 6, 8, 14, 4]
    secret_password = "blitz"
    result = True
    edited_given_password = "".ljust(24-len(given_password),' ') + given_password# filling 24 space with the password
    edited_secret_password = "".ljust(24-len(secret_password),' ') + secret_password
    
    for index in range(24):
        if edited_secret_password[index] != edited_given_password[index]:
            time.sleep(0.06)
            result = False
    # making the letter checks more difficult
    rnd = random.randint(1, 100)
    # gives a delay to a given password by a chance of approximitly 50% (0.94*10)' which make it  harder to find ther right letter
    if edited_given_password[19] != 'b':
        if rnd < 95:
            time.sleep(0.06)   
    # pre-selected number which meant to make the password's length check more difficult     
    if len(given_password) in len_delay_values:
            time.sleep(0.08) 
    return result


#This code run when this file is call but not when it imported by other file
if __name__== "__main__":
    #start running the web page
    app.run(debug=True)
