def num_digits(number):
	return len(str(number))

def most_digits(lcl_list):
	lcl_list = sorted(lcl_list, key=num_digits)
	return lcl_list[-1]

def largest_two_digit_even(lcl_list):
	lcl_lar = 0
	for number in lcl_list:
		if number%2 == 0 and len(str(number)) == 2:
			if number>lcl_lar:
				lcl_lar = number
	return lcl_lar
	
def num_ones_in_binary(number):
	bin_num = bin(number)
	bin_num = bin_num[2:]
	count = 0
	for digit in bin_num:
		if digit == "1":
			count += 1
	return count

def most_ones_in_binary(lcl_list):
	lcl_list = sorted(lcl_list, key = num_ones_in_binary)
	return lcl_list[-1]


def best(lcl_list, fun_name):
	return fun_name(lcl_list)

def main():
	lcl_list = [1,76,84,95,214,1023,511,32]
	print best(lcl_list,min)
	print best(lcl_list,largest_two_digit_even)
	print best(lcl_list,most_digits)
	print best(lcl_list,most_ones_in_binary)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
