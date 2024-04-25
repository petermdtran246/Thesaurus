# Read word and letter from user
word = input().strip()
letter = input().strip()

# Open the corresponding text file
file_name = f"{word}.txt"
with open(file_name, 'r') as file:
    lines = file.readlines()

# Store synonyms in a dictionary
synonyms = {}
for line in lines:
    words = line.strip().split()
    first_word = words[0]
    if first_word[0] not in synonyms:
        synonyms[first_word[0]] = words
    else:
        synonyms[first_word[0]].extend(words[1:])

# Output synonyms for the specified letter
if letter in synonyms:
    for synonym in synonyms[letter]:
        print(synonym)
else:
    print(f"No synonyms for {word} begin with {letter}.")
