
def wordcount(filepath):
     with open(filepath) as f:
         full_book = f.read()
         words = full_book.split()
         print(f"Found {len(words)} total words")

def charactercount(filepath):
    char_counts = {}

    with open(filepath, encoding="utf-8") as f:
        text = f.read().lower()
        for char in text:
            if char.isalpha():  # Only count alphabetical characters
                char_counts[char] = char_counts.get(char, 0) + 1

    # Sort the dictionary by count descending
    sorted_char_counts = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))

    # Print output as requested
    for char, count in sorted_char_counts.items():
        print(f"{char}: {count}")