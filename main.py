import random # For randomizing things
import pandas as pd # For storing highscores
import os # For changing the screen
import time # For the timer for the game

# HEADS UP!
# - The "x1B[3m" or anything similar is to change some text's color or style (For aesthetic purposes only).  
# - The information on the Wastebook's pages is currently in the progress. 


def mood(): # To set the mood of the game
    os.system('cls') # Clear the screen
    input("\n\"Our planet is counting on you \"")
    input("\n\"Your sacrifice will be remembered..\"")
    os.system('cls')
    input("\nYou obtained an oxygen tank.")
    os.system('cls') 

# lists and dictionaries of the game's components
waste_types = {
    "paper": "B","plastic": "N","glass": "N","aluminum": "N","electronics": "N","metal": "N","cigarette butts": "N","toothbrushes": "N","disposable razors": "N",
    "straws": "N","bottle caps": "N","plastic bags": "N","styrofoam": "N","bubble wrap": "N","plastic utensils": "N","tape": "N","CDs and DVDs": "N","printer cartridges": "N",
    "cell phones": "N","batteries": "N","light bulbs": "N","paint": "N","solvents": "N","aerosol cans": "N","motor oil": "N","tires": "N","fruit scraps": "B","coffee grounds": "B",
    "tea bags": "B","eggshells": "B","grass clippings": "B","leaves": "B","tree branches": "B","food waste": "B","manure": "B","hair and fur": "B","wool clothing": "B",
    "paper napkins": "B","cardboard": "N","strapping": "N","film plastic": "N","rigid plastic": "N","foam rubber": "N","ceramics": "N","crayons": "N","cosmetics": "N",
    "dental floss": "N","fire extinguishers": "N","fishing line": "N","floor wax": "N","insecticides": "N"}
randomquotes = [
  "Sorting trash has never been so risky!", "Breathe deep and sort fast!", "Don't let the trash choke you out!",
  "Match the garbage or face the consequences!", "Test your trash-sorting skills and (not)survive!", "Keep your oxygen above 0% and your trash sorted!",
  "Every litter bit hurts","There is no planet B","Proud people do not litter","Trash sorting is a matter of life and death!",
  "Recycle the present, save the future.","Eat, Sleep, Sort, Suffocate.","Never refuse to reuse.","Sort it out or run out of air! The clock is ticking!",
  "Sort fast, but don't make a mistake or you'll suffocate!","It's easy. Don't mess up.", "Your sacrifice is remembered",
  "Think you have what it takes to be a Trash Sorting Hero? ","The greatest threat to our planet is the belief that someone else will save it. -Robert Swan"]
randomphrase = [
  'You picked up', 'You gathered','You got your hands on','You found','You saw', 'What to do with ']

