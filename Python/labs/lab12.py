sent=input("Enter a sentence: ")
print('================================================')
print("           DOCUMENT ANALYSIS REPORT             ")
print('================================================')

total_chars = len(sent)
words=len(sent.split())
vowels=0
consonants=0
digits=0
spaces=0
special=0
for ch in sent:
    if ch.lower() in "aeiou":
        vowels+=1
    elif ch.isalpha():
        consonants+=1
    elif ch.isdigit():
        digits+=1
    elif ch.isspace():
        spaces+=1
    else:
        special+=1
total_letters=vowels+consonants
if total_letters>0:
    vowel_ercentage=(vowels/total_letters)*100
else:
    vowel_ercentage=0
print("Sentence:",sent)  
print(f"Total characters: {total_chars}")

print("---------- CHARACTER BREAKDOWN ----------")     

print(f"Total words: {words}")
print(f"Total vowels: {vowels}")
print(f"Total consonants: {consonants}")
print(f"Total digits: {digits}")
print(f"Total spaces: {spaces}")
print(f"Total special characters: {special}")

print('---------Summary---------')
print("Total letters:",total_letters)
print(f"Vowel percentage: {vowel_ercentage:.2f}%")

print('================================================')
print("               Analysis Complete!               ")
print('================================================')