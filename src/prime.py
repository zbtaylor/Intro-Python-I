import sys

num = int(sys.argv[1])


def is_prime(n):
    for i in range(2, n//2):
        if (n % i) == 0:
            return False
    return True


if is_prime(num):
    print(f'{num} is prime!')
else:
    print(f'{num} is not prime.')
