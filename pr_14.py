import csv
from typing impimport csv
from typing import Iterable, Callable
# 10 вариант

def fil(it: Iterable, predicate: Callable[[any], bool]) -> Iterable:
    return [i for i in it if predicate(i)]

def count(it: Iterable) -> int:
    count = 0
    return [count := count + 1 for _ in it][-1]

with open('StudentsPerformance 14.csv', 'r') as f:
    reader = csv.DictReader(f)
    students = [s for s in reader]
    coursed_males = fil(students, lambda s: s['gender'] == 'male' and s['lunch'] == 'standard')
    print(count(coursed_males))
    pass

import csv
from typing import Iterable, Callable

def fil(it: Iterable, predicate: Callable[[any], bool]) -> Iterable:
    return [i for i in it if predicate(i)]

def count(it: Iterable) -> int:
    count = 0
    return [count := count + 1 for _ in it][-1]

with open('StudentsPerformance 14.csv', 'r') as f:
    reader = csv.DictReader(f)
    students = [s for s in reader]
    coursed_males = fil(students, lambda s: s['gender'] == 'female' and s['good lunch'] == 'standard')
    print(count(coursed_males))
    pass