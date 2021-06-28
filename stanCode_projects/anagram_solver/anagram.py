"""
File: anagram.py
Name: Hui-Chi Yang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
# Global variables
dict = []                     # Word in dictionary.txt
lst = []


def main():
    print("Welcome to stanCode \"Anagram Generator \" (or -1 to quit)")
    read_dictionary()

    while True:
        s = input("Find anagram for: ")
        if s == EXIT:
            break
        else:
            print("Searching...")
            find_anagrams(s)
            print("------------------------------------------------------------------------------------------------------------------------------------")


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            dict.append(word)


def find_anagrams(s):
    """
    :param s: find s's anagram
    :return lst: anagram that is in dictionary.txt
    """
    global lst
    helper(s, '', [])
    print(f'{len(lst)} anagram: {lst}')
    lst = []


def helper(s, current, index):

    if len(s) == len(current) and current not in lst:
        if current in dict:
            print("Found: " + current)
            print('Searching...')
            lst.append(current)

    else:
        for i in range(len(s)):
            if i not in index:
                # choose
                current += s[i]
                index.append(i)
                # print(current)
                # explore
                if has_prefix(current) is True:
                    helper(s, current, index)
                # un-choose
                current = current[0:len(current)-1]
                index.pop()


def has_prefix(sub_s):
    """
    :param sub_s: a sub string in s
    :return: True or False. test if prefix is in the dictionary
    """
    for word in dict:
        word.startswith(sub_s)
        return True
    return False


if __name__ == '__main__':
    main()
