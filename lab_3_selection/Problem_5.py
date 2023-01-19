# Patryk Kostek
# Lab 3 Problem 5
#
'''
    Design and implement a program that allows the user to play Rock Paper Scissors
    (Lizard Spock anyone?)  against the computer.  The user begins by entering either
    Rock, Paper or Scissors at the keyboard.  The computer's move should be implemented
    by generating a random number between 1 and 3.  1 = Rock, 2 = Paper, 3 = Scissors.
    The program should display the user's move as well as the computer's move AND should
    display who won.  It is NOT necessary to validate the input from the user.  Your
    solution should have a function called displayWinner as well as main function.
    displayWinner should have 2 parameters, the user's choice and the computer's choice.
    displayWinner should display each choice as well as who won.  main should generate the
    computer's choice, get the user's choice and call the displayWinner function.


IPO Chart:
    Input
        u_choice
    Processing
        import random library
        define constants 1 = ROCK, 2 = PAPER, 3 = SCISSORS
        define random_num function, generate number 1-3 return as c_choice
        define gather_input function, gathers constant  return as u_choice

        define display_winner(u_choice, c_choice) function
            if u_choice is same as c_choice then
                message is 'It's a Tie!'
            elif u_choice is rock and c_choice is scissors
                message is 'You win, rock beats scissors!
            elif u_choice is scissors and c_choice is paper
                message is 'You win, scissors beats paper!
            elif u_choice is paper and c_choice is rock
                message is 'You win, paper beats rock!
            else print(f'You lose, c_choice beats u_choice!)

        state the welcome message showing instructions
        gather the input
        display the winner using display_winner
    Output
        display the winner.


Algorithm:
    gather_input
        gather input, define color1
        gather input, define color2
        return color1 and color2
    end gather_input

    display_color(color1, color2)
            if color1 is red and color2 is yellow
                then color3 is orange
            elsif color1 is red and color2 is blue
                then color3 is purple
            elsif color1 is yellow and color2 is blue
                then color3 is green
            else
                state error handle code
     end display_color

    main
        define the list of combination colors
        print the welcome message
        define color1 and color2 from gather_input
        define color 3 from display_color
        if color 3 is in list of combination colors
            print the color mixture
        else print the error handling message
    end main
'''