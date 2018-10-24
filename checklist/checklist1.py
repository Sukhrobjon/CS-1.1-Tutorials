# -*- coding: utf-8 -*-
checklist = []


def create(item):
    checklist.append(item)


def read(index):
    item = checklist[index]
    return item


def update(index, item):
    checklist[index] = item


def destroy(index):
    checklist.pop(index)


def mark_completed(index):
    print("√" + checklist[index])
#print all items inside list
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1


def user_input(prompt):
    # the input function will display a message in the terminal
    user_input = input(prompt)
    return user_input

def select(option):
    # Add and item to list
    if option.upper() == "A":
        input_item = user_input("Enter item: ")
        create(input_item)
    # Read item at specific index out of list
    elif option.upper() == "R":
        input_index = user_input("Enter the index: ")
        print(read(int(input_index)))
    # Print all item in the list
    elif option.upper() == "P":
        list_all_items()
    elif option.upper() == "C":
        completed = input("Enter the item you want to mark as completed:")
        mark_completed(int(completed))
    # Exits the while loop
    elif option.upper() == "Q":
        return False
    else:
        print("Invalid option selected! Please ")
        return True
    return True


runnning = True
while runnning:
    selection = user_input(
        "Enter A add to list, enter R to read from the list,"
        + "\nP to display the list, C to mark as completed the item," +
        "\nQ to exit the program!")
    runnning = select(selection)

print("Out of loop")
