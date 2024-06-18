with open("./Input/Names/invited_names.txt") as inviting_names:
    inviting_names_list = inviting_names.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letters:
    changing_names = starting_letters.read()
    for name in inviting_names_list:
        stripped_names = name.strip()
        inviting_letters = changing_names.replace("[name]", stripped_names)
        print(inviting_letters)
        with open(f"./Output/ReadyToSend{stripped_names}.txt", mode="w") as completing_invitation:
            final_invitation = completing_invitation.write(inviting_letters)
