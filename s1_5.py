def checkEven(n):
    if n%2==0:
        return "YES";
    else:
        return "NO";



if __name__ == "__main__":
    n,a,b=map(int, input().split())
    if checkEven(n) == "NO":
        print("NO")
    else:
        par=n/2
        left=par%a
        if (left==0 or left%b==0):
            print("YES")
        else:
            print("NO")
        
        
#This code is by Monesh Venkul
