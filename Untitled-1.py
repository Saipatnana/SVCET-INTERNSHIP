def generate_pattern(n):
    num = 1
    for i in range(1, n + 1):
        for i in range(i):
            if i%2 ==1:
                temp = num + i
                print(temp, end=" ")
                
            else:
                print(num, end=" ")
                num += 1
        print()
                


n = int(input())
generate_pattern(n)