from stats import wordcount
from stats import charactercount
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        full_book = f.read()
        #print(full_book)
        
def main():
    if len(sys.argv) < 2 or sys.argv == "":
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    get_book_text(sys.argv[1])
    print("---------- Word Count ----------bootdev run d6536f09-dc1d-4922-a2a5-a73c536ee09d")
    wordcount(sys.argv[1])
    print("-------- Character Count --------")
    charactercount(sys.argv[1])
    print("============= END ===============")

main()
