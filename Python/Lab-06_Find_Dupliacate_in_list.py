#Write a function to find Duplicate values in the List.
def duplicate(input_list):
	new_dict, new_list = {}, []

	for i in input_list:
		if not i in new_dict:
			new_dict[i] = 1
		else:
			new_dict[i] += 1

	for key, values in new_dict.items():
		if values > 1:
			new_list.append(key)

	return new_list

if __name__ == '__main__':
	input_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]    
	print(duplicate(input_list))

#Python program to print duplicates from
#a list of integers
list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

uniqueList = []
duplicateList = []

for i in list:
	if i not in uniqueList:
		uniqueList.append(i)
	elif i not in duplicateList:
		duplicateList.append(i)

print(duplicateList)

