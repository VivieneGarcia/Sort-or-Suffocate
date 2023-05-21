
import random
import os 
import time 

#HEADS UP:  The "\033[34m", "\x1B[0m" or anything similar is to change some text's color. 


def clear_screen():
  os.system("cls" if os.name == "nt" else "clear") 


def quit():
  print("    \n    ================================")
  print("++| Thanks for playing SOS! See ya! |++")
  print("    ================================\n")
  exit()  
 
 
def effects(): 
  clear_screen() 
  input("\n\"Our planet is counting on you\"")
  input("\n\"Your sacrifice will be remembered..\"")
  clear_screen()
  input("\nYou obtained an oxygen tank.")
  clear_screen()  


class Game:
  def __init__(self):
      self.player_score = { 
        "Vivss":2,
        "RAINL":40,
        "PRNCS":33,
        "JSTIN":26,
        "JASTN":29 }    
      self.biodegradable = [ 
        'paper', 'fruit scraps', 'coffee grounds', 'tea bag', 'eggshell',
        'grass clipping', 'leaves', 'tree branches', 'food waste', 'manure',
        'hair and fur', 'wool clothing', 'paper napkins','cardboard']
      self.non_biodegradable = [ 
        'plastic', 'glass', 'aluminum', 'electronic', 'metal', 'cigarette butt',
        'toothbrushes', 'disposable razors', 'straws', 'bottle caps', 'plastic bag',
        'styrofoam', 'bubble wrap', 'plastic utensils', 'tape', 'CDs and DVDs',
        'printer cartridge', 'cell phones', 'batteries', 'light bulbs', 'paint',
        'solvents', 'aerosol can', 'motor oil', 'tires', 'strapping']
      self.random_quote = [ 
      "Breathe deep and sort fast!",
      "Don't let the trash choke you out!",
      "Keep your oxygen above 0% and your trash sorted!",
      "Every litter bit hurts",
      "There is no planet B",
      "Proud people do not litter",
      "Trash sorting is a matter of life and death!",
      "Eat, Sleep, Sort, Suffocate.",
      "Never refuse to reuse.",
      "The greatest threat to our planet is the belief that someone else will save it. -Robert Swan"]
      self.random_phrase = [ 
      'You picked up', 
      'You gathered',
      'You got your hands on',
      'You found',
      'You saw',
      'What to do with ']
  
  
  def display_main(self):
        clear_screen()
        print("\n    =================")
        print("++| SORT OR SUFFOCATE |++")
        print("    =================")
        print("(1) PLAY SOS")
        print("(2) Wastebook")
        print("(3) Highscore")
        print("(4) Quit")
        print("(5) Random Quotes\n")
        print("\"\x1B[3m" + random.choice(self.random_quote) + "\x1B[0m\"\n")   
         
  
  def main(self):
      clear_screen()
      
      while True: 
        
          self.display_main()
          
          choice = input("Enter Choice: ")
          
          while choice not in ['1', '2', '3','4', '5']:
            print("Invalid input. Please enter 1, 2, 3, 4, or 5")
            choice = input("Enter Choice: ")
          if choice == '1':
            self.play_menu() 
          elif choice == '2':
            self.wastebook() 
          elif choice == '3':
            self.high_score() 
          elif choice == '4':
            quit()
          elif choice == '5':
            self.main() 
          else:
              break 


  def play_menu(self):
      clear_screen()
      
      print("       ============")
      print ("   ++| Select LEVEL |++")
      print("       ============")
      print("\n+=========================+")
      print(" [1] Light, but scarce")
      print(" [2] Middle, and steady")
      print(" [3] Heavy, but rewarding")
      print("+=========================+")
      print(" [4] Main Menu")
      
      level = input("\n Enter Choice: ")
      while level not in ['1', '2', '3','4']:
        print("\nInvalid input. Please enter 1, 2, or 3")
        level = input("\n Enter Choice: ")
        
      if level == '3':
          self.number_of_items = 4
          self.point = 3
          self.cap_points = 9
          self.display_start_game()
          
      elif level == '2':
          self.number_of_items = 3
          self.point = 2
          self.cap_points = 6
          self.display_start_game()
          
      elif level == '1':
          self.number_of_items = 2
          self.point = 1
          self.cap_points = 3
          self.display_start_game()  
          
      elif level == '4':
          self.main()
    
    
  def display_start_game(self):
      clear_screen()
      print("\n    ==============================")
      print("++|  ARE YOU READY TO GO OUTSIDE? |++")
      print("   ===============================")
      
      press = input("\nPress (1) for Tutorial | (Enter) to Play: ")
      if press == '1': 
        
        self.display_tutorial()   
          
      self.start_game() 
  
  
  def display_tutorial(self):
        clear_screen()
        print("\nYour Oxygen is at 66%")
        print("| It is slowly depleting.")
        print("| There are 2 types of trash, Biodegradable and Non-biodegradable.")
        print("| You have to pick the trash that is unlike the others in type")
        print("| One wrong move, it will dwindle faster")
        print("| Make sure to reach 27 pts to live!")
        print("| if it reaches 0 % ....")
        print("| Goodluck, OP.")
        print("==============================")
        print("| Type the ODD trash out      |")
        print("| This is spelling-sensitive  |")
        print("| Type [1] to go back to Main |")
        print("==============================")
        print("Press Enter to play")
        input()  
          
       
  def start_game(self):
      clear_screen()
      
      score = 0
      timer = 66
      win_score = 27
      
      start_time = time.time()
      while  time.time() - start_time < timer and score < win_score : 
        
          chosen_list = random.choice([self.biodegradable, self.non_biodegradable])
          chosen_trash = random.sample(chosen_list, self.number_of_items)
          other_list = self.biodegradable if chosen_list == self.non_biodegradable else self.non_biodegradable
          other_trash = random.choice(other_list)
          options = chosen_trash + [other_trash]
          random.shuffle(options)
          
          items = (" , ".join(options))
          phrase = random.choice(self.random_phrase)
          
          print("+======-------")
          print(f"+ {phrase} \033[34m{items} \x1B[0m?")
          print("+======--------")
          
          user_choice = input("Enter the Odd trash: ").lower()
          
          time_left = round(timer-(time.time() - start_time))
          
          if user_choice =='1':
            self.main()
            
          if user_choice.lower() == other_trash.lower():
              score += self.point
              timer += 3
              print(f"\n\033[32mCORRECT | Trash Sorted: {score}\x1B[0m |\033[32m {time_left}% oxygen remaining\x1B[0m\n")
              
              if score % int(self.cap_points) == 0:
                  self.number_of_items += 1
              
          else:
              time_reduction = random.randint(10, 15)
              timer -= time_reduction
              print(f"\n\033[31mit's {other_trash} | Trash Sorted: {score} \x1B[0m|\033[31m {time_left}% oxygen remaining\x1B[0m\n")
            
      if score >= win_score: 
        self.display_game_win(score)
        username = self.get_username()
        self.player_score[username] = score
        
      else:
        self.display_game_over(score) 
        username = self.get_username()
        self.player_score[username] = score
      
      
  def display_game_win(self, score):
        print("\n\n\n\n\n\n\n----------------------------------------")    
        print(f"You got", score ,"points. You reached the top!")
        print("Very Impressive. You've earned another day") 
        print("Here's another oxygen tank. See ya! ")
        print("------------------------------------------------")  
        
        
  def display_game_over(self, score):
        print("\n\n\n\n\n\n\n-----------------------------------------")
        print(f"YOU RUN OUT OF OXYGEN! You picked out", score, "odd trash") 
        if 20 <= score < 27:
            print("\"So close. We hope to find someone like you again.\"")
        elif 15 <= score < 20:
            print("\"Not entirely hopeless... There's a faint glimmer of wasted potential.\"")
        elif 11 <= score < 15:
            print("\"We'll take it. Thank you for your sacrifice.\"")
        elif 6 <= score < 11:
            print("\"Barely worth salvaging. You're destined to be consumed by the trash.\"")
        elif 3 < score < 6:
            print(f"\"huh? Only", score, "trash? really?\"")
        else:
            print("\"Your demise is inevitable.\"")
        print("-----------------------------------------") 
        
        
  def get_username(self):
      while True: 
        username = input("\nEnter Username (5 ABC chr):  ") 
        if len(username) == 5 and username.isalpha(): 
          break
        else:
              print("5 ABC character only bro.. like \"JESUS\" ")
      return username
    
    
  def high_score(self):
      clear_screen()
      sorted_scores = sorted(self.player_score.items(), key=lambda x: x[1], reverse=True)
    
      print("\n   =================")
      print("+    TOP ++ HEROES    +")
      print("   =================\n")
      print("+=====================+")
      for rank, (name, score) in enumerate(sorted_scores[:5], start=1):
          print(f"   Rank {rank} | {name}: {score}")
      print("+=====================+")
      input("\nHit enter to go back -->> ")     
  

  def wastebook(self):
      clear_screen()
      print("\n     ooo     ")
      print(" ===========")
      print("| SOS INFO  |")
      print("=============")
      print ("| Page (1)  |SOS LORE")
      print ("| Page (2)  |Impact of Waste")
      print ("| Page (3)  |Tips for a Green Planet")
      print ("| Page (4)  |Back to Menu")
      print ("| Page (5)  |Quit")
      print("=============")
      choice = input("\nEnter Page: ") 
      while choice not in ['1', '2', '3', '4','5']:
        print("Invalid input. Please enter 1, 2, 3, 4, or 5")
        choice = input()
      if choice == '1':
        self.page_1_story()
      elif choice == '2':
        self.page_2_info()
      elif choice == '3':
        self.page_3_tips()
      elif choice == '4':
        self.main()
      elif choice == '5':
        quit()
      
      
  def page_1_story(self): 
      clear_screen()
      print("Story: \n") 
      print("\nIt is 2050. Earth is on the verge of collapse due to excessive pollution and waste.")
      print("The air has become toxic, and humans must wear oxygen tanks to survive.")
      print("As a last-ditch effort, the government has developed a strict SOS system to control the resources left")
      print("You find yourself among the unfortunate ones, forced to participate in the SOS")
      print("Your mission is simple, to pick the trash that is unlike the others in type.")
      print("Every correct answer earns you points, but every mistake costs you oxygen.  ")
      print("It becomes evident that the government's true motive is twofold:")
      print("cleaning the Earth and reducing the human population to secure more oxygen for themselves. ")
      print("Sort as much trash as you can before your oxygen runs out and help save Earth!")
      
      choice_page = input("\n(1) Main Menu | (2) Next Page: ") 
      while choice_page not in ['1','2']: 
        print("Invalid input. Please enter 1 or 2")
        choice_page = input("(1) Main Menu | (2) Next Page: ")
      if choice_page =='1':
        clear_screen()
        self.main()
      if choice_page == '2':
        self.page_2_info()


  def page_2_info(self): 
      clear_screen()
      message = """Impact of waste on the environment.....
      In recent years, environmental concerns regarding garbage and \nits effects have grown. This game aims to raise awareness of \nthe damaging impacts of waste on the environment and to underline \nthe urgent need for sustainable waste management techniques.\n
      Some of the damaging effects of waste on our environment are: \n
      Land & Soil Pollution:
      Improper waste disposal, particularly non-biodegradable \nmaterials such as plastics, poses a significant threat to \nland and soil.\n
      Water Contamination:
      Waste mismanagement directly impacts water bodies, causing \nsevere pollution.\n
      Air Pollution & Climate Change:
      Waste incineration and open burning release harmful gases \nand particulate matter into the air, contributing to air pollution.\n
      Biodiversity Loss:
      Improper waste disposal practices, especially in natural \nhabitats and protected areas, pose a grave threat to biodiversity\n"""
      print(message)
      
      choice_page = input("(1) Main Menu | (2) Previous Page | (3) Next Page: ")
      while choice_page not in ['1','2','3']: 
        print("Invalid input. Please enter 1, 2, 3, 4, or 5")
        choice_page = input("(1) Main Menu | (2) Previous Page | (3) Next Page: ")
      
      if choice_page =='1':
        clear_screen()
        self.main()
      if choice_page == '2':
        self.page_1_story()
      if choice_page == '3':
        self.page_3_tips()
        
      
  def page_3_tips(self):
      clear_screen()
      message = """Tips for reducing waste....\n
Proper waste management is essential to minimize the \nnegative impact on the environment. Here are some \ntips to help you practice effective waste management:\n
Reduce, Reuse, Recycle: 
Purchase only what you need, repurpose items whenever \npossible, and keep recyclable materials separate \nfrom general waste.\n
Compost: 
Set up a compost bin to decompose organic materials \nand use it as nutrient-rich soil for gardening.\n
Responsible Disposal: 
Dispose hazardous waste (batteries, electronics, \nchemicals, etc.) properly to prevent contamination.\n
Adopt Sustainable Practices: 
Use eco-friendly alternatives and encourage responsible \nwaste management.\n
Participate in Community Initiatives: 
Join local cleanup efforts and support recycling programs.\n
Remember, effective waste management begins with \nindividual actions. By incorporating these tips into \nyour daily life, you can contribute to a cleaner, healthier \nenvironment for present and future generations.\n"""
      print(message)
      choice_page = input("(1) Main Menu | (2) Previous Page | (3) Quit: ") 
      while choice_page not in ['1','2','3']:
        print("Invalid input. Please enter 1, 2, or 3")
        choice_page = input("(1) Main Menu | (2) Previous Page | (3) Quit: ")
      
      if choice_page =='1':
        clear_screen()
        self.main()
      if choice_page == '2':
        self.page_2_info()
      if choice_page == '3':
        quit()


if __name__ == '__main__':
    effects()
    game = Game()
    game.main()
