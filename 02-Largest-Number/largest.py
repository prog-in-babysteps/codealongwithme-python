# Find the Largest Number

num_input = int(input("No. of Inputs: "))

num_list = []
for i in range(num_input):
    num = int(input())
    num_list.append(num)

largest_num = num_list[0]
for num in num_list[1:]:
    if num > largest_num:
        largest_num = num

print(f"Largest Number is {largest_num}")
