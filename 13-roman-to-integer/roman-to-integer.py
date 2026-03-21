class Solution:
    def romanToInt(self, s: str) -> int:
        romin=["I","V","X","L","C","D","M"]
        romin_s=["IV","IX","XL","XC","CD","CM",]
        value=[1,5,10,50,100,500,1000]
        value_s=[4,9,40,90,400,900]
        result=0
        check=True
        for i in range(len(s)-1,-1,-1):
            if (s[i-1]+s[i]) in romin_s and i!=0:
                m=romin_s.index(s[i-1]+s[i])
                result+=value_s[m]
                check=False
                continue
            elif check:
                if s[i] in romin:
                    m=romin.index(s[i])
                    result+=value[m]
            else:
                check=True

        return result
            
