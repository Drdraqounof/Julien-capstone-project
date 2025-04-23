"""
Data Structures
Student Project
Project Title:
"""
#Import#
import requests
import pp
#intro#
print("Hello I am the DnD Dictinary")

# URL DND #
url = "https://www.dnd5eapi.co/api/2014/"

#DnD race dictionaries for user [print] inputs/ if wrong inputs/ to add lore to DnD race print
races = {
    "dwarf": "Tank +2 Constitution, Hardy stoic folk who value tradition, family, and craftsmanship, especially in metal and stone. \nThey often live in mountain fortresses or underground cities. Known for their skill in mining, forging, and brewing, as well as their resilience and stubbornness.",
    "elf": "Agile +2 Dexterity, Graceful, long-lived humanoids deeply connected to nature and magic. \nThey are often seen as wise and possessing a refined culture, with a love for art, music, and arcane knowledge. They can be aloof and view the shorter-lived races with a sense of detachment.",
    "halfling": "Short +2 Dexterity, +1 Luck Small, cheerful, and nimble folk known for their love of comfort, good food, and simple pleasures. \nThey are often homebodies but possess a strong sense of community and loyalty. Despite their size, they can be surprisingly brave and resourceful, often relying on stealth and cunning.",
    "human": "Adaptive +1 to all ability scores or a variant human option with +1 to two ability scores,  Adaptable, ambitious, and diverse, humans are found in nearly every corner of the world. \nThey lack the inherent magical abilities or strong racial traits of other races but make up for it with their versatility, drive, and capacity for innovation. Their cultures and societies are incredibly varied.",
    "dragonborn": "Dragonkin +2 Strength, +1 Charisma Humanoids with draconic ancestry, often proud and honorable. \nThey possess a breath weapon based on their dragonic heritage (acid, cold, fire, lightning, or poison) and have resistance to that damage type. Their appearance can vary depending on their draconic ancestor, with scales and vestigial horns and tails.",
    "half-Elf": "Magic touchedn +2 Charisma, and +1 Inheriting traits from both their elven and human parents, half-elves are often seen as having the best of both worlds: the curiosity and ambition of humans mixed with the refined senses and long lifespans of elves. \nThey often feel like they belong to neither world fully and can be adaptable and charismatic.",
    "half-Orc": "Brutes +2 Strength, +1 Constitution, Bearing the blood of both orcs and humans, half-orcs often face prejudice but are known for their strength, determination, and resilience. They can be fierce warriors and often have difficulty fitting into either human or orc societies, forging their own paths through strength and willpower.",
    "tiefling": "Fae +2 Charisma, +1 Intelligence, Humanoids with infernal ancestry, often marked by horns, tails, and sometimes glowing eyes or a reddish skin tone. They have a natural affinity for magic and the darker arts and often face suspicion and fear from others due to their heritage. Despite this, they can be individuals of great intellect and charisma.",
}

class_names = {
    'barbarian', 
    'bard', 
    'cleric', 
    'druid', 
    'fighter', 
    'monk', 
    'paladin', 
    'ranger', 
    'rogue', 
    'sorcerer',
    'warlock', 
    'wizard',
}
user_class = []

while True:
    user_input = input("\nDo you wish see to access the DnD database (yes/no): ")

    # User_iput YES #
    if user_input == "yes":
        print("\nLOADING LEVEL....")
        print("\nRolling dice....🎲")
        print("\nFetching DnD data...🏹⚔️")
        
        
        response = requests.get(url) 
        if response.status_code == 200:
            print("\nConnected to DnD API!")
            input("\nDungeons & Dragons (D&D) is a tabletop role-playing game where players create characters and embark on adventures in a fantasy world. One player acts as the Dungeon Master (DM), guiding the story, controlling non-player characters, and determining the outcomes of player actions, often resolved by rolling dice. It's a collaborative storytelling experience where imagination and teamwork are key to overcoming challenges and having fun. \n[press enter]")
##          
        #input("\nDo you wish to see [classes/races/DnD facts]")
        # Load DnD class options in api database #
        print("\nWe will now start going down a list from classes to races to DnD facts")
        input("[Press enter]")
        classes_response = requests.get(url + "classes/")
        if classes_response.status_code == 200:
            classes_data = classes_response.json()
            
            # For loop for looping inside dic(classess_data) #
            # Classe is DIC, classess_data is list #
            for classe in classes_data ["results"]:
                print("\nThese are the available classes in the DnD database:")
                #pp(classes_data ["results"][0]["name"])
                print(classe["name"], end="\n")
            
            #Show DnD race on screen#
            #print("\nThese are the available classes in the DnD database:", [cls["name"] for cls in classes_data["results"]])
            
            #show class choice#
            while True:
                user_class = input("\nPlease choose a class: ").lower()
            
                #if user [class] in dictionaries print stats and lore#
                if user_class in class_names:
                    print("\nGreat choice! You are now a", [user_class] ,"best of luck")
                    print()
                    break
                
                else:
                    print("This is not within the DnD database")
        
        # load DnD race options in api database #
        race_response = requests.get(url + "races/")
        if race_response.status_code == 200:
            race_data = race_response.json()
            for race in race_data ["results"]:
                print("\nThese are the available race in the DnD database:")
                #pp(race_data ["results"])
                print(race["name"], end="\n")
           
                
                
            #Show DnD race on screen#
           # print("\nThese are the available races in the DnD database:", [cls["name"] for cls in race_data["results"]])
            while True:
                user_race = input("\nPlease choose a race: ").lower()
            
                #if user [race] in dictionaries print class and lore#
                print("\nYou have chosen the race: ", [user_race])
                if user_race in races:
                    print(races[user_race])
                    break
                
                else:
                    print("\nThat is not within the DnD database")
                    
    
    # User_iput NO #        
    elif user_input == "no":
        print("\nOkay see next time, may we go on to have a grand adventure!")
        break