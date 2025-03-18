import time

tasks = []


def add_task():
    task_name = input("Enter the task name: ")
    task_time = input("Enter the task time in seconds: ")

    task = {
        "name": task_name,
        "time": int(task_time)
    }
    tasks.append(task)

    print("Task added successfully!")


def run_scheduler():
    print("Task scheduler started!")

    while len(tasks) != 0:
        task = tasks.pop(0)
        print(task['name'])

        time.sleep(task['time'])
        print(f"\nTask {task['name']} completed!")


def main():
    while True:
        try:
            print("\nMenu:")
            print("====================")
            print("1. Add a task")
            print("2. Run scheduler")
            print("3. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_task()
            elif choice == 2:
                run_scheduler()
            elif choice == 3:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input! Please try again.")


if __name__ == "__main__":
    main()
