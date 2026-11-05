class Tic_Tac_Toe:
    def __init__(self):
        self.board=[[0,0,0],[0,0,0],[0,0,0]]
        g=False
        while not g:
            self.player_character = input("Please enter your character(excluding '#' and '0'):")
            if self.player_character=="#" or self.player_character=="0":
                print(self.player_character,"is not acceptable. Please give input again.")
            else:
                g=True
        self.computer_character = "#"
    def decision(self):
        #q=[[(1,-1),(-1,1)], [(-1,-1),(1,1)], [(-1,0),(1,0)], [(0,1),(0,-1)], [(0,1),(0,2)], [(0,-1),(0,-2)], [(-1,0),(-2,0)],[(1,0),(2,0)]]
        q = [[(1, -1), (-1, 1)], [(-1, -1), (1, 1)], [(-1, 0), (1, 0)], [(0, 1), (0, -1)]]
        tie=True
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j]==0:
                    tie=False
                else:
                    p=self.board[i][j]
                    for fire in q:
                        v1=fire[0][0]
                        v2=fire[0][1]
                        v3=fire[1][0]
                        v4=fire[1][1]
                        if i+v1>=0 and i+v1<=2 and j+v2>=0 and j+v2<=2 and self.board[i+v1][j+v2]==p and i+v3<=2 and i+v3>=0 and j+v4<=2 and j+v4>=0 and self.board[i+v3][j+v4]==p:
                            if p==self.computer_character:
                                print("Computer wins!!!")
                            else:
                                print("You win")
                            return True
        if tie:
            print("Tie!!!")
            return True
        return False


    def show_board(self):
        for i in range(0,3):
            for j in range(0,3):
                if j!=2:
                    print(self.board[i][j],end=" ")
                else:
                    print(self.board[i][j])
    def computer_turn(self):
        q=[[(1,-1),(-1,1)], [(-1,-1),(1,1)], [(-1,0),(1,0)], [(0,1),(0,-1)], [(0,1),(0,2)], [(0,-1),(0,-2)], [(-1,0),(-2,0)],[(1,0),(2,0)]]
        #q = [[(1, -1), (-1, 1)], [(-1, -1), (1, 1)], [(-1, 0), (1, 0)], [(0, 1), (0, -1)]]
        computer=False
        # computer trying to win
        for i in range(0,3):
            if computer:
                break
            for j in range(0,3):
                if computer:
                    break
                if self.board[i][j]==0:
                    for fire in q:
                        if computer:
                            break
                        gasoline=fire[0]
                        thermite=fire[1]
                        a1=i+gasoline[0]
                        a2=j+gasoline[1]
                        v1=i+thermite[0]
                        v2=j+thermite[1]
                        if a1>=0 and a1<=2 and a2>=0 and a2<=2 and self.board[a1][a2]==self.computer_character and v1>=0 and v1<=2 and v2>=0 and v2<=2 and self.board[v1][v2]==self.computer_character:
                            self.board[i][j]=self.computer_character
                            computer=True
                            break
        if computer:
            return
        # computer trying to prevent the player to win
        for i in range(0,3):
            if computer:
                break
            for j in range(0,3):
                if computer:
                    break
                if self.board[i][j]==self.player_character:
                    for fire in q:
                        if computer:
                            break
                        for k in range(0,2):
                            t=fire[k][0]
                            t1=fire[k][1]
                            if i+t<=2 and i+t>=0 and j+t1<=2 and j+t1>=0 and self.board[i+t][j+t1]==self.player_character:
                                k1=0
                                if k==k1:
                                    k1=1
                                h=fire[k1][0]
                                h1=fire[k1][1]
                                if i+h<=2 and i+h>=0 and j+h1<=2 and j+h1>=0 and self.board[i+h][j+h1]==0:
                                    self.board[i+h][j+h1]=self.computer_character
                                    computer=True
        # random turn as computer can't win or prevent player to win
        for i in range(0,3):
            if computer:
                break
            for j in range(0,3):
                if computer:
                    break
                if self.board[i][j]==0:
                    self.board[i][j]=self.computer_character
                    computer=True

    def player_turn(self):
        #self.show_board()
        n=False
        while not n:
            x=int(input("Enter the row number:"))
            y=int(input("Enter the column number:"))
            if x<0 or x>2 or y<0 or y>2:
                print("Your input suggests outside the board. Please give input again")
            elif self.board[x][y]!=0:
                print("There is already a",self.board[x][y],"in(",x,",",y,") cell of the board. Please give input again.")
            else:
                self.board[x][y] = self.player_character
                n=True
    def start_game(self):
        computer=False
        while not self.decision():
            if not computer:
                self.show_board()
                self.player_turn()
                computer=True
            else:
                self.computer_turn()
                computer=False
        print("Here is the final game board:")
        self.show_board()

game=Tic_Tac_Toe()
game.start_game()