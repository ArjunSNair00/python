r, c = map(int, input("Enter rows and columns: ").split())
matrix = []

print(f"Enter the elements of the {r}x{c} matrix row by row:")

for _ in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(*row)