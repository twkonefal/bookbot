import sys
from stats import get_num_words, count_chars, sort_dict_by_key

def check_args():
  if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
  check_args()

  book_path = sys.argv[1] # "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)

  all_chars = {}
  all_chars = count_chars(text)
  #print(all_chars)

  sorted_list = sort_dict_by_key(all_chars)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")

  for c in sorted_list:
    if not (c["char"]).isalpha():
      continue
    print(f"{c['char']}: {c['num']}")

  print("============= END ===============")



def get_book_text(path_to_file:str):
  with open(path_to_file) as f:
    return f.read()

# RUN
main()