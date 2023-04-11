import random
import pandas as pd
import os 
import time 

#--------------------------------------------------------------------lists and dictionaries
waste_types = {
    "paper": "N",
    "plastic": "N",
    "glass": "N",
    "aluminum": "N",
    "electronics": "N",
    "metal": "N",
    "cigarette butts": "N",
    "toothbrushes": "N",
    "disposable razors": "N",
    "straws": "N",
    "bottle caps": "N",
    "plastic bags": "N",
    "styrofoam": "N",
    "bubble wrap": "N",
    "plastic utensils": "N",
    "tape": "N",
    "CDs and DVDs": "N",
    "printer cartridges": "N",
    "cell phones": "N",
    "batteries": "N",
    "light bulbs": "N",
    "paint": "N",
    "solvents": "N",
    "aerosol cans": "N",
    "motor oil": "N",
    "tires": "N",
    "fruit scraps": "B",
    "coffee grounds": "B",
    "tea bags": "B",
    "eggshells": "B",
    "grass clippings": "B",
    "leaves": "B",
    "tree branches": "B",
    "food waste": "B",
    "manure": "B",
    "hair and fur": "B",
    "wool clothing": "B",
    "paper napkins": "B",
    "cardboard": "N",
    "strapping": "N",
    "film plastic": "N",
    "rigid plastic": "N",
    "foam rubber": "N",
    "ceramics": "N",
    "crayons": "N",
    "cosmetics": "N",
    "dental floss": "N",
    "fire extinguishers": "N",
    "fishing line": "N",
    "floor wax": "N",
    "insecticides": "N"
}
randomquotes = [
  "Sorting trash has never been so risky!", "Breathe deep and sort fast!", "Don't let the trash choke you out!",
  "Match the garbage or face the consequences!", "Test your trash-sorting skills and (not)survive!", "Keep your oxygen above 0% and your trash sorted!",
  "Every litter bit hurts","There is no planet B","Proud people do not litter","Trash sorting is a matter of life and death!",
  "Recycle the present, save the future.","Eat, Sleep, Sort, Suffocate.","Never refuse to reuse.","Sort it out or run out of air! The clock is ticking!",
  "Sort fast, but don't make a mistake or you'll suffocate!","It's easy. Don't mess up.", "Your sacrifice is remembered",
  "Think you have what it takes to be a Trash Sorting Hero? ","The greatest threat to our planet is the belief that someone else will save it. -Robert Swan"]
randomphrase = [
  'You picked up', 'You gathered','You got your hands on','You found','You saw', 'What to do with ']
#--------------------------------------------------------------------ask_question
def ask_question():
    item = random.choice(list(waste_types.keys()))
    phrase = random.choice(list(randomphrase))
    print("===========================================")
    answer = input(f"+ {phrase} \033[32m{item}? \x1B[0m(N/B/Q): ").upper()
    print("===========================================")
    if answer =='q' or answer == 'Q':
      quit()
    if answer != waste_types[item]:
        print(f"\nThe right answer is {waste_types[item]}")
    return answer == waste_types[item]
#--------------------------------------------------------------------highscore
def highScore():
  os.system('cls')
  print("\n   =================")
  print("+  REMEMBERED HEROES  +")
  print("   =================\n")
  df = pd.read_csv('highscores.txt',names=['USERNAME','WASTE_SORTED'])
  df.sort_values(by='WASTE_SORTED',ascending=False,inplace=True)
  df.to_csv('highscorer.txt')
  print(df.head(n=5))
  print("\nThank you for your service\n")
  choice_highscore = input("\nCheck recent heroes? (1)Yes | (2)No: ")
  while choice_highscore not in ['1','2']:
    print("Invalid input. Please enter 1 or 2")
    choice_highscore = input("Check recent heroes? (1)Yes | (2)No: ")
  if choice_highscore =='1':
    os.system('cls')
    print("\n   =================")
    print("+  RECENT +++ HEROES  +")
    print("   =================\n")
    df = pd.read_csv('highscores.txt',names=['USERNAME','WASTE_SORTED'])
    print(df.tail(n=5))
    input("\nHit enter to go back -->> ")
    os.system('cls')
    main()
  if choice_highscore =='2':
    main()
#--------------------------------------------------------------------mood
def mood():
  os.system('cls')
  input("\n\"Our planet is counting on you \"")
  input("\n\"Your sacrifice will be remembered..\"")
  os.system('cls')
  input("\nYou obtained 66% oxygen.")
  os.system('cls') 
#--------------------------------------------------------------------wastebook
def page_1_story():
  os.system('cls')
  print("Story.....\n")
  choice_page = input("(1) Main Menu | (2) Next Page: ")
  while choice_page not in ['1','2']:
    print("Invalid input. Please enter 1 or 2")
    choice_page = input("(1) Main Menu | (2) Next Page: ")
  if choice_page =='1':
    os.system('cls')
    main()
  if choice_page == '2':
    page_2_info()

