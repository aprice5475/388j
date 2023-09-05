from math import sqrt


def hello_world():
    return "Hello, World!"


def sum_unique(l):
    s = set(l)
    sum = 0
    for x in s:
        sum += x
    return sum


def palindrome(x):
    x = str(x)
    return x == x[::-1]


"""
Finds all multiples from multiple to max_num
"""


def all_multiples(multiple, max_num):
    l = []
    marker = multiple
    i = 2
    while marker < max_num:
        l.append(marker)
        marker = multiple * i
        i += 1
    return l


def sum_multiples(num):
    ans = 0
    mult_3 = all_multiples(3, num)
    m3 = set(mult_3)
    ans += sum(mult_3)
    mult_5 = all_multiples(5, num)
    m5 = set(mult_5).difference(m3)
    ans += sum(list(m5))
    return ans


def num_func_mapper(nums, funs):
    ans = []
    for fun in funs:
        ans.append(fun(nums))
    return ans


def pythagorean_triples(n):
    ans = []
    for a in range(1, n - 1):
        for b in range(a, n):
            c = sqrt(pow(a, 2) + pow(b, 2))
            if c % 1 == 0 and c < n and (int(a), int(b), int(c)) not in ans:
                ans.append((int(a), b, int(c)))
                a = c
                continue
    ans.sort(key=lambda x: x[2])
    return ans


def custom_sort(lst):
    evens = list(filter(lambda x: x % 2 == 0, lst))
    odds = list(filter(lambda x: x % 2 == 1, lst))
    return odds + evens
