import random
list = ['qwerty', 'hoi', 'test', 'milan', 'dier', 'contaminatie', 'exterminatie', 'aap', 'ziekenhuis', 'blok', 'achterwerk', 'tanden', 'pen', 'scherm', 'helm', 'kop', 'zwaard', 'rood', 'romeinen', 'mongolen', 'raam', 'glas', 'venster', 'oor', 'neus', 'trui', 'hand', 'nagel', 'spijker', 'chip', 'zeil', 'mast', 'toets', 'bladzijde', 'poot', 'haar', 'naam', 'woord', 'wachtwoord', 'oogbol', 'matje']
count = 0
lives = 10
# Zet een '#' voor de vier onderstaande regels om de grote woordenlijst uit te schakelen.
# Je kan je eigen woorden toevoegen aan de lijst genaamd 'list' hierboven door je woorden
# op dezelfde manier te schrijven als de woorden die al in de lijst hierboven staan.

#with open("dutch.txt") as file:
#  words = file.read().split()
#  for i in range(len(words)):
#    list.append(words[i])

againloop = True

while againloop:
  SecretWord = (random.choice(list))
  Length = len(SecretWord)
  streepjes = []
  for i in range(len(SecretWord)):
    streepjes.append("-")
  loop = 1
  while loop == 1:
    print ("Het geheime woord: " + "".join(streepjes))
    streepjes = []
    for i in range(len(SecretWord)):
      streepjes.append("-")
    InputWord = input("Raad het woord:    ")
    count +=1
    print("")
    if InputWord == "print(SecretWord)":
      print(SecretWord)
    else:
      for i in range(len(InputWord)):
        if len(InputWord) > len(SecretWord):
            print ("Probeer de lengte van je ingevoerde woord gelijk te houden aan de lengte van het geheime woord")
            break
        else:
            if InputWord[i] == SecretWord[i]:
                streepjes[i] = InputWord[i]
            elif (InputWord[i] in SecretWord and streepjes[i] == "-" and (streepjes[SecretWord.index(InputWord[i])] == "-" or streepjes[SecretWord.index(InputWord[i])]=="?")):
              streepjes[i] = "?"

    WordLength = len(InputWord)
    if InputWord == (SecretWord):
      loop = 0
      againloop = False
      print ("Je hebt gewonnen!")
      print ("Het geheime woord was",(SecretWord))
      print ("Je hebt het woord in " + str(count) + " beurten geraden")
      YesNo = input("Wil je nog een keer spelen? J/N:")
      if YesNo.lower() == ("j"):
        print ("")
        count = 0
        againloop = True
      else:
        print ("")
        print ("Oke, tot de volgende keer!")
        break

    else:
      lives = lives-1
      if lives == 0:
        print ("Je levens zijn op. Probeer het opnieuw")
        YesNo = input("Wil je nog een keer spelen? J/N:")
        if YesNo.lower() == ("j"):
          print ("")
          count = 0
          lives = 10
          againloop = True
        else:
          print ("")
          print ("Oke, tot de volgende keer!")
          break
      else:
        print ("Levens: " + str(lives))
        print ("Probeer een ander woord")
