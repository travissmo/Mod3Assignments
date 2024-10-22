class Solution:
    def __init__(self,arr):
        self.arr = arr
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self):
        self.arr.sort() #sort method to order the numbers 
        return self.arr

if __name__ == "__main__": #had to add a main manually because the driver code on geeks didnt seem to be working correctly

    examples = [
        [0, 2, 1, 2, 0],
        [0, 1, 0],
        [2, 2, 2]
    ]
    
    for arr in examples:
        solution = Solution(arr)
        sorted_solution = solution.sort012()
        print(sorted_solution)