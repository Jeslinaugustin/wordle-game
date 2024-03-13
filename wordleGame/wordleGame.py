
import os
import random
import board
os.system("cls")


def printInstruction(numberOfTries,wordLength):
    print("\n\nGame Instructions.\nGuess the word in " +str(numberOfTries)+" tries.\n" +
            "Each guess must be a valid "+str(wordLength)+" letter word(limited to the words present in the local directory)\n" +
            "The background colors of the word show how close your guess was to the word\n\n" +
            "A letter in green background indicates,the letter in the word at correct location\n" +
            "A letter in blue background indicates, the letter in the word at wrong location\n" +
            "A letter in red background indicates the letter is not present in the word\n\n" +
            "For Example\n"
            )
    print("\u001b[32mS", end='')
    print("\u001b[34mLEE",end='')
    print("\u001b[31mP")
    print("\u001b[30mHere S correct location\nL,E,E at wrong locations\nP not in the wordle")

def askForWord(wordLength, wordList):
    wordValid = False
    while(not wordValid ):
        enterdWord = input("Enter a "+str(wordLength)+" letter word: ")
        if ((enterdWord.upper() in wordList) and (len(enterdWord)==wordLength) and (enterdWord.isalpha())):
            wordValid = True
    return enterdWord

def playGame(gameBoard,maxNumberOfTries,hiddenWordle,wordLength, wordList):
    print("entered playgame")
    gameWin = False;
    numberOfTries=0
    userEnterdWord =""
    while(numberOfTries < maxNumberOfTries):
        userEnterdWord = askForWord(wordLength, wordList);
        print(userEnterdWord)
        gameBoard.updateBoard(userEnterdWord,hiddenWordle,numberOfTries)
        gameBoard.displayBoard()
        if (userEnterdWord == hiddenWordle):
            gameWin =True
            break
        numberOfTries +=1
    if gameWin:
        print("You won the word was "+hiddenWordle)
    else:
        print("You are out of tries the word was "+hiddenWordle)

def updateWordList(fileName,wordLength):
    if(os.path.exists(fileName)):
        file = open(fileName,"r")
        wordListReaded = file.readlines()
        wordListReaded =[x[:wordLength] for x in wordListReaded if (x[-1]=="\n")]
        wordList = [x.upper() for x in wordListReaded if ((len(x)==wordLength) and (x.isalpha()))]
        file.close()
        return wordList
    else:
        raise Exception("File not exists")

numberOfGuess = 6
wordLength = 5
wordListFile = "wordlist"
try:
    wordList =updateWordList(wordListFile,wordLength)
    print("wordlist",wordList)
    if (len(wordList)==0):
        raise Exception("No valid words in the file")
    else:
        hiddenWord =random.choice(wordList)
        printInstruction(numberOfGuess,wordLength)
        gameBoard = board.gameBoard(numberOfGuess,wordLength)
        gameBoard.resetBoard()
        gameBoard.displayBoard()
        playGame(gameBoard,numberOfGuess,hiddenWord,wordLength, wordList)
except Exception as error:
    print("An error occurred:", error)
