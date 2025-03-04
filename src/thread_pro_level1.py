from concurrent.futures import ThreadPoolExecutor

import logging



def find_dividers(num):
    counter = 0
    for i in range(1,num + 1):
        if num % i == 0:
            counter += 1
    return counter

def myFunc(x):
    min_num, max_num = x
    number = 0
    number_dividers = 0
    for i in range(min_num,max_num):
        num_of_dividers = find_dividers(i)
        if num_of_dividers > number_dividers:
            number = i
            number_dividers = num_of_dividers
    return (number, number_dividers)



def main():
    input_tuple = (40,150)
    results =  myFunc(input_tuple)
    print(results)

if __name__ == '__main__':
    main()