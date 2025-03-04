from concurrent.futures import ThreadPoolExecutor
from operator import itemgetter
import logging

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")

console_handler.setFormatter(FORMATTER)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)

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
    logger.debug(f"{tuple(x)}  - winner number {(number,number_dividers)}")
    return (number, number_dividers)



def main():
    range_lst = [(40000, 60000),(5000,10000),(7000 , 14000),(20000, 28000),(15000, 30000)]
    with ThreadPoolExecutor(max_workers=3) as worker:
        results =  worker.map(myFunc, range_lst)
    # itemgetter is used to get the max value from the second place of the tuple
    logger.debug(f"the max from all result {max(list(results),key = itemgetter(1))}")

if __name__ == '__main__':
    main()