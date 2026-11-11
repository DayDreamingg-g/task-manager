print("Hello, I'm test Task Manager based on python for learn something new in programming! "
      "\nHere's all options what you can choose.")


def main():
    tasks = []
    while True:
        print("\nWrite number of operation what you want to do. "
          "\n 1. - Add one task or more. "
          "\n 2. - Show tasks "
          "\n 3. - Complete tasks"
          "\n 4. - Exit the program")

        choose = input("So, what you choose? "
              "\nWrite here number of operation: ")

        if choose in ("1", "1."):
            add_task(tasks)

        elif choose in ("2", "2."):
            show_tasks(tasks)

        elif choose in ("3", "3."):
            complete_tasks(tasks)

        elif choose in ("4", "4."):
            break

def add_task(tasks):
    while True:
        n = int(input("How much tasks you want to add: "))

        for i in range (n):
            task = input(f"Enter your task: ")
            tasks.append(task)

        print("That's all, or add new tasks? Write the number of operation you want "
              "\n1. Add new tasks."
              "\n2. Back to menu."
              "\n3. Exit the program")

        choose = (input("Enter number of operation you want to do: "))
        if choose in ("1", "1."):
            continue
        elif choose in ("2", "2."):
            return

        else:
            break

def show_tasks(tasks):
    print("\nHere all your tasks:")
    for index, value in enumerate(tasks, start=1):
        print(f"{index}. {value}")




def complete_tasks(tasks):
    print("\nHere all your tasks:")
    for index, value in enumerate(tasks, start=1):
        print(f"{index}. {value}")
    #task_complete=int(input("\nWhat task you want to complete?"))
    #if task_complete >= 1 and task_complete <= len(tasks):
    try:
        task_complete = int(input("\nWhat task you want to complete?"))
        #task_complete = int(tasks.pop(task_complete-1))
    except ValueError:
        print("Please enter a valid number!")
        return





if __name__ == "__main__":
    main()