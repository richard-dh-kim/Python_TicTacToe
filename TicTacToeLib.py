
def eraseTable (tab):
   '''
   (list) -> None
   This function prepares the game table (array) 
   by putting '-' in all the elements.
   It does not create a new array
   Preconditions: tab is a reference to an nxn array matrice n x n that contains '-', 'X' or 'O'
   '''

   for i in range(len(tab)):
       for j in range(len(tab[0])):
           tab[i][j]="-"


def verifyWin(tab):  
    '''(list) ->  bool
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    * Verify if there is a winner.
    * Look for 3 X's and O's in a row, column, and diagonal.
    * If we find one, we display the winner (the message "Player X has won" 
    * or "Player O has won!") and returns True.
    * If there is a draw (verify it with the function testdraw),
    * display "It is a draw" and returns True.
    * If the game is not over, returns False.
    * The function call the functions testrows, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Those functions returns the winner 'X' or 'O', or '-' if there is no winner.
    '''
    if(testLignes(tab) == 'X' or testCols(tab) == 'X' or testDiags == 'X'):
        print("Player X has won!")
        return True
    elif(testLignes(tab) == 'O' or testCols(tab) == 'O' or testDiags(tab) == 'O'):
        print("Player O has won!")
        return True
    elif(testDraw(tab) == True):
        print("It is a draw.")
        return True

    return False  # to change

 
def testLignes(tab):
    ''' (list) ->  str
    * verify if there is a winning row.
    * Look for three 'X' or three 'O' in a row.  
    * If they are found, the character 'X' or 'O' is returned, otherwise '-' is returned.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    '''

    for i in range(len(tab)):
        if ((tab[i][0] == 'o' or tab[i][0] == 'O') and (tab[i][1] == 'o' or tab[i][1] == 'O') and (tab[i][2] == 'o' or tab[i][2] == 'O')):
            return 'O'
        elif((tab[i][0] == 'x' or tab[i][0] == 'X')  and (tab[i][1] == 'x' or tab[i][1] == 'X')  and (tab[i][2] == 'x' or tab[i][2] == 'X')):
            return 'X'
            
    return '-'        # to be modified so that it returns the winner, or '-' if there is no winner 

  
  
def testCols(tab):
    ''' (list) ->  str
    * verify a winning column.
    * look for three 'X' or three 'O' in a column.  
    * If it is the case the character 'X' or 'O' is returned, otherwise '-' is returned.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    '''

    for i in range(len(tab[0])):
        if ((tab[0][i] == 'o' or tab[0][i] == 'O') and (tab[1][i] == 'o' or tab[1][i] == 'O') and (tab[2][i] == 'o' or tab[2][i] == 'O')):
            return 'O'
        elif((tab[0][i] == 'x' or tab[0][i] == 'X')  and (tab[1][i] == 'x' or tab[1][i] == 'X')  and (tab[2][i] == 'x' or tab[2][i] == 'X')):
            return 'X'

    return '-'   #to be modified so that it returns the winner, or '-' if there is no winner


def testDiags(tab):
    ''' (list) ->  str
    * Look for three 'X' or three 'O' in a diagonal.  
    * If it is the case, the character 'X' or 'O' is returned
    * otherwise '-' is returned.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    '''

    if (((tab[0][0] == 'o' or tab[0][0] == 'O') and (tab[1][1] == 'o' or tab[1][1] == 'O') and (tab[2][2] == 'o' or tab[2][2] == 'O')) or ((tab[0][2] == 'o' or tab[0][2] == 'O') and (tab[1][1] == 'o' or tab[1][1] == 'O') and (tab[2][0] == 'o' or tab[2][0] == 'O'))):
        return 'O'
    elif(((tab[0][0] == 'x' or tab[0][0] == 'X')  and (tab[1][1] == 'x' or tab[1][1] == 'X')  and (tab[2][2] == 'x' or tab[2][2] == 'X')) or ((tab[0][2] == 'x' or tab[0][2] == 'X')  and (tab[1][1] == 'x' or tab[1][1] == 'X')  and (tab[2][0] == 'x' or tab[2][0] == 'X'))):
        return 'X'
    return '-'   # #to be modified so that it returns the winner, or '-' if there is no winner

  
  
def testDraw(tab):
    ''' (list) ->  bool
    * verify if there is a draw
    * check if all the array elements have X or O, not '-'.  
    * If we do not find find any '-' in the array, return True. 
    * If there is any '-', return false.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    '''

    for i in range(len(tab)):
        for item in range(len(tab[0])):
            #print(tab[i][item])
            if tab[i][item] == '-':
                return False
             # to BE modiffied
    return True


