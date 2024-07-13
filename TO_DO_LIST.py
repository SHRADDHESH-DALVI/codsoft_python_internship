U_task=[]


def add_T():

    task = input(" Enter task :- ")

    U_task.append(task)

    print("your task added")
    
def jls_extract_def():
    return print


def view_T():

    print("Veiw your tasks ..."  , U_task)

        
        

def delete_T():

    task_number = int(input(" enter the task number to delete :" ))
    

    if task_number > 0 and task_number <= len(U_task):

        U_task.pop(task_number -1 )

        print("Task deleted !")
    else:

        print (" Invalid Task number  ..!")
        

        #main prog. loop
        

while True:

    print("\n 1. Add task")

    print ("2. View task")

    print ("3.Delete task")

    print ("4. Quit")

    choice = input("choose an option:")
    

    if choice =="1":

        add_T()

    elif choice == "2":

        view_T()

    elif choice == "3":

        delete_T()

    elif choice=="4":

        break 
    else:

        print("inv1alid choice...!")
