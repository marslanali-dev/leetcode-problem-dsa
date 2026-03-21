class Solution:
    def intToRoman(self, num: int) -> str:
        dic1={
            1 :"I" ,5:	"V",10:	"X",50:	"L",100:"C",500:"D",1000:"M",}
        dic2={
            4 :"IV", 9 :"IX",40 :"XL", 90 :"XC", 400:"CD" ,900 :"CM"}
        lis1=[1,5,10,50,100,500,1000]
        str1=str(num)
        str2=""
        str3=""
        count=1
        for i in str1[::-1]:
            m =int(i)*count
            if m in dic2:
                str2=dic2[m]+str2
                count*=10
                continue
            elif m in dic1:
                str2=dic1[m]+str2
                count*=10
                continue
            elif m not in dic1 and m not in dic2:
                for j in lis1[::-1]:
                    while m>=j:
                        m=m-j
                        str3=str3+dic1[j]
                str2=str3+str2
                count*=10
                str3=""
        return str2    

            
