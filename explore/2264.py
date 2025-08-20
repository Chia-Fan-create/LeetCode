class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num = list(num)
        test = []
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                test.append(int(num[i])*111)
        if len(test) == 0:
            num = ""
        elif max(test) == 0:
            num = "000"
        else:
            num = str(max(test))
        return num
    
    
    # what I learned today:

    # string manipulation
    # Example: 
    # n = ["1", "2", "3"]
    # n[0]+n[1]+n[2] = "123"
    # m = ["4", "5", "6"]
    # m[0]+m[1]+m[2] = "456"