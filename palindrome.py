import re



# TODO: return True or False if the sentence is or isn't a palindrome
def is_palindrome(sentence):
    sentence = re.sub(r'[^A-Za-z]', "", (sentence.lower()))
    sentence_rev = sentence[::-1]
    if sentence == sentence_rev:
         return ("True")
    else:
         return ("False")

def main():
    sentence =input("What is your sentence? ")
    is_palindrome(sentence)
    check = is_palindrome(sentence)
    if check:
       print("{} is a palindrome".format(sentence))
    else:
       print("{} is not a palindrome".format(sentence))


if __name__ == '__main__':
   main()
