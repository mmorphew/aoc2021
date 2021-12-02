import numpy as np

input_data = np.genfromtxt("day_1_input.txt")
print(input_data)

increased = [1.0 if input_data[i+1] > input_data[i] else 0.0 for i in range(len(input_data)-1)]

print(np.sum(increased))

increased_part_2 = 0
for i in range(len(input_data)-3):
    past_sliding_sum = input_data[i] + input_data[i+1] + input_data[i+2]
    current_sliding_sum = input_data[i+1] + input_data[i+2] + input_data[i+3]
    if current_sliding_sum > past_sliding_sum:
        increased_part_2 += 1

print(increased_part_2)