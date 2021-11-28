print("\t\t\tWelcome to the Thesaurus App.")
caliente={'calido','veraniego','tropical','hirviente','abrasador'}
frio={'gelido','fresco','helado','frigido','polar'}
feliz={'contento','alegre','jovial','jocoso'}
triste={'infeliz','abatido','miserable','cabizbajo','melancolico'}

print("Choose a word from the thesaurus and i will give you a synonym.")
print("Here are the words in the thesaurus: ")
print("-Hot")
print("-Cold")
print("Happy")
print("-Sad")

thesaurus=input("What word you like a synonym for: ")
print("A synonym for hot is boiling.")
confir=input("Would you like to see the whole thesaurus (yes/no ")

if thesaurus=='hot':
    print(caliente)
    print("cold synonyms are: ",frio)
    print("happy synonyms are: ",feliz)
    print("sad synonyms are: ",triste)
if thesaurus=='cold':
    print(frio)
    print("happy synonyms are: ",feliz)
    print("sad synonyms are: ",triste)
    print("hot synonyms are: ",caliente)
if thesaurus=='happy':
    print(feliz)
    print("sad synonyms are: ",triste)
    print("hot synonyms are: ",caliente)
    print("cold synonyms are: ",frio)

if thesaurus=='sad':
    print(triste)
    print("hot synonyms are: ",caliente)
    print("cold synonyms are: ",frio)
    print("happy synonyms are: ",feliz)
else:
    thesaurus=='no'
    print("I hope you enjoyed the program. Thank you!.")

