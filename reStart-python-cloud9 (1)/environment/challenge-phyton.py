def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_and_save_primes(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]

    with open('results.txt', 'w') as file:
        for prime in primes:
            print(prime)
            file.write(str(prime) + '\n')

if __name__ == "__main__":
    display_and_save_primes(1, 250)