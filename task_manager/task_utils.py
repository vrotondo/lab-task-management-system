'''from datetime import datetime
from validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    """
    Add a new task to the tasks list.
    
    Args:
        title (str): The task title
        description (str): The task description
        due_date (str): The task due date in YYYY-MM-DD format
        
    Returns:
        bool: True if task was added successfully, False otherwise
    """
    # Validate inputs
    if not validate_task_title(title):
        return False
        
    if not validate_task_description(description):
        return False
        
    if not validate_due_date(due_date):
        return False
    
    # Create task dictionary
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    
    # Add to tasks list
    tasks.append(task)
    print("Task added successfully!")
    return True

def mark_task_as_complete(index, tasks=tasks):
    """
    Mark a task as complete.
    
    Args:
        index (int): The index of the task to mark as complete
        tasks (list): The list of tasks
        
    Returns:
        bool: True if task was marked as complete, False otherwise
    """
    if not tasks:
        print("No tasks available.")
        return False
        
    try:
        index = int(index)
        if index < 0 or index >= len(tasks):
            print(f"Error: Invalid task index. Please enter a number between 0 and {len(tasks) - 1}.")
            return False
            
        if tasks[index]["completed"]:
            print("Task is already marked as complete.")
            return False
            
        tasks[index]["completed"] = True
        print("Task marked as complete!")
        return True
    except ValueError:
        print("Error: Please enter a valid number.")
        return False

def view_pending_tasks(tasks=tasks):
    """
    Display all pending (not completed) tasks.
    
    Args:
        tasks (list): The list of tasks
    """
    if not tasks:
        print("No tasks available.")
        return
    
    pending_tasks = [task for task in tasks if not task["completed"]]
    
    if not pending_tasks:
        print("No pending tasks available.")
        return
        
    print("\nPending Tasks:")
    for i, task in enumerate(pending_tasks):
        print(f"{i}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}")
        print()

def calculate_progress(tasks=tasks):
    """
    Calculate the progress percentage of completed tasks.
    
    Args:
        tasks (list): The list of tasks
        
    Returns:
        float: The progress percentage (0-100)
    """
    if not tasks:
        return 0.0
        
    completed_count = sum(1 for task in tasks if task["completed"])
    progress = (completed_count / len(tasks)) * 100
    return progress'''


from datetime import datetime
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

tasks = []  # List to store tasks

def add_task(title, description, due_date):
    # validate functions:
    validate_due_date(due_date)
    validate_task_description(description)
    validate_task_title(title)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)  # Add the task to the list of tasks     
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Error: Invalid task index. Please enter a number between 0 and", len(tasks) - 1)

def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if not task["completed"]]
    if not pending_tasks:
        print("No pending tasks available.")
    else:
        print("\nPending Tasks:")
        for i, task in enumerate(pending_tasks):
            print(f"{i}. Title: {task['title']}")
            print(f"   Description: {task['description']}")
            print(f"   Due Date: {task['due_date']}")
            print()

def calculate_progress(tasks=tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    progress = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    return progress
