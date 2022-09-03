'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
'''
def reverseWords(str):
    newStr=""
    words=str.split();
    for word in words:
        newWord=list(word)
        reverse(newWord)
        newStr+=''.join(newWord)+" "
    return newStr

def reverse(word):
    l,r=0, len(word)-1
    while(l<r):
        tmp=word[l]
        word[l]=word[r]
        word[r]=tmp
        l+=1
        r-=1


def main():
    s = "Let's take LeetCode contest"
    print(reverseWords(s))
    from timeit import timeit
    setup = 's = "Let\'s take LeetCode contest"'
    statements = ("' '.join(s.split()[::-1])[::-1]",
	          "' '.join(x[::-1] for x in s.split())",
	          "' '.join([x[::-1] for x in s.split()])")
    for stmt in statements:
        print(' '.join('%.2f' % timeit(stmt, setup) for _ in range(5)), 'seconds for:', stmt)

if __name__=="__main__":
    main()

    #  def reverseWords(self, s: str) -> str:
    #     newStr=""
    #     words=s.split();
    #     for word in words:
    #         newStr+=''.join(list(word[::-1]))+" "
    #     newStr=newStr.strip()
    #     return newStr

    # return ' '.join(s.split()[::-1])[::-1]