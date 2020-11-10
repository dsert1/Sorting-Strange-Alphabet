# @author Deniz Sert
# @version September 25, 2020


# **** HELPERS *****

def make_alphabet():
	'''returns dict mapping 0...25 to chars in alphabet'''
	alphabet = letter_count = dict([(chr(i),0) for i in range(97,123)])
	k = 0
	for char, i in alphabet.items():
		alphabet[char] += k
		k += 1
	return alphabet



def counting_sort(A, sorting_index):
	'''Sort A assuming items have non-negative keys'''
	alphabet = make_alphabet() # 1 + to include 0
	u = 1 + max([alphabet[x[sorting_index]] for x in A]) # O(n): find max key. you could just do u = 26, bc we know all is 26 letters
	D = [[] for i in range(u)] # O(u) direct access array of chains
	for x in A: # sorting step. placing things into buckets
		D[alphabet[x[sorting_index]]].append(x)
	i = 0
	for chain in D: # O(u): read out items in order. Fancy way to put back into array 
		for x in chain:
			A[i] = x
			i += 1
	return A

# **************

# **** MAIN MARTIAN ***
def martian_sort(wordlist, order):
	'''
	Inputs a list of Martian words and a permutation representing order

	Returns the wordlist sorted based on order. As per the problem set 3 writeup.

	Runs in O(kn) time.
	'''

	while order:
		wordlist = counting_sort(wordlist, order.pop())
	return wordlist
	

# *******************






