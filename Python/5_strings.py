def double_word(word):
    word = word*2+str(len(word))
    return word

def first_and_last (message):
    if message == "":
        return True
    elif message[0] == message[-1]:
        return True
    else:
        return False

def initials(phrase):
    words = phrase.upper().split()
    result = ""
    for word in words:
        result += words
    return word

print(double_word("Hello"))
print(first_and_last(""))
##print(initials("Universal Serial Bus"))
print("Universal Serial Bus".split())

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])

def count_letters(text):
  result = {}
  text = text.lower()
  # Go through each letter in the text
  for letter in text:
   
    # Check if the letter needs to be counted or not
    if letter.isalpha() :
      # Add or increment the value in the dictionary
      count = text.count(letter)
      result[letter] = count
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))