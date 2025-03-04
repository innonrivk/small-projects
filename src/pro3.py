


def is_prime(num):
    for i in range(2,num // 2):
        if num % i == 0:
            return False
    return True


def factors(x):
    # We will store all factors in `result`
    result = []
    i = 1
    # This will loop from 1 to int(sqrt(x))
    while i*i <= x:
        # Check if i divides x without leaving a remainder
        if x % i == 0:
            result.append(i)
            # Handle the case explained in the 4th
            if x//i != i: # In Python, // operator performs integer/floored division
                result.append(x//i)
        i += 1
    # Return the list of factors of x
    return result

def large_factor(x):
    l = 1
    for i in x:
        if is_prime(i):
            if i > l:
                l = i
    return l

def main():

    number = input("put num")
    print(large_factor(factors(int(number))))

if __name__ == '__main__':
    main()