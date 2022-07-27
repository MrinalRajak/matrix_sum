

#Determination of matrix sum

a=[]
m=int(input("Enter the number of rows of matrix a: "))
n=int(input("Eneter the number of columns of matrix a: "))
a=[[int(input())for i in range(m)]for j in range(n)]
print("The matrix a: ",a)

p=int(input("Enter the number of rows of matrix b: "))
q=int(input("Enter the number of columns of matrix b: "))
b=[[int(input())for i in range(p)]for j in range(q)]
print("The matrix b: ",b)

c=[[0]*m for i in range(n)]
print("The Null matrix: ",c)

if(m==p and n==q):
    for i in range(m):
        for j in range(n):
            c[i][j]=a[i][j]+b[i][j]
    print("The resultant matrix is: ",c)
else:
    print("matrices are not conformal for addition")
