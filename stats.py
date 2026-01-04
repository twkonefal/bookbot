def get_num_words(string:str):
  return len(string.split())

def count_chars(string:str):
  lower_string = string.lower()
  char_counts = {}

  for c in lower_string:
    if not c in char_counts:
      char_counts[c] = 0
    char_counts[c] += 1

  return char_counts

def make_list(dictionary:dict):
  my_list = []

  for keys, values in dictionary.items():
    my_list.append({"char": keys, "num": values})

  return my_list


def sort_on(items):
  return items["num"]

def sort_dict_by_key(char_counts:dict):
  sorted_list = []

  unsorted_list = make_list(char_counts)
  sorted_list = sorted(unsorted_list, reverse=True, key=sort_on)

  return sorted_list