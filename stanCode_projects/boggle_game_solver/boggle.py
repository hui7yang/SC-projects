"""
File: boggle.py
----------------------------------------
Author: Hui-Chi Yang
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# global variable
dict = []      # words in dictionary.txt
ans = []       # words acquired after running boggle game
count = 0      # the number of words in boggle game


def main():
	"""
	TODO: Play boggle game! (find valid words in the gird player enter)
	"""
	global count
	read_dictionary()
	lst = []
	for i in range(4):  # run 4 times (0, 1, 2, 3)
		letters = input(str(i+1) + ' row of letters:')
		letter = letters.split()
		# illegal input
		if len(letters) != 7 or letters[1] != ' ' or letters[3] != ' ' or letters[5] != ' ':
			print('Illegal format!')
			break
		lst.append(letter)

	for x in range(4):
		for y in range(4):
			detecting_letter(lst, x, y, lst[x][y], [(x, y)])

	print("There are "+str(count)+" words in the total.")


def detecting_letter(lst, x, y, word, coor_lst):

	if word in dict and len(word) >= 4 and word not in ans:
		print("Found" '\"' + word + '\"')
		global count
		count += 1
		ans.append(word)

	# base case
	if has_prefix(word):
		for i in range(-1, 2):
			if 4 > x+i >= 0:
				for j in range(-1, 2):
					if 4 > y+j >= 0:
						letter_x = x+i
						letter_y = y+j
						coordinate = (letter_x, letter_y)
						# recursive case
						if coordinate in coor_lst:
							pass
						else:
							# choose
							word += lst[letter_x][letter_y]
							coor_lst.append(coordinate)
							# explore
							detecting_letter(lst, letter_x, letter_y, word, coor_lst)
							# un-choose
							word = word[:len(word)-1]
							coor_lst.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dict
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			dict.append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for vocab in dict:
		if vocab.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
