#Jordan McWilliams///Walker Williams
#Nov 16, 2022
#Random Restaurant Algorithm
import random
import sys

def restaurants(filename): #creates lines in a file to each be a list and removes \n
    pos1 = -1
    pos2 = -1
    lst = []
    mode = 'r'
    testing = open(filename,mode)
    for i in testing.readlines(): #goes through lines of file and makes them lists
        x = list(i)
        x.remove('\n') #removes all new lines
        x = ''.join(x)
        x = [x]
        for i in x:
            e = i.split()
            lst = lst + [e]
    for i in lst: 
        pos1 = pos1 + 1 
        pos2 = -1
        for word in i:     #jumps into our list and filters into segments of it
            pos2 = pos2 + 1
            for char in word:
                if char == '~': #this whole area so we can remove our ~ 'They act like spaces in our file'
                    word1 = word.replace('~',' ')
                    if word not in lst[pos1]:
                        continue
                    else:
                        lst[pos1].remove(word)
                        lst[pos1].insert(pos2,word1)
    testing.close()
                        
    return lst



def welcome():
    print('Welcome to our Randomized Restaurant Algorithm!\n')

def inputs():
    ohio = []
    randomization = ''
    #location = ''
    time = '' #0            these are positions for later on
    experience = '' #1
    price = '' #2
    food = '' #3

    #Location                        decided to remove location
    #print('''\t\tLocation:
#\tA) Riverpark Campus
#\tB) Main Campus\n''')
    #while location not in ['A','B']:
        #location = input('Please choose from the above options (A or B): ')
        #if location == 'A':
            #choice1 = 'Riverpark Campus'
            #ohio.append(choice1)
        #elif location == 'B':
            #choice1 = 'Main Campus'
            #ohio.append(choice1)
        #else:
            #print(f'Sorry, {location} is not a valid option.')

    #Random or No
    print('''\n\t\tRandom:
\tA) 100% randomized
\tB) Randomized from preferences\n''')
    while randomization not in ['A','B','a','b']:
        randomization = input('Please choose from the above options on how you would like this program to run (A or B): ')
        if randomization in ['A','a']:
            CLEAR = 1
        elif randomization in ['B','b']:
            CLEAR = 0
        else:
            print(f'Sorry, {randomization} is not a valid option.')
    
    if CLEAR == 0:
        #Meal Times
        print('''\n\t\tMeal Time:
\tA) Breakfast
\tB) Lunch
\tC) Dinner\n''')
        while time not in ['A','B','C','a','b','c']:
            time = input('Please choose from the above options (A, B, or C): ') #gaining information from user
            if time in ['A','a']:
                choice2 = 'Breakfast'
                ohio.append(choice2)
            elif time in ['B','C','b','c']: #this is not a mistake we decided to create the illusion of lunch and all dinner options in our database are actually Lunch and Dinner
                choice2 = 'Dinner'
                ohio.append(choice2)
            else:
                print(f'Sorry, {time} is not a valid option.') #if fail they are re-asked

        #Experience
        print('''\n\t\tExperience:
\tA) Fast Food
\tB) Restaurant\n''')
        while experience not in ['A','B','a','b']:
            experience = input('Please choose from the above options (A or B): ')
            if experience in ['A','a']:
                choice3 = 'Fast Food'
                ohio.append(choice3) #appending inputs to list
            elif experience in ['B','b']:
                choice3 = 'Restaurant'
                ohio.append(choice3)
            else:
                print(f'Sorry, {experience} is not a valid option.')
    
        #Price
        print('''\n\t\tPrice:
\tA) Low-Price
\tB) Mid-Price
\tC) High-Price\n''')
        while price not in ['A','B','C','a','b','c']:
            price = input('Please choose from the above options (A, B, or C): ')
            if price in ['A','a']:
                choice4 = 'Low-Price'
                ohio.append(choice4)
            elif price in ['B','b']:
                choice4 = 'Mid-Price' #appending inputs to list
                ohio.append(choice4)
            elif price in ['C','c']:
                choice4 = 'High-Price'
                ohio.append(choice4)
            else:
                print(f'Sorry, {price} is not a valid option.')

        #Food
        if choice2 != 'Breakfast': #if breakfast skip bc you are getting breakfast food
            print('''\n\t\tFood:
\tA) American
\tB) Mexican
\tC) Italian
\tD) Chinese
\tE) Seafood
\tF) Japanese\n''')
            while food not in ['A','B','C','D','E','F','a','b','c','d','e','f']:
                food = input('Please choose from the above options (A, B, C, D, E or F): ')
                if food in ['A','a']:
                    choice5 = 'American'
                    ohio.append(choice5)
                elif food in ['B','b']:
                    choice5 = 'Mexican'
                    ohio.append(choice5)
                elif food in ['C','c']:               #appending inputs to list
                    choice5 = 'Italian'
                    ohio.append(choice5)
                elif food in ['D','d']:
                    choice5 = 'Chinese'
                    ohio.append(choice5)
                elif food in ['E','e']:
                    choice5 = 'Seafood'
                    ohio.append(choice5)
                elif food in ['F','f']:
                    choice5 = 'Japanese'
                    ohio.append(choice5)
                else:
                    print(f'Sorry, {food} is not a valid option.')

        return ohio #our final list filled with preferences
        
    elif CLEAR == 1:
        return CLEAR

