# A program to find Euler Primes[0] and determine the prime percentage[1]
#
# [0] - https://mathworld.wolfram.com/EulerPrime.html
# [1] - https://www.codebymath.com/index.php/welcome/challenge/euler-prime

print(
    f"Euler's Prime Generating Polynomial: {(euler := {e**2 + e + 41 for e in range(101)})}",
    f'Euler Primes: {(primes := {
        p
        for p in euler
        if p > 1 and all(
            p % i
            for i in range(2, int(p**.5 - 1))
        )
    })}',
    f'Non-Primes: {str(euler-primes):1}',
    f'Prime Percentage: {len(primes) / len(euler):%}',
    sep='\n\n'
)
