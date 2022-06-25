from template import UtilityTemplate

class BinarySearch(UtilityTemplate):
    def logic_function(self):
        return 1, 2

    def test_function(self):
        return 1


if __name__ == "__main__":
    object = BinarySearch("One", "Binary Search")
    object.stockyard(2)
    object.dumpyard()
    object.showtime(object.logic_function, object.test_function)
    print(object.inputList)
