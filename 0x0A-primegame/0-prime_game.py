#!/usr/bin/python3

def generate_primes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for start in range(2, int(n**0.5) + 1):
        if sieve[start]:
            for i in range(start * start, n + 1, start):
                sieve[i] = False
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = generate_primes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        set_numbers = set(range(1, n + 1))
        maria_turn = True
        while set_numbers:
            prime = next((p for p in primes if p in set_numbers), None)
            if prime is None:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            multiples = set(range(prime, n + 1, prime))
            set_numbers.difference_update(multiples)
            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
