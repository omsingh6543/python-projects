def functions(your_choice, comp_choice):
    if your_choice == comp_choice:
        print("Both moves are same: Match tie\n")
    elif your_choice == "stone":
        if comp_choice == "paper":
            print("Paper covers stone: Computer wins\n")
        else :
            print("Stone smashes scissor: You wins\n")
    elif your_choice == "paper":
        if comp_choice == "stone":
            print("Paper covers stone: You wins\n")
        else :
            print("Scissor cuts paper: Computer wins\n")
    else:
        if comp_choice == "stone":
            print("Stone smashes scissor: Computer wins\n")
        else:
            print("Scissor cuts paper: You wins\n")            