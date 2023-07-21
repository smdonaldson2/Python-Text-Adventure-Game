import time,random,os
rooms = (1,2,3,4,5)
rooms_visited = []

chocolate_total = 2

def main():
    choice = play_game()
    while True:
        if choice == '1':
            choice = entrance_way()
        elif choice == '2':
            choice = cafeteria()
        elif choice == '3':
            choice = library()
        elif choice == '4':
            choice = computer_lab()
        elif choice == '5':
            choice = resource_room()
        elif choice == '6':
            choice = office()
        else:
            break


    print("Thank you for playing! " )



def play_game():
    print("""
Hello and welcome to the Elementary School!
In each room, you will be told which directions you can go.
You can move throughout the school by typing the available letters
You are a teacher and your goal is to visit every room having a positive
chocolate rating. If you don't, you lose.

type Q to end the program.
type S to start the game""")

    while True:
        choice = input("Enter your choice\n>> ").upper()
        if choice in ["S","Q"]:
            break
        else:
            ("Please enter a valid choice: 'S' or 'Q'\n")
    if choice == 'S':
        return '1'
    else:
        return 'Q'


def print_room_header(room):
    line = '=' * 25
    print(f'\n{line}{room}{line}')

def check_chocolate():
    global chocolate_total, rooms, rooms_visited
    if set(rooms) == set(rooms_visited):
        if chocolate_total > 0:
            print("Congrats, you win!")
            os._exit(0)
        else:
            print("Sorry, you loose /n:(")



def entrance_way():
    global chocolate_total, rooms, rooms_visited
    print_room_header("Entrance Way")
    print("""
You are an elementary school teacher entering school for the day.
You go to the Secretary's desk in the plaza of the school.
They have chocolate on their desk, however they look crabby.
Type s to try to sneak a chocolate.
Then type N after to go into the school.

    \n""")
    option = input('Select S to try to sneak a chocolate.\n>> ').upper()
    if option == 'S':
        print('Sneaking chocolate')
        time.sleep(2)
        if random.randint(1,2) == 1:
            print("You snuck a chocolate")
            chocolate_total += 1

        else:
            print("You weren't able to sneak a chocolate")
    while True:
        choice = input("Enter N to enter the school\n>> ").upper()
        if choice in ['N','Q']:
            if 1 in rooms_visited:
                break
            else:
                rooms_visited.append(1)
                check_chocolate()
            break
        else:
            print("Please enter a valid choice\n")
    if choice == 'N':
        return '2'
    else:
        return 'Q'


def cafeteria():
    global chocolate_total, rooms, rooms_visited
    print_room_header("Cafeteria")
    print("""
You are in the cafeteria of your school.
It reeks of poop and dead mice, which likely explains todays mystery meat.
Suddenly a toothless lunch lady grabs you. They say you must answer their riddle.\n""")
    while True:
        time.sleep(2)
        print('"You will always find me in the past. I can be created in the present, But the future can never taint me. What am I?"')
        answer = input("Your answer:\n>> ").lower()
        if answer in ['history']:
            print('The lunch lady gives you a chocolate!')
            chocolate_total += 1
            time.sleep(2)
            break
        else:
            print('The evil lunch lady snatches two of your chocolates!')
            chocolate_total -= 2
            time.sleep(2)
            break

    print("""
Now that you have dealt with the lunch lady, you can move on.
You can go to the Library by entering L
Computer Lab by entering C
Entrance way by entering E
or Resource Room by entering R""")
    choice = input("What is you choice?\n>>").upper()
    if choice in ['Q','L','E','C','R']:
        if 2 in rooms_visited:
            pass
        else:
            rooms_visited.append(2)
            check_chocolate()
        pass
    else:
        print("You can't go that way.\n")
    if choice == 'L':
        return '3'
    elif choice == 'E':
        return '1'
    elif choice == 'C':
        return '4'
    elif choice == 'R':
        return '5'
    else:
        return 'Q'




def library():
    global chocolate_total, rooms, rooms_visited
    print_room_header("Library")
    print("""
You enter the libray, and oh no! The librarians are being overwhelmed with flies.
You grab a fly swatter and try to help out.\n """)
    time.sleep(2)
    print("""
You and the libraians have nearly got them all\n""")
    time.sleep(2)
    print("""
There is one last fly. It is the biggest one you've ever seen.
The librarians looks scared and run for their lives.
However, you're brave so you take one swing at it\n""")
    time.sleep(2)
    while True:
        if random.randint(1,2) == 1:
            print("You killed the fly!")
            print("The librarians give you a chocolate!")
            chocolate_total += 1
            break
        else:
            print("""
You weren't able to get it! The fly knocks a chocolate out of your
hand and a student walking into the library steps on it.
You try again to get it.\n""")
            time.sleep(2)
            if random.randint(1,3) != 1:
                print("""
You got the fly! The Librarian's come out of their hiding place
and they reward your heroics with chocolate.
You can now continue with your quest!\n""")
                time.sleep(2)
                chocolate_total += 1
                break

            else:
                print("""
You still weren't able to get it!
The fly knocked two more chocolates out of your bag and they
fall into an a/c vent!
You take a jump off the librarians desk and you get the fly finally!
That took a long time, you better move on.\n""")
                time.sleep(2)
                break

    print("""
You can enter the computer lab by entering C
or Go back to the cafeteria with F
or vist the office with O\n
    """)
    time.sleep(2)
    c = input("Enter in your choice\n>>").upper()
    if c in ['Q','F','C']:
        if 3 in rooms_visited:
            pass
        else:
            rooms_visited.append(3)
            check_chocolate()
        pass
    else:
        print("You can't go that way.\n")
    if c == 'F':
        return '2'
    elif c == 'C':
        return '4'
    elif c == 'O':
        return '6'
    else:
        return 'Q'



