from time import time
from multiprocessing import Pool, cpu_count


def factorize(*numbers):
    result = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        result.append(factors)
    return result


def factorize_parallel(*numbers):
    pool = Pool(cpu_count())
    results = pool.map(factorize_single, numbers)
    pool.close()
    pool.join()
    return results


def factorize_single(number):
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return result


if __name__ == "__main__":
    start_time = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(f"Done by {round(time() - start_time, 4)} seconds")
    print(a)
    print(b)
    print(c)
    print(d)

    start_time = time()
    a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)
    print(f"Done by {round(time() - start_time, 4)} seconds")
    print(a)
    print(b)
    print(c)
    print(d)

    with Pool(cpu_count()) as pool:
        start_time = time()
        a, b, c, d = pool.map(factorize, (128, 255, 99999, 10651060))
        pool.close()
        pool.join()
        print(f"Done by {round(time() - start_time, 4)} seconds")
        print(a)
        print(b)
        print(c)
        print(d)