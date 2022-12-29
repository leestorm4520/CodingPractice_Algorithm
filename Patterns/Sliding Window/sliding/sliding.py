import math

class SlidingWindow:
    #assign value to object properties when initialized
    def __init__(self, arr, k, max, line):
        self.arr=arr
        self.k=k
        self.max = max
        self.line = line
    def __str__(self):
        return f"{self.arr} - {self.k}"
    def findAverageSubArray(self):
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
    def findSmallestSubArray(self):
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
    def findLongestSubstring(self):
      # left is the start of substring
      # right is the end of substring, being (k-1)th
      # count is the number of distinct substrings in the current substring
      left, right, maxLength, count = 0, 0, 0, 0

       # dictionary to keep track of how often a character shows up in the line
      dict = {}
      for character in self.line:
        dict[character] = 0

      while right < len(self.line):
        dict[self.line[right]]+=1
        if dict[self.line[right]] == 0:
          count+=1
        while count > self.k:
          maxLength = max(maxLength, right - left +1)
          left+=1
          dict[self.line[left]]-=1
          if dict[self.line[left]] == 0 :
            count -=1
        right+=1
      return self.line[left:right]



def main():
    slidingWindow=SlidingWindow([3,45,-5,7,26,63,1,67], 4, 49, "aaravfffberefessss")
    print("Averages of subarrays of size K: " + str(slidingWindow.findAverageSubArray()))
    print("Smallest subarray with a great sum of "+str(slidingWindow.max) + " is " + str(slidingWindow.findSmallestSubArray()))
    print("Longest substring with "+ str(slidingWindow.k)+" distinct character is "+str(slidingWindow.findLongestSubstring()))

main()