"""Find all word-pair palingrams in a dictionary file."""
import load_dictionary

word_list = load_dictionary.load('words.txt')

# Find word-pair palingrams
def find_palingrams() -> list[tuple[str,str]]:
    """Find dictionary palingrams."""
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list

palingrams = find_palingrams()

# Sort palingrams on first word
palingrams_sorted = sorted(palingrams)

# Display list of palingrams
print(f"\nNumber of palingrams = {len(palingrams_sorted)}")
for first, second in palingrams_sorted:
    print(f"{first} {second}")
