'''
r, c = map(int, input("Enter rows and columns: ").split())
matrix = []

print(f"Enter the elements of the {r}x{c} matrix row by row:")

for _ in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(*row)
'''



def read_matrix(n):
  r,c=map(int,input(f"Enter number of rows and columns of matrix {n}: ").split())
  matrix=[]
  print(f"Enter the elements of matrix {n}")
  for i in range (r):
    a=[]
    for j in range (c):
      element=int(input())
      a.append(element)
    matrix.append(a)
  return matrix,r,c
def print_matrix(n,matrix,r,c):
  print(f"Matrix{n}: ")
  for i in range (r):
    for j in range(c):
      print(matrix[i][j],end=' ')
    print()

matrix_1,r1,c1=read_matrix(1)
print_matrix(1,matrix_1,r1,c1)
matrix_2,r2,c2=read_matrix(2)
print_matrix(2,matrix_2,r2,c2)
if r1==r2 and c1==c2:
  print("Result is: ")
  for i in range(r1):
    for j in range(c1):
      print(matrix_1[i][j]+matrix_2[i][j], end=' ')
    print()
else:
  print("Error")