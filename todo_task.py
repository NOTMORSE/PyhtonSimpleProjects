todo_task = []


def todo_list():

    print("To do List for a day")
    print("|1.Add a Task", "\n|2.View Task", "\n|3.Mark Task as Complete", "\n|4.Quit")
    choice = int(input("Please choose the number of your choice: "))
    if choice == 1:
        creation()
    elif choice == 2:
        view()
    elif choice == 3:
        completed()
    else:
        print("Thank you for using the app")


def creation():
    create_task = ""
    while create_task != "quit":
        create = input("Add a task(type 'quit' to stop)': ").lower()
        if create == "quit":
            todo_list()
            break
        todo_task.append(create)


def view():
    for i in todo_task:
        print(f"* {i}".title())
    print("|1. Add another task", "\n|2. Return to main menu")
    choice = int(input("Please choose a number of your choice: "))
    if choice == 1:
        creation()
    else:
        todo_list()


def completed():
    for i in todo_task:
         print(f"* {i}".title())
    print("|1. Mark a task as complete", "\n|2. Return to main menu")
    choice = int(input("Please enter a number of your choice: "))
    marked_complete = ""
    while marked_complete != "n":
        if choice == 1:
            marked = input("Please enter the task u completed: ")
            todo_task.remove(marked)
            print("Updated list:")
            for i in todo_task:
                print(f"* {i}".title())
                marked_complete = input("Completed another task?(y/n) ").lower()
                if marked_complete == 'n':
                    todo_list()
            else:
                todo_list()
                break


todo_list()
