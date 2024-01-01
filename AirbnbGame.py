# Gilbert Hernandez, IT-140
import random

def generate_airbnb_ascii():
    airbnb_ascii = [
        "      ___    _      __          __       _____                                                __                __ ",
        "     /   |  (_)____/ /_  ____  / /_     / ___/_________ __   _____  ____  ____ ____  _____   / /_  __  ______  / /_",
        "    / /| | / / ___/ __ \/ __ \/ __ \    \__ \/ ___/ __ `/ | / / _ \/ __ \/ __ `/ _ \/ ___/  / __ \/ / / / __ \/ __/",
        "   / ___ |/ / /  / /_/ / / / / /_/ /   ___/ / /__/ /_/ /| |/ /  __/ / / / /_/ /  __/ /     / / / / /_/ / / / / /_  ",
        "  /_/  |_/_/_/  /_.___/_/ /_/_.___/   /____/\___/\__,_/ |___/\___/_/ /_/\__, /\___/_/     /_/ /_/\__,_/_/ /_/\__/  ",
        "                                                                       /____/                                 "
    ]

    for line in airbnb_ascii:
        print(line)

# Call the function to generate ASCII art for "Airbnb"
generate_airbnb_ascii()

# Function to display instructions
def show_instructions():
    print("\nText-based adventure game")
    print("\nYou wake up to birds chirping and the gentle sea-breeze drifting through an open window.")
    print("\nYour tropical stay in an Airbnb bungalow is coming to an end.")
    print("\nYou and your friends have had a great time throughout the week! Too good it seems.")
    print("\nThat's because you have misplaced some belongings and need to collect 7 items from your friends to leave.")
    print("\nYour friends love Airbnb so much, they've put together a few questions for you to answer before you can retrieve each item")
    print("\nEach question wrong subtracts one Energy level. You have 4 Energy level's to help you on your journey.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'\n")


# Function to handle enemy questions
def ask_question(current_room):
    questions = {
        'Kitchen': "Celeste asks you: Did Airbnb sell potato chips during the 2008 U.S presidential election? True or false.",
        'Dining Room': "Ladaisa asks you: Is it true that the 'air' in Airbnb came from an air mattress? True or false.",
        'Front Door': "Everyone asks: Is it true that the average Hotel guest outspends an average Airbnb guest for stays? True or false.",
        'Food Storage': "William mentions: The only places Airbnb has to offer are houses and apartment rooms. True or false.",
        'Laundry Room': "Adriana says: I heard there were less than one million listings on Airbnb, is that true? True or false.",
        'Back Porch': "Reef says to you: Was there really a whole country listed on Airbnb? True or false.",
        'Living Room': "Gilbert mentions: I heard somewhere that the worlds smallest house was listed on Airbnb. True or false.",
        'Uber': "Final challenge: Do you agree that Airbnb experiences are the best part of using the platform? True or false."
    }

    success_messages = {
        'Kitchen': "Congratulations! Airbnb raised early funding by selling repackaged cereal boxes during the 2008 presidential election in the United States. The 'Obama O's' and 'Cap'n McCain's' helped the startup raise over $30,000. Celeste hands you the House keys. You may now move on.",
        'Dining Room': "Wicked good job! Founders Brian Chesky and Joe Gebbia placed an air mattress in their living room and turned the room into a bed and breakfast. Nathan Blecharczyk, Chesky's old roommate, later joined as a third co-founder in 2008, and the company was named AirBed and Breakfast. Ladaisa hands you the Wallet. You may now move on.",
        'Front Door': "Amazing! Despite 79% of guests choosing Airbnb over hotels to save money, Airbnb guests, on average, outspend hotel guests, with longer stays and higher expenditures per visit, as found in a San Francisco Airbnb research. Everyone hands you your Luggage as your cab arrives.",
        'Food Storage': "Bravo! Airbnb offers extremely unique places available to rent if you're in an adventurous mood. They have castles, beach huts, igloos, and more than two thousand tree houses currently available on the site. William hands you the Liquid IV. You may now move on.",
        'Laundry Room': "Way to go! As of June 30, 2023, Airbnb has over seven million active listings worldwide. Adriana hands you the Jacket. You may now move on.",
        'Back Porch': "Grattis! Sweden made history in 2017 when it became the first to list the whole country on the Airbnb website. Airbnb and Visit Sweden collaborated to promote Sweden's 'freedom to wander', which allows individuals to freely explore all public places around the nation. Reef hands you the Shoes. You may now move on.",
        'Living Room': "Awesome! The world's tiniest 'home' was listed on Airbnb! This one-square-meter waterproof structure in Berlin, Germany, was designed for one person and includes a bed, desk, and chair. Gilbert hands you the Phone charger. You may now move on.",
        'Uber': "Congratulations! You've completed the final challenge. You are now ready to leave with all your belongings and unforgettable memories from your Airbnb stay!"
    }

    question = questions[current_room]
    correct_answer = 'T' if current_room == 'Dining Room' or current_room == 'Living Room' or current_room == 'Back Porch' or current_room == 'Outside' else 'F'

    print(question)
    user_answer = input("Your answer (T or F): ").upper()

    while user_answer not in ['T', 'F']:
        print("Invalid input. Try again.")
        user_answer = input("Your answer (T or F): ").upper()

    if user_answer == correct_answer:
        print("Correct! " + success_messages.get(current_room, "You may now move on."))
        return True
    else:
        print("Incorrect! You lose one Energy level. Try again.")
        return False

