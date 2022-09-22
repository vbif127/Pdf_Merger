import random
import os
import shutil

from __init__ import Sorter_Files

def not_and_a_b(a: list, b: list) -> None:
    return list(filter(lambda it: not it[0] == it[1], zip(a, b)))

shuffle = lambda *array: sorted( [*array], key=lambda k: random.random())

sorter = Sorter_Files()
path = "C:\\Users\\mihac\\OneDrive\\Рабочий стол\\Новая папка (11)\\Изображения\\"
for i2 in range(1, 11):
    for i in range(1, 11):
        if not os.path.exists(f"{path}test"):
            os.makedirs(f"{path}test")
        if not os.path.exists(f"{path}test\\{i2}-{i}.jpg"):
            shutil.copyfile(f"{path}1.jpg", f"{path}test\\{i2}-{i}.jpg")
        # shutil.move(f"{path}{i}.jpg")
        # shutil.copyfile()
    
# print(sorter.sort(["/1.jpg", "/1-1.jpg"]))
# assert sorter.sort(["1.jpg", "1-1.jpg"]) == ["1.jpg", "1-1.jpg"]
# assert sorter.sort(shuffle("/1.jpg", "/1-1.jpg", "/2.jpg")) == ["//1.jpg", "//1-1.jpg", "//2.jpg"]
# assert sorter.sort(shuffle("/1.jpg", "/2.jpg", "/3.jpg", "/10.jpg", "/10-2.jpg")) == ["/1.jpg", "/2.jpg", "/3.jpg", "/10.jpg", "/10-2.jpg"]

assert list(map(os.path.basename,
                sorter.sort(shuffle(f"{path}1.jpg",*[f"{path}1-{i}.jpg" for i in range(1, 101)], f"{path}2.jpg"))))\
        ==\
        list(map(os.path.basename,
                [f"{path}1.jpg",*[f"{path}1-{i}.jpg" for i in range(1, 101)], f"{path}2.jpg"]))
array = list(map(lambda it: f"{path}test\\{it}", os.listdir(f"{path}test")))
name_array = lambda array_: list(map(os.path.basename, array_))
# print(name_array(array), [f"{i}.jpg" for i in range(1, 21)])
assert name_array(sorter.sort(shuffle(*array))) == [f"{i}.jpg" for i in range(1, 21)]

print("Все тесты пройдены!!")