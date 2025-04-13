from add_task import add_task
from list_tasks import list_tasks
from update_task import update_task
from complete_task import complete_task
from delete_task import delete_task

def main():
    tasks = []

    while True:
        print("\n=== Task Manager ===")
        print("1. Add task")
        print("2. List tasks")
        print("3. Update task")
        print("4. Mark task as completed")
        print("5. Delete task")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Task description: ")
            task = add_task(tasks, desc)
            print("Task added:", task)

        elif choice == "2":
            list_tasks(tasks)

        elif choice == "3":
            task_id = input("Enter task ID to update: ")
            new_desc = input("Enter new description: ")
            task = update_task(tasks, task_id, new_desc)
            print("Task updated." if task else "Task not found.")

        elif choice == "4":
            task_id = input("Enter task ID to mark as completed: ")
            task = complete_task(tasks, task_id)
            print("Task marked as completed." if task else "Task not found.")

        elif choice == "5":
            task_id = input("Enter task ID to delete: ")
            task = delete_task(tasks, task_id)
            print("Task deleted." if task else "Task not found.")

        elif choice == "6":
            print("Exiting Task Manager. Bye!")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
