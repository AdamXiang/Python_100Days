#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt", mode="r") as data:
    names = data.readlines()  #  一次讀很多行，並存入list

with open("Input/Letters/starting_letter.txt") as letter:
    letter_format = letter.read()
    for name in names:
        cut = name.strip('\n')
        w_txt = letter_format.replace("[name]", f"{cut}")
    with open(f"Output/ReadyToSend/letter_for_{cut}.txt", mode="w") as text:
        text.write(w_txt)