class Game(): 
  def __init__(self):
    self.time = 66 #default time
  
  def main():
    game = Game() # This ensures that the "self" argument is correctly passed to the play_menu()
    os.system('cls')
    while True: # Display the main menu and handle user choices
        print("\n    =================")
        print("++| SORT OR SUFFOCATE |++")
        print("    =================")
        print("(1) PLAY SOS")
        print("(2) SOS Lore ")
        print("(3) Highscore")
        print("(4) Quit")
        print("(5) Random Quotes\n")
        print("\"\x1B[3m" +random.choice(randomquotes)+ "\x1B[0m\"\n" ) # To print italicized random quotes
        choice = input("Enter Choice: ")
        while choice not in ['1', '2', '3','4', '5', 'q','Q','P','p','S','s','H','h']: 
          print("Invalid input. Please enter 1, 2, 3, 4, or 5")
          choice = input()
        if choice in ['1','P','p']:
          game.play_menu() # Start the game by calling the play_menu()
          os.system('cls')
        elif choice == '2':
          Game.wastebook() # Show wastebook (infos) by calling the wastebook()
          os.system('cls')
        elif choice == '3':
          Game.highScore() # Show high scores by calling the highScore()
          os.system('cls')
        elif choice in ['4','q','Q']:
          quit()
        elif choice == '5':
          os.system('cls')
          Game.main() # Restart/refresh the main menu by calling the main()
        else:
            break # Exit the loop
            
  def play_menu(self):
        os.system('cls')
        print("=========================")
        print ("Select Oxygen Tank level")
        print("=========================")
        print("\n(1) High Tank (100%)")
        print("(2) Normal Tank (66%)")
        print("(3) Low Tank (20%)")
        level = input("\nEnter Choice: ")
        while level not in ['1', '2', '3']:
          print("Invalid input. Please enter 1, 2, or 3")
          level = input()
        if level == '1':
            self.time = 100 # Set the oxygen tank level to 100%
            Game.play_game(self)
        elif level == '2':
            self.time # Set the oxygen tank level to the default level which is 66%
            Game.play_game(self)
        elif level == '3':
            self.time = 20 # Set the oxygen tank level to 20%
            Game.play_game(self)   
              
  def ask_question():
      item = random.choice(list(waste_types.keys())) # Select a random waste item 
      phrase = random.choice(list(randomphrase)) # Select a random phrase
      print("===========================================")
      answer = input(f"+ {phrase} \033[32m{item}? \x1B[0m(N/B/Q): ").upper() # State phrase with the random waste item and phrase. ".upper() converts char to uppercase
      print("===========================================")
      if answer =='q' or answer == 'Q':
        quit()
      if answer != waste_types[item]:
          print(f"\nThe right answer is {waste_types[item]}") # Display the correct answer if the user's answer is incorrect
      return answer == waste_types[item] # Return True if the user's answer is correct, False otherwise
    
  def play_game(self):
    os.system('cls')
    score = 0
    print("\n    ==============================")
    print("++|  ARE YOU READY TO GO OUTSIDE? |++")
    print("   ===============================")
    press = input("\nPress (1) for Tutorial | (Enter) to Play: ")
    if press == '1': # Check if tutorial mode is selected
        os.system('cls')
        print("\nYour Oxygen is at "+str(self.time)+"%")
        print("| It is slowly depleting." )
        print("| You have to sort trash to gain some oxygen back. ")
        print("| One wrong move, it will dwindle faster")
        print("| if it reaches 0 % ....")
        print("| Goodluck, OP.")
        print("===========================")
        print("| [B] = Biodegradable     |")
        print("| [N] = Non-Biodegradable |")
        print("| [Q] = Quit              |")
        print("===========================")
        print("Press Enter to play")
        input()
    else:
      pass
    os.system('cls')
    start_time = time.time()
    while time.time() - start_time < self.time: # Main game loop
        result = Game.ask_question()
        if result: # Process the result of the question
            score += 1 # Increase score and adjust start time
            start_time += random.randint(1,1) # If correct, the time will increase to 1secs
            print(f"\n\033[32mCORRECT | Trash Sorted: {score}\x1B[0m |\033[32m {round(self.time-(time.time() - start_time))}% oxygen remaining\x1B[0m\n") #Display the "correct", current score, and time remaining.
        else:
            start_time -= random.randint(17,30) # Decrease start time in the range of 17-30secs for wrong answer.
            print(f"\n\033[31mWRONG | Trash Sorted: {score} \x1B[0m|\033[31m {round(self.time-(time.time() - start_time))}% oxygen remaining\x1B[0m\n") #Display the "wrong", current score, and time remaining.
    print("\n\n\n\n\n\n\n-----------------------------------------")      
    print(f"YOU RUN OUT OF OXYGEN! You sorted" ,score,"trash") # Game over message
    
    # Assess the player's score and give comment/ feedback.
    if score >= 40:
      print("\"WOW! Your name is probably in the Hero list!!\"")
    elif 30 <= score < 40:
        print("\"Great job!\"")
    elif 20 <= score < 30:
        print("\"Not bad, but you..can do better...\"")
    elif 10 <= score < 20:
        print("\"Thanks for participating!\"")
    elif 5 < score < 10:
        print(f"\"That's too bad. Only",score,"trash? really?\"")
    else:
        print("\"Your sacrifice is not remembered\"")
    print("-----------------------------------------")
    while True: # Prompt the user to provide a username until a valid one is given.
      USERNAME = input("\nEnter Username (5 ABC chr):  ") 
      if len(USERNAME) == 5 and USERNAME.isalpha(): #  Check if the entered username has 5 characters and consists of alphabetic characters only
        break
      else:
            print("5 ABC character only bro.. like \"JESUS\" ")
    WASTE_SORTED = score # Assign the value of 'score' to 'WASTE_SORTED' variable
    with open("highscores.txt", "a") as text_file: # Open the 'highscores.txt' file in append mode and write the username and score
      text_file.write("\n" + USERNAME + ','+ format(WASTE_SORTED) +"\n")
    text_file.close() # Close the file after writing
    return USERNAME, WASTE_SORTED # Return the username and score as a tuple. Tuple: multiple values to be returned as a single entity

  def highScore():
    os.system('cls')
    print("\n   =================")
    print("+  REMEMBERED HEROES  +")
    print("   =================\n")
    df = pd.read_csv('highscores.txt',names=['USERNAME','WASTE_SORTED']) # Read the high scores data from the file into a DataFrame
    df.sort_values(by='WASTE_SORTED',ascending=False,inplace=True) # Sort the Dataframe by the 'WASTE_SORTED' column in descending order
    df.to_csv('highscorer.txt') # Save the sorted DataFrame to a new file
    print(df.head(n=5)) # Display the top 5 high scores
    print("\nThank you for your service\n")
    choice_highscore = input("\nCheck recent heroes? (1)Yes | (2)No: ") # Ask the user if they want to check recent players
    while choice_highscore not in ['1','2']:
      print("Invalid input. Please enter 1 or 2")
      choice_highscore = input("Check recent heroes? (1)Yes | (2)No: ")
    if choice_highscore =='1':
      os.system('cls')
      print("\n   =================")
      print("+  RECENT +++ HEROES  +")
      print("   =================\n")
      df = pd.read_csv('highscores.txt',names=['USERNAME','WASTE_SORTED']) # Read the high scores data from the file again
      print(df.tail(n=5))  # Display the bottom 5 scores (recent scores)
      input("\nHit enter to go back -->> ")
      os.system('cls')
      Game.main()
    if choice_highscore =='2':
      Game.main()

  def wastebook():
    os.system('cls')
    print("\n     ooo     ")
    print(" ===========")
    print("| SOS INFO  |")
    print("=============")
    print ("| Page (1)  |Story")
    print ("| Page (2)  |Info")
    print ("| Page (3)  |di pa sure. Trivas?")
    print ("| Page (4)  |Back to Menu")
    print ("| Page (5)  |Quit")
    print("=============")
    choice = input("\nEnter Page: ") # Get the user's choice of page
    while choice not in ['1', '2', '3', '4','5']: # Validate the user's choice
      print("Invalid input. Please enter 1, 2, 3, 4, or 5")
      choice = input()
    if choice == '1':
      Game.page_1_story()
    elif choice == '2':
      Game.page_2_info()
    elif choice == '3':
      Game.page_3_tips()
    elif choice == '4':
      Game.main()
    elif choice == '5':
      quit()
      
  def page_1_story(): 
    os.system('cls')
    print("Story.....\n") # Display the story
    choice_page = input("(1) Main Menu | (2) Next Page: ")  # Get the user's choice for next page or main menu
    while choice_page not in ['1','2']:  # Validate the user's choice
      print("Invalid input. Please enter 1 or 2")
      choice_page = input("(1) Main Menu | (2) Next Page: ")
    if choice_page =='1':
      os.system('cls')
      Game.main()
    if choice_page == '2':
      Game.page_2_info()
  
  def page_2_info(): 
    os.system('cls')
    print("Impact of waste on the environment.....\n") # Display information about the impact of waste on the environment
    choice_page = input("(1) Main Menu | (2) Previous Page | (3) Next Page: ") # Get the user's choice for next page, previous page or main menu
    while choice_page not in ['1','2','3']:  # Validate the user's choice
      print("Invalid input. Please enter 1, 2, 3, 4, or 5")
      choice_page = input("(1) Main Menu | (2) Previous Page | (3) Next Page: ")
    if choice_page =='1':
      os.system('cls')
      Game.main()
    if choice_page == '2':
      Game.page_1_story()
    if choice_page == '3':
       Game.page_3_tips()
      
  def page_3_tips():
    os.system('cls')
    print("Tips for reducing waste....\n") # Display tips for reducing waste
    choice_page = input("(1) Main Menu | (2) Previous Page | (3) Quit: ") # Get the user's choice for previous page, next page, or quit
    while choice_page not in ['1','2','3']: # Validate the user's choice
      print("Invalid input. Please enter 1, 2, or 3")
      choice_page = input("(1) Main Menu | (2) Previous Page | (3) Quit: ")
    if choice_page =='1':
      os.system('cls')
      Game.main()
    if choice_page == '2':
      Game.page_2_info()
    if choice_page == '3':
      quit()

#--------------------------------------------------------------------execute functions
mood() # run the "def mood()" (to give the game the feel of a game)
Game.main() # run the main screen next. its in the class Game.
