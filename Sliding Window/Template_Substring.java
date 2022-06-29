/*
 * Use two pointers, start and end to represent a window
 * Move end to find a valid window
 * When a valid window is found, move start to find a smaller window
 */

 import java.util.*;
 class Template_Substring{
     //Minimum Window
    public String minWindow(String s, String t){
        int[] map=new int[128];
        for(char c:t.toCharArray()) map[c]++; //create a dictionary using array to reduce space complexity
        int start=0, end=0, minStart=0, minLen=Integer.MAX_VALUE, counter=t.length();
        while(end< s.length()){
            final char c1=s.charAt(end);
            if(map[c1]>0) counter--;
            map[c1]--;
            end++;
            while(counter==0){
                if(minLen>end-start){
                    minLen=end-start;
                    minStart=start;
                }
                final char c2=s.charAt(start);
                map[c2]++;
                if(map[c2]>0) counter++;
                start++;
            }
        }
        return minLen==Integer.MAX_VALUE ? "": s.substring(minStart, minStart+minLen);
     }
     
     //Longest substring - at most K distinct characters
     public int lengthOfLongestSubstringKDistinct(String s, int k) {
        int[] map = new int[256];
        int start = 0, end = 0, maxLen = Integer.MIN_VALUE, counter = 0;
    
        while (end < s.length()) {
          final char c1 = s.charAt(end);
          if (map[c1] == 0) counter++;
          map[c1]++;
          end++;
    
          while (counter > k) {
            final char c2 = s.charAt(start);
            if (map[c2] == 1) counter--;
            map[c2]--;
            start++;
          }
    
          maxLen = Math.max(maxLen, end - start);
        }
    
        return maxLen;
       }

       //Longest Substring - without repeating character
       public int longestSubstring(String s){
        int[] map=new int[128];
        int start=0, end=0, maxLen=0, counter=0;
        while(end<s.length()){
            final char c1=s.charAt(end);
            if(map[c1]>0) counter++;
            map[c1]++;
            end++;
            while(counter>0){
                final char c2=s.charAt(start);
                if(map[c2]>1) counter--;
                map[c2]--;
                start++;
            }
            maxLen=Math.max(maxLen, end-start);
        }
        return maxLen;
       }
 }
 