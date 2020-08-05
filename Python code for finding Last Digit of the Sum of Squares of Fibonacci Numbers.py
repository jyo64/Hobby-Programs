l = [0,1,1,4,9,5,4,9,1,6,5,1,6,9,9,0,9,9,6,1,5,6,1,9,4,5,9,4,1,1]
n = int(input())
sumval = 140
if (n%30) == 0 :
    res = 0
elif ( n < len(l) ):
    res = sum(l[:n+1]) % 10
else :
    modi =  ( n % 30 )
    mul = (n - modi) / 30
    starter = sumval * mul
    rest = sum(l[:modi+1])
    res = int(rest  +  starter) % 10
print(res)
