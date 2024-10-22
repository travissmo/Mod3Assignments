#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        low = 0
        high = len(arr) - 1
        while low <= high: #uses while loop to keep searching until an answer is found
            mid = (low + high) // 2 
            if arr[mid] == k: #if k is the middle number on the first search this will output it
                return mid
            elif arr[mid] < k: #if the middle number is less than k this adds 1 to mid and searches again
                low = mid+1
            else:
                high = mid - 1 #if middle number is higher than k this subtracts 1 and searches again
        return -1 #if k is not in array then -1 is returned 

# End of my code
#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)

# } Driver Code Ends