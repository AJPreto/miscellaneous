#!/usr/bin/env python

"""
The rule to the sequence:
1
11
21
1211
111221
...
"""

__author__ = "A.J. Preto"
__email__ = "martinsgomes.jose@gmail.com"

def generate_new_number(input_old_number):

	single_holder = ""
	open_dict = {}
	block_count = 0
	block_keys = []
	for char in str(input_old_number):
		if char == single_holder:
			open_dict[current_block][1] += 1
		if char != single_holder:
			current_block = "block_" + str(block_count)
			open_dict[current_block] = [char, 1]
			block_count += 1
			block_keys.append(current_block)
		single_holder = char
	output_string = ""
	for values in block_keys:
		output_string = output_string + str(open_dict[values][1]) + str(open_dict[values][0])
	return output_string

def apply_on_range(target_range, input_number = 1):

	for number in range(1,target_range):
		current_number = generate_new_number(input_number)
		input_number = current_number
		print(input_number)
		print(len(str(input_number)))

"""
Call apply on range to find the nearest values
"""
#apply_on_range(30)