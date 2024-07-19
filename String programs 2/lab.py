def replace_characters(original_string, old_chars, new_chars):
     if original_string is None or old_chars is None or new_chars is None:
        raise ValueError("None argument provided")

    return original_string.replace(old_chars, new_chars)
   

def split_string(original_string, delimiter):
    if original_string is None or delimiter is None:
        raise ValueError("None argument provided")
    
    return original_string.split(delimiter)

def join_strings(string_list, separator):
    if string_list is None or separator is None:
        raise ValueError("None argument provided")

    return separator.join(string_list)
   

def count_occurrences(original_string, char):
      return original_string.count(char)

def find_char_index(original_string, char):
  if original_string is None or char is None:
        raise ValueError("None argument provided")
    if len(char) != 1:
        raise ValueError("The 'char' parameter must be a single character")
    
    try:
        return original_string.index(char)
    except ValueError:
        return -1

def starts_with_substring(original_string, substring):
    if original_string is None or substring is None:
        raise ValueError("None argument provided")

    return original_string.startswith(substring)

def ends_with_substring(original_string, substring):
     if original_string is None or substring is None:
        raise ValueError("None argument provided")

    return original_string.endswith(substring)
