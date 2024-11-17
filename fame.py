a=int(input('The no.of rows'))
b=1
print("Floyd's Triangle")
for i in range(1, a + 1):
    for j in range(1, i+1):
        print(b, end=' ')
        b=b+1
    print()