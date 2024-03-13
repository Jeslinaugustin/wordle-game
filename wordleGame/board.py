
class gameBoard:
    def __init__(self,row,column):
        self.row = row
        self.column = column
        self.board =[]

    def resetBoard(self):
        for i in range(self.row):
            newList = []
            for j in range(self.column):
                newList.append((" ","black"))
            self.board.append(newList)

    def displayBoard(self):
        print("-"*3*self.column)
        for i in self.board:
            for j in i:
                print("|",end='')
                if (j[1] == "black"):
                    print(j[0], end=" ")
                elif (j[1] =="green"):
                    print("\u001b[32m{}".format(j[0]), end=" ")
                elif (j[1] =="blue"):
                    print("\u001b[34m{}".format(j[0]), end=" ")
                elif (j[1] =="red"):
                    print("\u001b[31m{}".format(j[0]), end=" ")
            print("\u001b[30m|\n"+"-" * 3 * self.column)

    def countDictUpdate(self,word):
        letterCount = {}
        for letter in word:
            if letter in letterCount:
                letterCount[letter] +=1
            else:
                letterCount[letter] = 1
        return letterCount

    def updateBoard(self,enteredWord,hiddenWord,trialNumber):
        hiddenWordUpper = hiddenWord.upper();
        enteredWordUpper = enteredWord.upper();
        hiddenLetterCount = self.countDictUpdate(hiddenWordUpper)
        enteredLetterCount = self.countDictUpdate(enteredWordUpper)
        k=0
        for i,j in zip(hiddenWordUpper,enteredWordUpper):
            if (j==i):
                self.board[trialNumber][k]=(j,"green")
                hiddenLetterCount[i] -=1
                enteredLetterCount[j] -=1
            elif (j in hiddenWordUpper) and (
                    (hiddenLetterCount[j]) >= (enteredLetterCount[j])):
                self.board[trialNumber][k] = (j, "blue")
                hiddenLetterCount[j] -= 1
                enteredLetterCount[j] -= 1
            else:
                self.board[trialNumber][k] = (j, "red")
                enteredLetterCount[j] -= 1
            k +=1





