options = {'Rock','Paper','Scissor'}
Computer = 0
Player = 0
while True:
    option = input("Choose any option Rock\Paper\Scissor:")
    
    comp_option = options.pop()
    
    if option == 'Quit' or Computer == 10 or Player == 10:
        break
    elif option == 'Rock' and comp_option == 'Rock':
        print("Draw")
    elif option == 'Rock' and comp_option == 'Paper':
        print("Computer Won")
        Computer += 1
    elif option == 'Rock' and comp_option == 'Scissor':
        print("Player Won")
        Player += 1
    elif option == 'Paper' and comp_option == 'Paper':
        print("Draw")
    elif option == 'Paper' and comp_option == 'Rock':
        print("Player Won")
        Player += 1
    elif option == 'Paper' and comp_option == 'Scissor':
        print("Computer Won")
        Computer += 1
    elif option == 'Scissor' and comp_option == 'Scissor':
        print("Draw")
    elif option == 'Scissor' and comp_option == 'Rock':
        print("Computer Won")
        Computer += 1
    elif option == 'Scissor' and comp_option == 'Paper':
        print("Player Won")
        Player += 1
        
    options.add(comp_option)
        
print(f"Player Point:{Player}")
print(f"Computer Point:{Computer}")