from typing import List

def main():
    from datetime import datetime
    start = 0
    stop = 100_000

    starttime = datetime.now()
    primelist = findPrimes(start, stop)
    endtime = datetime.now()

    for p in primelist:
        print(p)

    print(f"{len(primelist)} primes found between {start} and {stop}")
    print(f"Took {endtime - starttime} to find primes")

# returns a list of all prime numbers greater than or equal to `start` and less than `stop`
# raises ValueError if `start` is greater than or equal to `stop`
# raises TypeError if either start or stop is a non-integer
def findPrimes(start: int, stop: int) -> List[int]:

    if start >= stop:
        raise ValueError(f"start value {start} is greater than or equal to stop value {stop}")

    if not isinstance(start, int):
        raise TypeError(
            f'findPrimes requires integer values but was passed a(n): {type(start)}')
    if not isinstance(stop, int):
        raise TypeError(
            f'findPrimes requires integer values but was passed a(n): {type(stop)}')

    return [prime for prime in filter(isPrime, range(start, stop))]
        

# returns True if the value provided is a prime number, False if a composite number
# raises TypeError if non-integer is passed
# NOTE: 0 and 1 are considered composite by this function
# NOTE: negative values have their sign removed (this may not be mathematically accurate)
def isPrime(val: int) -> bool:
    from math import sqrt, ceil

    if not isinstance(val, int):
        raise TypeError(
            f'isPrime requires an integer value but was passed a(n): {type(val)}')

    # make value positive by taking absolute value
    val = abs(val)

    # return False if this number is 0 or 1
    if val == 0 or val == 1:
        return False

    # return True if this number is 2
    if val == 2:
        return True

    # try dividing by 2 (test if number is even)
    if val % 2 == 0:
        return False

    # maximum possible factor of some value n is the square root of n
    # any factor larger than this must be paired with a factor smaller than this
    # we round up to the nearest integer
    maxTest = int(ceil(sqrt(val)))

    # iterate through every noneven integer from 3 through maxTest (1 is added to include maxTest)
    # (all even numbers above 2 can be skipped as if val were divisble by an even number it would have to be even itself)
    for candidate in range(3, maxTest + 1, 2):
        # check if val is divisible by each candidate
        if val % candidate == 0:
            # if yes, value is composite
            return False

    # if val isn't divisible by any of the tested candidates, val is prime
    return True

if __name__ == "__main__":
    main()