def page_2_info():
  os.system('cls')
  print("Impact of waste on the environment.....\n")
  choice_page = input("(1) Main Menu | (2) Previous Page | (3) Next Page: ")
  while choice_page not in ['1','2','3']:
    print("Invalid input. Please enter 1, 2, 3, 4, or 5")
    choice_page = input("(1) Main Menu | (2) Previous Page | (3) Next Page: ")
  if choice_page =='1':
    os.system('cls')
    main()
  if choice_page == '2':
    page_1_story()
  if choice_page == '3':
    page_3_idk()
    
def page_3_idk():
  os.system('cls')
  print("Tips for reducing waste....\n")
  choice_page = input("(1) Main Menu | (2) Previous Page | (3) Quit: ")
  while choice_page not in ['1','2','3']:
    print("Invalid input. Please enter 1, 2, or 3")
    choice_page = input("(1) Main Menu | (2) Previous Page | (3) Quit: ")
  if choice_page =='1':
    os.system('cls')
    main()
  if choice_page == '2':
    page_2_info()
  if choice_page == '3':
    quit()

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
  choice = input("\nEnter Page: ")
  while choice not in ['1', '2', '3', '4','5']:
    print("Invalid input. Please enter 1, 2, 3, 4, or 5")
    choice = input()
  if choice == '1':
    page_1_story()
  elif choice == '2':
    page_2_info()
  elif choice == '3':
    page_3_idk()
  elif choice == '4':
    main()
  elif choice == '5':
    quit()
#--------------------------------------------------------------------main screen
def main():
  os.system('cls')
  while True:
      print("\n    =================")
      print("++| SORT OR SUFFOCATE |++")
      print("    =================")
      print("(1) PLAY SOS")
      print("(2) SOS Lore ")
      print("(3) Highscore")
      print("(4) Quit")
      print("(5) Random Quotes\n")
      print("\"\x1B[3m" +random.choice(randomquotes)+ "\x1B[0m\"\n" )
      choice = input("Enter Choice: ")
      while choice not in ['1', '2', '3','4', '5', 'q','Q','P','p','S','s','H','h']:
        print("Invalid input. Please enter 1, 2, 3, 4, or 5")
        choice = input()
      if choice in ['1','P','p']:
        play_game()
        os.system('cls')
      elif choice == '2':
        wastebook()
        os.system('cls')
      elif choice == '3':
        highScore()
        os.system('cls')
      elif choice in ['4','q','Q']:
        quit()
      elif choice == '5':
        os.system('cls')
        main()
      else:
          break 
#--------------------------------------------------------------------play
def play_game():
  os.system('cls')
  score = 0
  print("\n    ==============================")
  print("++|  ARE YOU READY TO GO OUTSIDE? |++")
  print("   ===============================")
  press = input("\nPress (1) for Tutorial | (Enter) to Play: ")
  if press == '1':
      os.system('cls')
      print("\nYour Oxygen is at 66%")
      print("| It is slowly depleting (66 secs)." )
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
  while time.time() - start_time < 66:
      
      result = ask_question()
      if result:
          score += 1
          start_time += random.randint(1,1)
          print(f"\n\033[32mCORRECT | Trash Sorted: {score}\x1B[0m |\033[32m {round(66-(time.time() - start_time))}% oxygen remaining\x1B[0m\n")
      else:
          start_time -= random.randint(17,30)
          print(f"\n\033[31mWRONG | Trash Sorted: {score} \x1B[0m|\033[31m {round(66-(time.time() - start_time))}% oxygen remaining\x1B[0m\n")
  print("\n\n\n\n\n\n\n-----------------------------------------")     
  print(f"YOU RUN OUT OF OXYGEN! You sorted" ,score,"trash")

  if score >= 40:
    print("\"WOW! Your name is probably in the Hero list!!\"")
  elif 30 <= score < 40:
      print("\"Great job!\"")
  elif 20 <= score < 30:
      print("\"Not bad, but you..can do better...\"")
  elif 10 <= score < 20:
      print("\"I guess thank u\"")
  elif 5 < score < 10:
      print("\"we'll take it\"")
  else:
      print("\"Your sacrifice is not remembered\"")
  print("-----------------------------------------")
  while True:
    USERNAME = input("\nEnter Username (5 ABC chr):  ")
    if len(USERNAME) == 5 and USERNAME.isalpha():
      break
    else:
          print("5 ABC character only bro.. like \"JESUS\" ")
  WASTE_SORTED = score
  with open("highscores.txt", "a") as text_file:
    text_file.write("\n" + USERNAME + ','+ format(WASTE_SORTED) +"\n")
  text_file.close()
  return USERNAME, WASTE_SORTED


  
  

    
#--------------------------------------------------------------------execute functions
mood()# This is just to set the "mood" for the game, like effects. You can delete this
main() # To run the main() which is the main menu for the game. 