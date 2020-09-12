class solution:
    def __init__(self,nums,target):
        self.nums=nums
        self.target=target
    def twoSum(self):
        Mpnum={}
        for i in range(len(self.nums)):
            if self.target-self.nums[i] in Mpnum:
                return(i,Mpnum.get(self.target-self.nums[i]))
            else:
                Mpnum[self.nums[i]]=i
if __name__ == '__main__':
    s1=solution([2,3,5,7],12)
    ans=s1.twoSum()
    print(ans)