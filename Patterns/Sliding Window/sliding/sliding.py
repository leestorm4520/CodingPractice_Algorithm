import math

class SlidingWindow:
    #assign value to object properties when initialized
    def __init__(self, arr, k, max):
        self.arr=arr
        self.k=k
        self.max = max
    def __str__(self):
        return f"{self.arr} - {self.k}"
    def findAverage(self):
        result = []
        windowSum, windowStart = 0.0, 0
        for windowEnd in range(len(self.arr)):
            windowSum += self.arr[windowEnd]  # add the next element
            # slide the window, no need to slide if we've not hit the required window size of 'k'
            if windowEnd >= self.k - 1:
                result.append(windowSum / self.k)  # calculate the average
                windowSum -= self.arr[windowStart]  # subtract the element going out
                windowStart += 1  # slide the window ahead
        return result
    # find smallest subarray with a greater sum
    def findSmallest(self):
        windowSum, windowStart, minLength = 0, 0, math.inf
        for windowEnd in range(len(self.arr)):
            windowSum += self.arr[windowEnd] # add the next element
            if windowSum >= self.max:
                minLength = min(minLength, windowEnd - windowStart + 1)
                windowSum -= self.arr[windowStart]
                windowStart +=1
        if minLength == math.inf:
            return []
        return self.arr[windowStart:windowEnd]

def main():
    slidingWindow=SlidingWindow([3,45,-5,7,26,63,1,67], 4, 49)
    result = slidingWindow.findAverage()
    print("Averages of subarrays of size K: " + str(result))
    print("Smallest subarray with a great sum of "+str(slidingWindow.max) + " is " + str(slidingWindow.findSmallest()))


main()