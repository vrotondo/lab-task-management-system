from datetime import datetime

def validate_task_title(title):
    """
    Validate the task title.
    
    Args:
        title (str): The task title to validate
        
    Returns:
        bool: True if title is valid, False otherwise
    """
    if not title:
        print("Error: Title cannot be empty.")
        return False
    
    if len(title) < 3:
        print("Error: Title must be at least 3 characters long.")
        return False
    
    if len(title) > 50:
        print("Error: Title must be no more than 50 characters long.")
        return False
    
    return True

def validate_task_description(description):
    """
    Validate the task description.
    
    Args:
        description (str): The task description to validate
        
    Returns:
        bool: True if description is valid, False otherwise
    """
    if not description:
        print("Error: Description cannot be empty.")
        return False
    
    if len(description) > 200:
        print("Error: Description must be no more than 200 characters long.")
        return False
    
    return True

def validate_due_date(due_date):
    """
    Validate the task due date in YYYY-MM-DD format.
    
    Args:
        due_date (str): The due date string to validate
        
    Returns:
        bool: True if due date is valid, False otherwise
    """
    if not due_date:
        print("Error: Due date cannot be empty.")
        return False
    
    try:
        # Try to parse the date in YYYY-MM-DD format
        date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        
        # Check if the date is in the past
        if date_obj.date() < datetime.now().date():
            print("Error: Due date cannot be in the past.")
            return False
            
        return True
    except ValueError:
        print("Error: Due date must be in the format YYYY-MM-DD.")
        return False