def computer_lab():
    global chocolate_total, rooms, rooms_visited
    print_room_header("Computer Lab")
    print("""
You have entered the Computer Lab.
Here, you see a student struggling.
They ask you if Tuples are mutable or immutable
Enter I if you want to tell the student their immutable
Enter M if you want to tell the student their mutable""")
    time.sleep(2)
    while True:
        c = input('\n>>').upper()
        if c == 'I':
            print("""
You are correct. The student submits their assigment on the computer
and got the question correct. They are very pleased and give you a chocolate!""")
            chocolate_total += 1
            time.sleep(2)
            break
        else:
            print("""
You tell the kid that Tuples are mutable. They get the question wrong and they are mad.
You give them three chocolates to calm them down :(\n""")
            chocolate_total -= 3
            time.sleep(2)
            break
    print("""
You can go to the Library with L
Entrance Way with E
Cafeteria with C
Office with )""")
    choice = input('\n>>').upper()
    if choice in ['Q','L','E','C']:
        if 4 in rooms_visited:
            pass
        else:
            rooms_visited.append(4)
            check_chocolate()
        pass
    else:
        print("You can't go that way.\n")

    if choice == 'L':
        return '3'
    elif choice == 'E':
        return '1'
    elif choice == 'C':
        return '2'
    elif choice == 'O':
        return '6'
    else:
        return 'Q'



def resource_room():
    global chocolate_total, rooms, rooms_visited
    print_room_header("Resource Room")
    print("""
You have entered the resource room. You can smell chocolate.
Time to search for it\n>>""")
    time.sleep(2)
    while True:
        if random.randint(1,3) != 1:
            print("You found a chocolate")
            time.sleep(2)
            print("The package looks a little roughed up, but you're hungry so you eat it.")
            time.sleep(2)
            if random.randint(1,4) == 1:
                print("You eat it and after chewing you get sick instantly")
                chocolate_total -= 2
                break
            else:
                print("You get a chocolate!\n")
                chocolate_total += 1
                break
        else:
            time.sleep(2)
            print("You didn't find anything, time to move on!")
            break


    print("""
You can input L to go the library
C to go to the Cafteria
and O to go to the Office""")
    a = input('\n>>').upper()
    if a in ['Q','L','O','C']:
        if 5 in rooms_visited:
            pass
        else:
            rooms_visited.append(5)
            check_chocolate()
    else:
        print("You can't go that way.\n")
    if a == 'L':
        return '3'
    elif a == 'O':
        return '6'
    elif a == 'C':
        return '2'
    else:
        return 'Q'

def office():
    global chocolate_total, rooms, rooms_visited
    print_room_header("Office")
    print("""
You enter the office of the school. The principal is a chocolate
appendict and many their hungry!
They take three of your chocolates and tell you that they will eat them unless
you can tell them the answer to their riddle:


Why Was six afraid of seven?

Because seven _____ nine
(You type what should be in the blank)\n>>""")
    while True:
        time.sleep(2)
        a = input("What is your answer?\n>>").lower()
        if a in ['eight','8']:
            time.sleep(2)
            print("""
You are correct. The principal gives back your chocolate and one more to be nice.
It is a stressful year and he apologizes for taking your chocolate""")
            chocolate_total += 4

        else:
            print("""
You are wrong. The principal eats all of your chocolate. He even makes you throw the rappers away. What a monster.""")
            chocolate_total -= 3
            time.sleep(2)
            print("""
Despite being mad, you wish the principal well and go on your day.""")
        break

    print("You can go to the Library with L, Cafeteria with C and Entrance Way with W")
    e = input('\n>>').upper()
    if e in ['Q','L','W','C']:
        if 6 in rooms_visited:
            pass
        else:
            rooms_visited.append(6)
            check_chocolate()
        pass
    else:
        print("You can't go that way.\n")
    if e == 'L':
        return '3'
    elif e == 'W':
        return '1'
    elif e == 'C':
        return '2'
    else:
        return 'Q'

main()














