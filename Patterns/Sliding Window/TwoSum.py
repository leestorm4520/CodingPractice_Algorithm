def twoSum(self, nums, target):
    l, r=0, len(nums)-1
    while(nums[l]+nums[r]!=target):
        if(nums[l]+nums[r]>target):
            r-=1
        else:
            l+=1
    return [l+1, r+1]

def main():
   nums=[2,7,11,14]
   target=9
   print(twoSum(0, nums,target)) 

if __name__=="__main__":
    main()