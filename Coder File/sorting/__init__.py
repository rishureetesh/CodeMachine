from time import time


def get_time() -> float:
    return time()


class Sorting:
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

    def bubble(self, data: list, enhanced: bool = True) -> list:
        """
        Takes unsorted list and sort it in ascending order, pass enhanced False only when you want to degrade the performance

        :param data: list
        :param enhanced: bool
        :return: list
        """
        self.set_start_time()
        for index in range(0, len(data)):
            sorted_data: bool = True
            for another_index in range(0, len(data) - index - 1):
                if data[another_index] > data[another_index + 1]:
                    data[another_index], data[another_index+1] = data[another_index+1], data[another_index]
                    sorted_data = False
            if enhanced and sorted_data:
                print(f"Enhanced after {index} iteration of {len(data)} length data!")
                break
        self.get_execution_time()
        return data

    def insertion(self, data: list) -> list:
        """
        Takes unsorted list and sort it in ascending order

        :param data: list
        :return: list
        """
        self.set_start_time()
        for index in range(2, len(data)):
            key = data[index]
            another_index = index
            while another_index > 0 and key < data[another_index-1]:
                data[another_index] = data[another_index-1]
                another_index -= 1
            data[another_index] = key
        self.get_execution_time()
        return data

    def selection(self, data: list) -> list:
        self.set_start_time()
        for index in range(0, len(data)-1):
            key_index = index
            for another_index in range(index + 1, len(data)):
                if data[another_index] < data[key_index]:
                    key_index = another_index
            if key_index != index:
                data[index], data[key_index] = data[key_index], data[index]
        self.get_execution_time()
        return data

    def merge(self, data: list) -> list:
        self.set_start_time()
        self.get_execution_time()
        return data


sort_it = Sorting()
data_output = sort_it.insertion([2, 6, 4, 8, 1, 9, 5, 2, 6, 4, 8, 1, 9, 5, 2, 6, 4, 8, 1, 9, 5])
print(data_output)
