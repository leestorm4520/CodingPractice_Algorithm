import math

# Set a time limit for each question (40-45 minutes)

# At the start of each question, read it out loud as you would in an interview and ask any clarifying questions (even though there is no interviewer there)

# Talk through the problem and figure out the approach you will use (state brute force and then discuss how to optimize. write down how your algorithm will work)

# Once you've figured out your approach, then write out the code, talking through what each part of your code is doing

# After you've written out the code, review it for bugs and go through test cases if you have time



class SlidingWindow:
    #assign value to object properties when initialized
    def __init__(self, arr, k, max, line, binary):
        self.arr=arr
        self.k=k
        self.max = max
        self.line = line
        self.binary = binary
    def __str__(self):
        return f"{self.arr} - {self.k}"
    def findAverageSubArray(self):
        result = []
        windowSum, windowStart = 0.0, 0
        for windowEnd in range(len(self.arr)):
            windowSum += self.arr[windowEnd]  # add the next element
            # slide the window, no need to slide if we've not hit the required window size of 'k'
            if windowEnd >= self.k - 1:
                result.append(round(windowSum / self.k, 2))  # calculate the average
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

    # time complexity: O(N+N) (N is the number of characters in the input string)
    def findLongestSubstringWithKDistinctChar(self):
      # left is the start of substring
      # right is the end of substring, being (k-1)th
      # count is the number of distinct substrings in the current substring
      left, right, maxLength = 0, 0, 0
      left_final = 0

       # dictionary to keep track of how often a character shows up in the line
      dict = {}

      for right in range(len(self.line)):
        rightChar = self.line[right]
        if rightChar not in dict:
          dict[rightChar] = 0
        dict[rightChar] +=1
        while len(dict) > self.k:
          leftChar = self.line[left]
          dict[leftChar] -=1
          if dict[leftChar] == 0:
            del dict[leftChar]
          left += 1
        if maxLength <= right - left + 1:
          maxLength = right - left +1
          left_final = left
      return self.line[left_final:left_final+maxLength] # behave like a range() so [start to end -1 th]

      # add one character to the window (slide the window ahead)
      # shrink the window from the beginning if count > k
      # while shrinking, decrement the character's frequency going out of window
      # and the count if the character's frequency is 1 (unique in the substring)

      # while right < len(self.line):
      #   if dict[self.line[right]] == 0:
      #     count+=1
      #   dict[self.line[right]]+=1
      #   while count > self.k:
      #     # maxLength = max(maxLength, right - left +1)
      #     if maxLength <= right - left +1:
      #         maxLength = right - left+ 1
      #         left_final = left
      #     if dict[self.line[left]] == 1:
      #       count -=1
      #     dict[self.line[left]]-=1
      #     left+=1
      #   right+=1
      # return self.line[left_final:left_final+maxLength-1]

    def fruitIntoBaskets(self):
      charList = list()
      charList.extend(self.line)
      left, right, maxLength = 0, 0, 0
      dict = {}

      # try to extend the range [left, right]
      for right in range(len(charList)):
        rightChar = charList[right]
        if rightChar not in dict:
          dict[rightChar] = 0
        dict[rightChar] +=1

        # shrink the sliding window, until we are left with 2 distinct characters
        while len(dict) > 2:
          leftChar = charList[left]
          dict[leftChar] -= 1
          if dict[leftChar] == 0:
            del dict[leftChar]
          left +=1
        maxLength = max(maxLength, right - left + 1)
      return maxLength
      # while right < len(charList):
      #   if dict[charList[right]] == 0:
      #     count+=1
      #   dict[charList[right]]+=1
      #   print(maxLength)
      #   while count >= self.k:
      #     maxLength = max(maxLength, right - left +1)
      #     if dict[charList[left]] == 1 and count > self.k:
      #       count -=1
      #       dict[charList[left]]-=1
      #       left+=1
      #   right+=1
      # return maxLength
    def findLongestSubstringWithDistinctChar(self):
      left, right, maxLength = 0, 0, 0

       # dictionary to keep track of characters and their position in the string
      dict = {}

      for right in range(len(self.line)):
        rightChar = self.line[right]
        # if the dict already has the right char, shrink the window from the beginning
        # so that we have only one occurence of right char
        if rightChar in dict:
          # in the current window, we will not have any right char after its previous index
          # if "left" is already head of the last index of right char, we'll keep "left"
          left = max(left, dict[rightChar] + 1)
        # insert the right char into the map
        dict[rightChar] = right
        maxLength = max(maxLength, right - left +1)
      return maxLength

      # for right in range(len(self.line)):
      #   rightChar = self.line[right]
      #   if rightChar not in dict:
      #     dict[rightChar] = 0
      #   dict[rightChar] +=1 Z
      #   while dict[rightChar] > 1:
      #     leftChar = self.line[left]
      #     dict[leftChar] -=1
      #     if dict[leftChar] == 0:
      #       del dict[leftChar]
      #     left += 1
      #   maxLength = max(maxLength, right - left +1)
      # return maxLength
    def findLongestSubstringWithSameLettersAfterReplacement(self):
      left, right, maxLength, maxRepeatLetterCount = 0, 0, 0, 0
      frequencyMap={} # key: letter, value: its count in the current window

      for right in range(len(self.line)):
        rightChar=self.line[right]
        if rightChar not in frequencyMap:
          frequencyMap[rightChar]=0
        # add count to the letter
        frequencyMap[rightChar]+=1
        maxRepeatLetterCount = max(maxRepeatLetterCount, frequencyMap[rightChar])
        # find the length of remaining letters from the max repeated letter
        # if the length is less than k, replace them all
        # if not, shrink the window by decreasing leftChar freq and increment left
        if ((right-left+1) - maxRepeatLetterCount) > self.k:
          leftChar = self.line[left]
          frequencyMap[leftChar] -=1
          left +=1
        maxLength = max(maxLength, right - left + 1)

      return maxLength

    def findLongestSubarrayWithOnesAfterReplacement(self):
      right, left, max1s, maxLength = 0,0,0,0
      # frequency_map = {}
      # for right in range(len(self.binary)):
      #   rightNum = self.binary[right]
      #   if rightNum not in frequency_map:
      #     frequency_map[rightNum] = 0
      #   frequency_map[rightNum] +=1
      #   if rightNum == 1:
      #     max1s = max(max1s, frequency_map[rightNum])
      #   if((right-left+1) - max1s) > self.k:
      #     leftNum = self.binary[left]
      #     frequency_map[leftNum] -=1
      #     left +=1
      #   maxLength = max(maxLength, right - left +1)

      for right in range(len(self.binary)):
        if self.binary[right] == 1:
          max1s +=1

        # Current window is from left to right
        # we have a max of 1s repeating, which means we can have a window with max_ones_counts 1s
        # and the remaining are 0s which should be replaced with 1s
        # If the remaining 0s are more than 'k', it is the time to shrink the window as
        # we are not allowed to replace more than 'k' 0s
        if ((right - left +1) - max1s) > self.k:
          if self.binary[left] == 1:
            max1s -=1
          left +=1
        maxLength = max(maxLength, right - left +1)

      return maxLength



def main():
    slidingWindow=SlidingWindow([3,45,-5,7,26,63,1,67], 2, 49, "aabccbb", [0,1,1,0,0,0,1,1,0,1,1])
    print("Averages of subarrays of size K: " + str(slidingWindow.findAverageSubArray()))
    print("Smallest subarray with a great sum of "+str(slidingWindow.max) + " is " + str(slidingWindow.findSmallestSubArray()))
    print("Longest substring with "+ str(slidingWindow.k)+" distinct character is "+str(slidingWindow.findLongestSubstringWithKDistinctChar()))
    print("Max fruits into 2 baskets are "+ str(slidingWindow.fruitIntoBaskets()))
    print("Longest Substring with Distinct Characters is " + str(slidingWindow.findLongestSubstringWithDistinctChar()))
    print("Longest Substring with Same Letters after Replacement is " + str(slidingWindow.findLongestSubstringWithSameLettersAfterReplacement()))
    print("Longest subarray with ones after replacement: " + str(slidingWindow.findLongestSubarrayWithOnesAfterReplacement()))
main()