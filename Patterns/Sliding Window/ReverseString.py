'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
'''
def reverseString(s):
    l,r=0,len(s)-1
    while(l<r):
        reverse(s,l,r)
        l+=1
        r-=1
    return s

def reverse(s, i, k):
    tmp=s[i]
    s[i]=s[k]
    s[k]=tmp

def main():
    s = ["h","e","l","l","o"]
    print(reverseString(s))
if __name__=="__main__":
    main()