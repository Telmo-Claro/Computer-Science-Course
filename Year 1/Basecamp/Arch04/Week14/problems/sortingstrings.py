import time


def timeit(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time() - start_time
        print(end_time)
    return wrapper


def get_num_of_vowels(inp):
    vowel_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in inp:
        if letter in vowels:
            vowel_count += 1
    # todo: implement the body of the function
    return int(vowel_count)


@timeit
def sort_basedon_vowels():
    cases = ['code', 'programming', 'description', 'fly', 'free']
    print(sorted(cases, key=get_num_of_vowels))


if __name__ == "__main__":
    sort_basedon_vowels()
