def eleminate():
 vowels = ("a", "e","i", "o", "u")

 string = input("Enter word")

 altered_word = ""

 for i in string:
     if i not in vowels:
         altered_word += i
     print(altered_word)

eliminate()





