from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

def main():
    """Main function to run the Task Management System."""
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            # Add a new task
            print("\nAdd a New Task")
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            
            add_task(title, description, due_date)
            
        elif choice == "2":
            # Mark a task as complete
            print("\nMark Task as Complete")
            from task_manager.task_utils import tasks
            
            if not tasks:
                print("No tasks available.")
                continue
                
            print("\nAll Tasks:")
            for i, task in enumerate(tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['title']} ({status})")
                
            task_index = input("\nEnter the index of the task to mark as complete: ")
            mark_task_as_complete(task_index)
            
        elif choice == "3":
            # View pending tasks
            view_pending_tasks()
            
        elif choice == "4":
            # View progress
            progress = calculate_progress()
            print(f"\nCurrent Progress: {progress:.2f}%")
            
        elif choice == "5":
            print("Exiting the program...")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()