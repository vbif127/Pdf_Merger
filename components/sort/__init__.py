import os
import re

from collections import defaultdict
from abc import ABC


class Sorter(ABC):
    def sort(self, array: list) -> list: ...

class Sorter_Files(Sorter):
    def sort(self, array: list) -> list:
        res = []
        res_dict1: defaultdict[int, list[str]] = defaultdict(list, {})
        # print(array)
        for path, name in zip(map(os.path.dirname, array), map(os.path.basename, array)):
            name: str
            colum = int(re.search(r"\d{1,5}", name).group(0))
            row = re.search(r"\d{1,5}(.\d{1,5}|)", name).group(0)
            row = int("".join(re.split(r"-", row)))
            res_dict1[colum].append([f'{path}/{name}', row])
        for v in sorted(res_dict1):
            for v2 in sorted(res_dict1[v], key=lambda i: i[1]):
                res.append(v2[0])
    
        # print(res)
        return res