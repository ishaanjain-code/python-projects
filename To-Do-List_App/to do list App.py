def view_task(tasks):
    if tasks:
        for i,task in enumerate(tasks,start=1):
            print(f"{i}. {task}")
    else:
        print("no task to display")

tasks=[]
while True:
    print("--- To Do List App ---")
    print("enter 1 to add task\nenter 2 to view your tasks\nenter 3 to delete your task\nenter 4 to exit the app")
    choice=int(input("enter your choice: "))
    if choice==1:
        task=input("enter your task: ")
        if task:
            tasks.append(task)
            print("task added successfully\n")
            view_task(tasks)
    elif choice==2:
        view_task(tasks)
    elif choice==3:
        if not tasks:
            print("no task to delete")
        else:
            for i,task in enumerate(tasks,start=1):
                print(f"{i}. {task}")
            try:
                num=int(input("enter task number to delete task: "))
                index=num-1
                if 0 <= index < len(tasks):
                    removed_task = tasks.pop(index)
                    print(f"Deleted task: {removed_task}")
                else :
                    print("invalid task number")
            except ValueError:
                print("invalid task number")
    elif choice==4 :
        print("--- exiting app ---")
        break
    else:
        print("invalid choice")