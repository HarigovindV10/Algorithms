class sorting:

    array = []

    def __init__(self, array):
        self.array = array

    def sort(self, algorithm = "bubble"):
        array = []
        
        if(algorithm == "bubble"):
            array = self.bubble_sort()
        elif(algorithm == "insertion"):
            array = self.insertion_sort()
        elif(algorithm == "selection"):
            array = self.selection_sort()
        elif(algorithm == "merge"):
            array = self.merge_sort()

        return array

    def bubble_sort(self):
        array = self.array

        for i in range(0, len(array)):
            for j in range(0, len(array) - 1 - i):
                if (array[j] > array[j + 1]):
                    array[j], array[j + 1] = array[j + 1], array[j]
        
        return array

    def insertion_sort(self):
        pass

    def merge_sort(self):
        pass

    def selection_sort(self):
        pass


array = [2, 3, 1, 7, 0, 9, 8, 10]

obj = sorting(array)

sorted_array = obj.sort("bubble")

print(sorted_array)