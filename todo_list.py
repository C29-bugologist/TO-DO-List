
my_todolist = []

#task_function = int(input("Enter 1 for adding a new task\nEnter 2 for removing a completed task\nEnter 3 for viewing all tasks\n"))

while True:
    print("----------TO-DO LIST----------\n")
    task_function = int(input("Enter 1 for adding a new task\nEnter 2 for removing a completed task\nEnter 3 for viewing all tasks\nEnter 4 for Ending the program resting the list"))

    if task_function == 3:
        print(my_todolist)
    elif task_function == 1:
        task_add = input("What is the task that you want to add?\n")
        my_todolist.append(task_add)
    elif task_function == 2:
         task_remove = input("What is the task that you want to remove?\n")
         if task_remove in my_todolist:
             my_todolist.remove(task_remove)
         else:
             print("No such Task found")
    elif task_function == 4:
        break   
    else:
        print("Choose either 1, 2, or 3")
print("goodby")