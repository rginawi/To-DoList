#Giovanny Ceballos and Reem
#1/11/24


todo = ["Eggs", "Milk", "Flour","Sugar","Bread", "Cheese","Ham"]
def replay():
    displaymenu()


def displaymenu():
    print("Welcom4e to your Shopping List!")
    print("What would you like to do to your list? :\n 1. Add to list\n 2. View List\n 3. Mark Item Complete\n 4. Remove Item\n 5. Remove list\n 6. Sort Alphabetically\n 7. Print # of Items")
    option = int(input("Option : "))
    if option == 1:
        print ("What would you like to add?")
        add = input("Type in item : ")
        print("Where would you like to add it?")
        where = int(input("Type in a number between 0 and 7 : "))
        todo.insert(where, add)
        replay()
    if option == 2:
        print(todo)
        replay()
    if option == 3:
        print("Which item would you like to mark as complete?")
        comp = input("Type in the item : ")
        x = todo.index(comp)
        todo[x] = comp + "[X]"
        replay()
    if option == 4:
        print("Which item would you like to remove?")
        remove = input("Select which item to remove : ")
        y = todo.index(remove)
        todo.pop(y)
        replay()
    if option == 5:
        todo.clear()
        print(todo)
        replay()
    if option == 6:
        todo.sort()
        print(todo)
        replay()
    if option == 7:
        todo.count()
        print(todo)
        replay()



displaymenu()

