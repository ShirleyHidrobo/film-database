import readfilms, addfilms, updatefilms, deletefilms # filmsreport
 
# create a function to read the filmsMenu.txt file
def menu_file():
    with open("python/python project/filmsMenu.txt") as filmsFile:
        # read data from the filmsMenu.txt file and save it in the menuOptions variable
        menuOptions = filmsFile.read()
    return menuOptions
# print(menu_file()) - it gives back what's in the file so we can read it in the terminal

# create the menu function
def films_menu():
    option = 0 # initialise the option variable with an integer value
    optionsList = ["1","2","3","4","5"] # initiliased a list data structure with optionsLis variable
 
    # initialised/assigned the variable 'menuChoices' to the menu_file()function
    menuChoices = menu_file()
 
    # create a while loop to repeat the code within the body of the while loop
    while option not in optionsList:
        # call/invoke the menu_file()function assigned to the 'menuChoices' variable to display the menu options
        print(menuChoices)
 
        # re-assign the option variable to an input function to ask to enter user choice
        option = input("Enter an option from the films main menu: ")
 
        #check if the user input from the option(assigned to the input function)variable
        # matches any of the menu options(menuChoices)
        if option not in optionsList:
            # execute the code below
            print(f"{option} is not a valid choice! ") # option(assigned to the input function)variable: 0//7/8/9...
    return option
# print(songs_menu()) - hasta aqui para q cuando el user ponga una opcion que no esta en la lista le devuelva q no es valido y que vuelva a seleccionar una opcion

#create a boolean variaable that can be toggled true/false or on/off --- from here, there're more ways to do it (match/dictionary)
mainProgram = True

while mainProgram: #same writing while True
    # initialise the songs_menu() function with mainMenu variable
    mainMenu = films_menu()
 
    # if option(assigned to the input function) = 1/2/3/4/5/6
    # if "1" == "1"
    if mainMenu == "1": #NO me sale esta opcion
        # ca// the file then the function from that file
        readfilms.read_films()
    elif mainMenu == "2":
        addfilms.insert_films()
    elif mainMenu == "3":
        updatefilms.update_films()
    elif mainMenu == "4":
        deletefilms.delete_films()
    # elif mainMenu == "5": #NO me sale esta opcion
        # filmsreport.films_report()
    else:# re-assign the value of the mainProgram variable to False
        mainProgram = False
        input("Press the 'Enter' key to quit the films app")

# if __name__ == "__main__":