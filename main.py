def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	characters = count_characters(text)
	print(f"--- Begin report of {book_path}")
	character_report(characters)
	print("--- End Report ---")			
	#print(f"{num_words} words found")
	#print(f"The following characters were found: {characters}")
	
	
def get_num_words(text):
	word_count = len(text.split())
	return word_count
	
def get_book_text(path):
	with open(path) as f:
		return f.read()
	

def count_characters(text):
	char_dict = {}
	lowered_text = text.lower()
	char_list = list(lowered_text)
	for char in char_list:
		if char not in char_dict:
			char_dict[char] = 1
		else:
			char_dict[char] += 1
	return char_dict
	
def character_report(char_dict):
	alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

	for alpha in alphabet:
		for c in char_dict:
			if alpha == c:
				print(f"The '{c}' character was found {char_dict[c]}")
	

	#print(char_dict)
	
	
main()