def tictac_toe():
    first = True
    
    used = []
    
    p1choices = []
    
    p2choices = []
    
    board = list(' _|_|_\n _|_|_\n  | | \n')
    
    def win_check(choices):
        if ('1' in choices) and ('2' in choices) and ('3' in choices):
             return True
        elif ('1' in choices) and ('4' in choices) and ('7' in choices):
             return True
        elif ('3' in choices) and ('5' in choices) and ('7' in choices):
             return True
        
        elif ('1' in choices) and ('5' in choices) and ('9' in choices):
             return True
        
        elif ('3' in choices) and ('6' in choices) and ('9' in choices):
             return True
            
        elif ('7' in choices) and ('8' in choices) and ('9' in choices):
             return True
        elif ('2' in choices) and ('5' in choices) and ('8' in choices):
             return True
        elif ('4' in choices) and ('5' in choices) and ('6' in choices):
             return True
    for x in range(0,10):
        
        if (win_check(p2choices)) or (win_check(p1choices)):
            break
        if x < 1:
            restring = ''.join(board)
            print(restring)
        while first:
            
            
            if win_check(p2choices):
                print('p2 WINS!')
                
                break
            p1 = input('player one is up! choose between spots 1-9... ')
            if p1 in used: 
                print('already taken!')
                continue
            elif p1 == '1': board[1] = 'x'
            elif p1 == '2': board[3] = 'x'
            elif p1 == '3': board[5] = 'x'
            elif p1 == '4': board[8] = 'x'
            elif p1 == '5': board[10]= 'x'
            elif p1 == '6': board[12] ='x'
            elif p1 == '7': board[15] ='x'
            elif p1 == '8': board[17] ='x' 
            elif p1 == '9': board[19] ='x'
            elif p1 not in range(1,10):
                continue
            if ((len(p1choices) > 4) or (len(p2choices) > 4)):
                print("it's a draw")
                break
                
            
            used.append(p1)
            p1choices.append(p1)
            restring = ''.join(board)
            print(restring)
            first = False 
       
            
        while not first:     
            if win_check(p1choices):
                print('p1 WINS!')
                break
                
    
            p2 = input('player two is up! choose between spots 1-9... ')
            if p2 in used:
                print('already taken!')
                continue 
            elif p2 == '1': board[1] = 'o'
            elif p2 == '2': board[3] = 'o'
            elif p2 == '3': board[5] = 'o'
            elif p2 == '4': board[8] = 'o'
            elif p2 == '5': board[10]= 'o'
            elif p2 == '6': board[12]= 'o'
            elif p2 == '7': board[15]= 'o'
            elif p2 == '8': board[17]= 'o'
            elif p2 == '9': board[19]= 'o'
            elif p1 not in range(1,10): 
                continue
            if (len(p1choices) > 4) or (len(p2choices) > 4):
                print("it's a draw")
                break
            used.append(p2)
            p2choices.append(p2)
            restring = ''.join(board)
            print(restring)
            first = True
        
    