def program(restaurant_list,preferences):
    lst1 = [] #this works as a filter making sure the resturants hit all the checks
    lst2 = []
    lst3 = []
    lst4 = []
    # take ohio list and lst list
    # use ohio list options to take from lst options
    # ex. ohio has mexican so grab all mexican lists and filter from there
    for i in restaurant_list:
        if preferences[0] in i:
            lst1.append(i)
    if len(lst1) == 0:
        print('Sorry, we do not have anything in our database that fits your preferences.')
        print('Good-bye!')
        sys.exit()
    for i in lst1:
        if preferences[1] in i:
            lst2.append(i)
    if len(lst2) == 0:
        print('Sorry, we do not have anything in our database that fits your preferences.')
        print('Good-bye!')
        sys.exit()
    for i in lst2:          #all this (if and for) is to filter
        if preferences[2] in i:
            lst3.append(i)
    if len(lst3) == 0:
        print('Sorry, we do not have anything in our database that fits your preferences.')
        print('Good-bye!')
        sys.exit()
    elif preferences[0] != 'Breakfast': #skips if you want breakfast
        for i in lst3:
            if preferences[3] in i:
                lst4.append(i)
        if len(lst4) == 0:
            print('\nSorry, we do not have anything in our database that fits your preferences.')
            print('Good-bye!')
            sys.exit()

    if preferences[0] == 'Breakfast':
        lst4 = lst3
            
    return lst4

def randomizer(x):
    names = []
    count = 0
    print('\nHere are the options we are randomizing:\n')
    while count != len(x):
        print(f'{x[count][0]}')
        names.append(x[count][0]) #displaying the resturants in the options we found and adding them to a list
        count = count + 1
    print()
    num = random.randrange(0,len(names)) #grabs a number that we can use for position
    print(f'We have decided that you will get....... {names[num]} today!')

def special(restaurants):
    num = random.randrange(0,len(restaurants))
    random_restaurant = restaurants[num]
    if random_restaurant[1] != 'Breakfast':
        print(f'\nWe have randomized EVERY place in our database and you have been given....... {random_restaurant[0]}!\n')
        print(f'{random_restaurant[0]} has {random_restaurant[4]} food, is {random_restaurant[3]}d, and is a {random_restaurant[2]} experience.')
    elif random_restaurant[1] == 'Breakfast':
        print(f'\nWe have randomized EVERY place in our database and you have been given....... {random_restaurant[0]}!\n')
        print(f'{random_restaurant[0]} has {random_restaurant[1]} food, is {random_restaurant[3]}, and is a {random_restaurant[2]} experience.')
        
def main():
    welcome()
    food = restaurants('database.txt')
    preferences = inputs()
    if preferences == 1:
        special(food)
    else:
        options = program(food,preferences)
        randomizer(options)
    

main()

