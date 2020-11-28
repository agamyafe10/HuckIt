from flask import Flask, render_template, url_for, request
import time
import random
#create flask object with file name
app = Flask(__name__)

#route index page to root of web site

@app.route('/<string:given_pass>', methods = ['GET', 'POST'])
def index(given_pass="agam"):
    if given_pass == "":
        return render_template('index.html')
    if verify(given_pass):
        return '1'
    else:
        return '0'

def verify(given_password):
    # pre
    POOL = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n1 = random.randint(0,1)
    len_delay_values = [11, 6, 8, 14, 18]
    char_delay_values= '0123456789bcdefgijknopqrstDEFGHIJKLMNOPQRS'
    # while(len(char_delay_values) < 20) 
    #     rnd = random.randint(0,61)
    #     if POOL[rnd] not in char_delay_values:
    #         char_delay_values.append(POOL[rnd])
    
    secret_password = "lmao"
    result = True
    edited_given_password = "".ljust(24-len(given_password),' ') + given_password# filling 24 space with the password
    edited_secret_password = "".ljust(24-len(secret_password),' ') + secret_password
    rnd = random.randint(1, 10)
    for index in range(24):
        if edited_secret_password[index] != edited_given_password[index]:
            
            time.sleep(0.06)
            result = False
    
        # rnd = random.randint(0,2)
        # if len(given_password) == len(secret_password) and edited_given_password[index] in char_delay_values and rnd == 1:
        #     time.sleep(0.03)
    # for the values in the arr the time rises
    if  len(given_password) in len_delay_values:
        time.sleep(0.12)
    # a chance of 0.3 per each pass check that the time rises
    if len(given_password) == len(secret_password):
        if rnd < 4:
            time.sleep(0.05)
    return result
#This code run when this file is call but not when it imported by other file
if __name__== "__main__":
    #start running the web page
    app.run(debug=True)
