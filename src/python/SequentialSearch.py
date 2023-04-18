# SequentialSearch.py - searches for an element in a list and returns the key if found and -1 if not found


def sequentialSearch(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return i
    return -1

def reverseSequentialSearch(list, element):
    for i in range(len(list)-1, -1, -1):
        if list[i] == element:
            return i
    return -1


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reverseAlphabet = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

for i in range(len(alphabet)):
    print('For element: ' + alphabet[i] + ', it is located at: ' + str(sequentialSearch(alphabet, alphabet[i])) + '\n')

print('--------------------')

for i in range(len(reverseAlphabet)):
    print('For element: ' + reverseAlphabet[i] + ', it is located at: ' + str(reverseSequentialSearch(reverseAlphabet, reverseAlphabet[i])) + '\n')