from time import time


def factorize(*number):
    prime_divisors = []
    for num in number:
        num_lst = []
        for i in range(1, num + 1):
            if num % i == 0:
                num_lst.append(i)
        prime_divisors.append(num_lst)
    return prime_divisors




timer = time()

gep = factorize(128, 255, 675, 99999, 10651060, 15876342, 17999481, 87545321)
for elem in gep:
    print(elem)


print(f'Total time: {round(time() - timer, 4)} sec')