# Main function
def main():
    show_instructions()

    # Initialize health
    Energy = 4

    # A dictionary linking a room to other rooms and linking one item for each room
    rooms = {'Master Bedroom': {'South': 'Kitchen', 'North': 'Food Storage', 'East': 'Living Room', 'West': 'Laundry Room',
                                 'item': None},
             'Kitchen': {'North': 'Master Bedroom', 'East': 'Dining Room', 'item': 'House keys', 'enemy_completed': False},
             'Dining Room': {'West': 'Kitchen', 'item': 'Wallet', 'enemy_completed': False},
             'Front Door': {'South': 'Living Room', 'North': 'Outside', 'item': 'Luggage', 'enemy_completed': False},
             'Food Storage': {'West': 'Back Porch', 'South': 'Master Bedroom', 'item': 'Liquid IV', 'enemy_completed': False},
             'Laundry Room': {'East': 'Master Bedroom', 'item': 'Jacket', 'enemy_completed': False},
             'Back Porch': {'East': 'Food Storage', 'South': 'Front Door', 'item': 'Shoes', 'enemy_completed': False},
             'Living Room': {'West': 'Master Bedroom', 'North': 'Front Door', 'item': 'Phone charger', 'enemy_completed': False},
             'Uber': {'South': 'Front Door', 'item': None, 'enemy_completed': False}
             }

    current_room = 'Master Bedroom'
    inventory = []

    while True:
        print("\nYou are in the", current_room)

        if all('enemy_completed' in rooms[room] and rooms[room]['enemy_completed'] and rooms[room]['item'] is None for
               room in rooms):
            if current_room == 'Uber':
                if len(inventory) == 7:
                    print(
                        "\nCongratulations! You have collected all items, answered all questions, and had an amazing holiday with Airbnb!")
                    break
                else:
                    print(
                        "\nYou left without collecting all of your belongings. Looks like that next holiday is coming sooner than expected!")
                    break
        elif current_room == 'Uber':
            if len(inventory) == 7:
                print(
                    "\nCongratulations! You have collected all items, answered all questions, and had an amazing holiday with Airbnb!")
            else:
                print(
                    "\nYou left without collecting all of your belongings. Looks like that next holiday is coming sooner than expected!")
            break

        if rooms[current_room]['item'] is not None and not rooms[current_room].get('enemy_completed', False):
            print("You see your", rooms[current_room]['item'])
            # Check if the enemy question is already completed
            if not ask_question(current_room):
                Energy -= 1
                print(f"Energy level remaining: {Energy}")
                if Energy == 0:
                    print("You ran out of Energy! Looks like you have to try again tomorrow!")
                    break
                continue
            inventory.append(rooms[current_room]['item'])
            rooms[current_room]['item'] = None
            rooms[current_room]['enemy_completed'] = True
        else:
            print("Item collected or nothing in this room")

        print("Inventory:", inventory)
        print(f"Energy level remaining: {Energy}")

        direction = input("Direction to move? (East, West, North, South): ").title()
        directions = list(rooms[current_room].keys())
        directions.remove('item')
        while direction not in directions:
            print("Invalid direction from " + current_room + ". Try again")
            direction = input("Direction to move? (East, West, North, South): ").title()

        next_room = rooms[current_room][direction]
        print("You have just moved to", next_room)
        print("------------------------------------------------")

        current_room = next_room

    print("\nGame over!")


# Call the main function
main()

