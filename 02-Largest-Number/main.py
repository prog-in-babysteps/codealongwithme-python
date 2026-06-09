num = int(input())
num_list = []
for i in range(num):
    x = int(input())
    num_list.append(x)

largest_num = num_list[0]
for element in num_list[1:]:
    if element > largest_num:
        largest_num = element

print(f"Largest Number is {largest_num}")
