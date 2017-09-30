path = "C:/Users/anton/Documents/Python/PappApp/v1.2/"

def chooseOption():
    print("Välj ett av följande alternativ: \n\n 1. Skapa ordlista \n 2. Radera ordlista \n 3. "
          "Redigera ordlista \n 4. Testa dina kunskaper\n 5. Avsluta \n")
    opt = input("Ange med en siffra vad du vill göra: ")
    try:
        opt = int(opt)
    except:
        print("\nFuck you! A digit, you retard!\n")
        chooseOption()
    if opt == 1:
        createDB()
    elif opt == 2:
        deleteDB()
    elif opt == 3:
        editDB()
    elif opt == 4:
        test()
    elif opt == 5:
        import sys
        sys.exit()
    else:
        print("\nFuck you! A valid digit, you retard!\n")
    chooseOption()


def createDB():
    createDBinstructions()
    name = nameDB()
    constantWords = open(name,"w")
    constantWords.close()
    addWords(name)


def nameDB():
    return input('Döp din ordlista:\n')+'.txt'


def addWords(name):
    while True:
        constantWords = open(name, "a")
        itaWord=input('Skriv ett ord du vill lägga till i ordlistan på italienska:\n')
        if itaWord.lower() == 'färdig':
            break
        else:
            constantWords.write(itaWord +"\n")
            constantWords.write(input('Skriv ett ord du vill lägga till i ordlistan på svenska:\n')+"\n")
        constantWords.close()
        printOutWords(name)


def createDBinstructions():
    print("\nNu lägger du in ord i databasen. \n"
          "Du blir först ombedd att skriva ordet på italienska och sedan vad det betyder på svenska. Om du vill sluta "
          "mata in ord skriver du 'Färdig'\n")


def printOutWords(name):
    read_words = open(name, 'r')
    print(read_words.read())


def deleteDB():
    import glob, os
    os.chdir(path)
    deleteWords = input('Vill du radera någon ordlista?\n')
    if deleteWords.lower() == 'ja':
        specifyWordlist = input('Vilken ordlista vill du radera?\n')
        safety = input('Är du säker?\n')
        if safety.lower() == 'ja':
            os.remove("C:/Users/herman/PycharmProjects/language/" + specifyWordlist + ".txt")
        goAgain = input('Vill du ta bort någon mer?\n')
        if goAgain.lower() == 'ja':
            deleteDB()


def editDB():
    showExistingDB()
    selectedList = selectList()
    print('Orden i listan är:\n')
    printOutWords(selectedList)
    open(selectedList, "a")
    try:
        answer = determineAddOrDelete()
    except:
        print('Något har gått fel')
        determineAddOrDelete()
    if answer.lower() == 'radera':
        removeWords(selectedList)
    elif answer.lower() == 'addera':
        addWords(selectedList)
    else:
        print('Något har gått fel')


def selectList():
    selectedList = input('Vilken lista vill du välja?\n')+'.txt'
    return selectedList


def determineAddOrDelete():
    addOrDelete = input('Ange om du vill radera eller addera ord:\n')
    if addOrDelete.lower() == 'radera':
        return 'radera'
    elif addOrDelete.lower() == 'addera':
        return 'addera'
    else:
        print('Inget alternativ valt')


def showExistingDB():
    showDatabase = input('Vill du visa existerande ordlistor?')
    if showDatabase.lower() == 'ja':
        print('Detta är dina ordlistor du sparat hittills:\n')
        import glob, os
        os.chdir(path)
        for file in glob.glob("*.txt"):
            file = file[:-4]
            print(file)


def removeWords(selectedList):
    while True:
        selectedWordIta = input('Vilket ord vill du ta bort? (på italienska)\n')
        if selectedWordIta.lower() == 'färdig':
            break
        selectedWordSwe = input('Vad är motsvarigheten för ordet på svenska?\n')
        constantWords = open(selectedList,'r')
        lines = constantWords.readlines()
        constantWords.close()
        constantWords = open(selectedList,'w')
        for line in lines:
            if line != selectedWordIta+'\n' and line != selectedWordSwe+'\n':
                constantWords.write(line)
    constantWords.close()


def test():
    selectedList = input('Vilken lista vill du öva på?\n')+'.txt'
    constantWords = open(selectedList, 'r')
    lines = constantWords.readlines()
    constantWords.close()
    k = 0
    for line in lines:
        k += 1
        if k%2 != 0:
            answer = input('Vad är \n' + line + 'på svenska?\n')
        else:
            if line == answer + '\n':
                print(answer + ' var rätt!\n')
            else:
                print(answer + ' var tyvärr fel.. Rätt svar var\n' + line)
    if goAgain() == 'yes':
        test()


def goAgain():
    yesOrNo = input('Vill du börja om?\n')
    if yesOrNo.lower() == 'ja':
        return 'yes'
    else:
        return 'no'


def continueProcess():
    yesOrNo = input('Vill du fortsätta?\n')
    if yesOrNo.lower() == 'ja':
        return 'yes'
    else:
        return 'no'


#    while line != "":
#        k =+ 1
#        line = constantWords.readline(k)
#        #italienskt
#        constantWords.readline(k+1)
#        #svenskt
#        constantWords.readline(k-1)