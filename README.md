
 
<h1>
<p align="center">
  <br>     ==================
  <br>++| SOS: SORT OR SUFFOCATE |++
  <br>   ==================
</h1>
  <p align="center">
    "Will you be remembered as a hero or will you perish in the waste"
    <br />
    </p>
</p>


---
## + About the Project
SOS is a text-based command line game created in Python. It's a simple sorting game where your mission is to identify the trash that is unlike the others in type(Biodegradable or Non-biodegradable) within a given time limit. Success in the game requires achieving a specific score. The game keeps track of high scores and features a Wastebook filled with valuable information about waste management. The game turned out to be more challenging than our initial expectations.

<img src = "https://github.com/VivieneGarcia/python_SOS/blob/main/READ%20ME%20PHOTOS/SS%20GAME.png" width=200px height=200px>

## + Main Objective
The game has been designed to promote the United Nations' **Sustainable Development Goals (SDG) 12 and 13**: Responsible Consumption and Production and Climate Action. It aims to create awareness about the importance of waste management and how small steps in our everyday life can help in reducing pollution. It aims to teach the player the art of sorting waste so perfectly that sorting itself becomes second nature.  

<img src = "https://github.com/VivieneGarcia/python_SOS/blob/main/READ%20ME%20PHOTOS/SDG12-13.png" width=500px height=250px>

### + Objective 2
This project has been designed to showcase our understanding and proficiency in Python programming by **demonstrating our knowledge of loops, data types, collections, functions, and classes**. As we delve into the development of this project, we will explore various programming concepts that we have learned so far and apply them in the context of building a  game that is both entertaining and educational. As we work on this project, we will also place a strong emphasis on **user-friendliness** and the **readbility** and **organization** of the code. The game will be designed to be intuitive and easy to use, with clear instructions. 

## + Modules Used
Make sure you have the following modules installed before running the game:
###### If you have Python3+ , you are good to go.

- os 
- time
- random

If you don't have the modules: 
- Search for "Command Propmt" on your search bar
- Then type: 
- random : ```pip install random``` 

## + How to run the program
To run the program, follow these steps:
- Download the "main.py" file.
- Open an Integrated Development Environment (IDE) such as Visual Studio Code.
- Import the necessary modules or libraries required by the program.
- Run the program by executing the "main.py" file.
- Ensure that you have Python installed on your system and that the required dependencies are available in your environment.

## + UML Diagram

<img src = "https://github.com/VivieneGarcia/python_SOS/blob/main/READ%20ME%20PHOTOS/FINAL%20UML.png" width=270px height=490px>

## + Gameplay Video 
 *(unmute for asmr) !! the sound is not included in the game*
 
https://github.com/VivieneGarcia/python_SOS/assets/129963246/9bdca9fe-3066-46d6-bfc4-fe16ef1f8ea9


## + Plans for the game
- Expansion of Waste Types and Question Types: Introduce a wider range of waste types to sort, such as recyclable, hazardous, or electronic waste. Additionally, incorporate different question types (ex. multiple choice, identification,etc.)
- Sorted Highscores for each level
- GUI (Pygame or Renpy) :)
- Add music / sound effects

## + SOS V1 versus SOS V2 (Present)

**Collection of items:**
- V1: Uses one dictionary. items = { "paper": B, "plastic": N,...} Pain-staking to type and add new items
- V2: Uses two lists.  bio = [paper, teabags,..] and non-bio = [plastic, toothbrush..] 

**Level Difficulty:**
- V1: 3 levels (Dependent Variable: time) Harder = less time. Doesn't really makes sense for the game.
- V2: 3 levels (Dependent Variable: number_of_items) Harder = more number of items

**Gameplay:**
- V1: The game presents only 1 item and you have to determine if it biodegradable or non-bio
- v2: The game presents 3 or more items, determine the item that doesn't have the same type as the others

**Level progression:**
- V1: None
- V2: increases the number of items

**User Input of the answer:**
- V1: Only 2 choices. "B" for Biodegradable, "N" for Non-Biodegradable. Prone for SPAMMING
- V2: Type the odd item. Wrong spelling is wrong. SPAM PROOF

**Storing Score:**
- V1: Has a working database using the module pandas. Extra files (.txt)
- V2: Temporarily stored in a dictionary. No extra files. Although Version 1 is more advantageous, we opt for simplicity with Version 2.

**Data Structure:**
- V1: Lacks a class structure. Display and functions are not separated.
- V2: Includes a class structure where most print displays are separated from the main functions. Better readability and organization

## + Contributors 
  Section: CS 1203
- [Viviene Marie C. Garcia (21-51308)](https://github.com/VivieneGarcia)
- [Rain Lyrra R. Panganiban (21-05880)](https://github.com/rnlyra)
- [Princess Mae L. Delos Santos (22-03579)](https://github.com/princessdlssnts)
- [Justin Mae Nuñez (22-02253)](https://github.com/jstnnz)
- [Jastine C. Corteza (20-05802](https://github.com/jasteng)

## + Acknowledgements 
We would like to express our gratitude to our Advanced Computer Programming prof, Dr. Francis Jesmar P. Montalbo, for teaching us Python programming, sharing best practices and for providing us with his helpful beginner-friendly [repository](https://github.com/francismontalbo/learning_python). His guidance have allowed us to showcase what we have learned and improve our coding skills. 

