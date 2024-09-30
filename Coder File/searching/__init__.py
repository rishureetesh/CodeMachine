from time import time
from typing import Union


def get_time() -> float:
    return time()


class Searching:
    def __init__(self):
        self.end_time = None
        self.start_time = None

    def set_start_time(self) -> None:
        self.start_time = get_time()
        print(f"Started at : {self.start_time}")

    def get_execution_time(self):
        self.end_time = get_time()
        print(f"Completed at : {self.start_time}")
        print(f"Execution time : {self.end_time - self.start_time}ms")

    def binary(self, data: list, element: Union[float, int], index: bool = False) -> Union[int, bool]:
        """
        Takes list and check for element if present

        :param element:
        :param index:
        :param data: list
        :return: bool
        """
        self.set_start_time()
        low = 0
        high = len(data) - 1
        key_index = low
        found = False
        while low < high:
            mid = int((low + high) / 2) + 1
            if data[mid] == element:
                found = True
                key_index = mid
                break
            elif data[mid] > element:
                high = mid - 1
            else:
                low = mid + 1
        self.get_execution_time()
        if index:
            return key_index if found else -1
        return found

    def linear(self, data: list, element: Union[float, int], index: bool = False) -> Union[int, bool]:
        """
        Takes list and check for element if present

        :param element:
        :param index:
        :param data: list
        :return: bool
        """
        self.set_start_time()
        found: bool = False
        ele_index = 0
        for key_index in range(0, len(data)):
            if data[key_index] == element:
                found = True
                ele_index = key_index
                break
        self.get_execution_time()
        if index:
            return ele_index if found else -1
        return found


searching = Searching()
output = searching.linear([3, 8, 4, 0, 2, 5, 1, 7, 9], 7, True)
print(output)
output = searching.binary([1, 2, 3, 4, 5, 6, 7, 8, 9], 0)
print(output)
