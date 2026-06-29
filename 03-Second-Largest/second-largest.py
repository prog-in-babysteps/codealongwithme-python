# Find the SecondLargest Number
num_input = int(input("No. of Inputs: "))

num_list = []
for i in range(num_input):
    num = int(input())
    num_list.append(num)

if num_list[0] > num_list[1]:
    largest_num = num_list[0]
    second_largest_num = num_list[1]
else:
    largest_num = num_list[1]
    second_largest_num = num_list[0]

for num in num_list[2:]:
    # >= consume duplicate largest number if any
    if num >= largest_num:
        second_largest_num = largest_num
        largest_num = num
    elif num > second_largest_num:
        second_largest_num = num

print(f"Largest Number is {largest_num}")
print(f"Second Largest Number is {second_largest_num}")
