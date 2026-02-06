"""
Module for managing tasks in the console todo application.
"""

import datetime
import calendar
from typing import Optional, Dict, Any, Union

# Global in-memory storage for tasks
tasks_storage = []


def create_task(title, description="", completed=False, priority="Medium", tags=None, due_date=None, recurring=None):
    """
    Creates a new task dictionary with a unique ID.

    Args:
        title (str): The title of the task (required)
        description (str): The description of the task (optional)
        completed (bool): Whether the task is completed (default False)
        priority (str): Priority level of the task (default "Medium")
        tags (list): List of tags associated with the task (default [])
        due_date (str or datetime.datetime, optional): Due date for the task
        recurring (dict, optional): Recurrence pattern for the task

    Returns:
        dict: A task dictionary with id, title, description, completed status, priority, tags, due_date, and recurring
    """
    # Generate a unique ID based on the current length of the storage
    task_id = len(tasks_storage) + 1

    # Set default tags list if none provided
    if tags is None:
        tags = []

    # Normalize priority
    normalized_priority = normalize_priority(priority)

    # Convert due_date to ISO string format if it's a datetime object
    if isinstance(due_date, datetime.datetime):
        due_date = due_date.isoformat()
    elif due_date is not None and not isinstance(due_date, str):
        due_date = None

    # Create the task dictionary
    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "completed": completed,
        "priority": normalized_priority,
        "tags": tags,
        "due_date": due_date,
        "recurring": recurring
    }

    return task


def get_next_id():
    """
    Gets the next available ID for a new task.

    Returns:
        int: The next available ID
    """
    return len(tasks_storage) + 1


def add_task(task):
    """
    Adds a task to the in-memory storage.

    Args:
        task (dict): The task dictionary to add

    Returns:
        bool: True if the task was added successfully, False otherwise
    """
    global tasks_storage
    tasks_storage.append(task)
    return True


def get_all_tasks():
    """
    Retrieves all tasks from the in-memory storage.

    Returns:
        list: A list of all task dictionaries
    """
    global tasks_storage
    return tasks_storage


def get_task_by_id(task_id):
    """
    Retrieves a task by its ID.

    Args:
        task_id (int): The ID of the task to retrieve

    Returns:
        dict or None: The task dictionary if found, None otherwise
    """
    global tasks_storage
    for task in tasks_storage:
        if task["id"] == task_id:
            return task
    return None


def update_task(task_id, title=None, description=None, completed=None, priority=None, tags=None, due_date=None, recurring=None):
    """
    Updates a task by its ID.

    Args:
        task_id (int): The ID of the task to update
        title (str, optional): New title for the task
        description (str, optional): New description for the task
        completed (bool, optional): New completion status for the task
        priority (str, optional): New priority for the task
        tags (list, optional): New tags for the task
        due_date (str or datetime.datetime, optional): New due date for the task
        recurring (dict, optional): New recurrence pattern for the task

    Returns:
        bool: True if the task was updated successfully, False otherwise
    """
    global tasks_storage
    for i, task in enumerate(tasks_storage):
        if task["id"] == task_id:
            if title is not None:
                tasks_storage[i]["title"] = title
            if description is not None:
                tasks_storage[i]["description"] = description
            if completed is not None:
                tasks_storage[i]["completed"] = completed
            if priority is not None:
                # Normalize the priority before updating
                normalized_priority = normalize_priority(priority)
                tasks_storage[i]["priority"] = normalized_priority
            if tags is not None:
                tasks_storage[i]["tags"] = tags
            if due_date is not None:
                # Convert due_date to ISO string format if it's a datetime object
                if isinstance(due_date, datetime.datetime):
                    tasks_storage[i]["due_date"] = due_date.isoformat()
                elif due_date is not None and not isinstance(due_date, str):
                    tasks_storage[i]["due_date"] = None
                else:
                    tasks_storage[i]["due_date"] = due_date
            if recurring is not None:
                tasks_storage[i]["recurring"] = recurring
            return True
    return False


def validate_priority(priority):
    """
    Validates that the priority is one of the allowed values.

    Args:
        priority (str): The priority value to validate

    Returns:
        bool: True if the priority is valid, False otherwise
    """
    valid_priorities = ["High", "Medium", "Low", "H", "M", "L", "1", "2", "3"]
    return priority.capitalize() in valid_priorities


def normalize_priority(priority):
    """
    Normalizes the priority value to the standard form (High, Medium, Low).

    Args:
        priority (str): The priority value to normalize

    Returns:
        str: The normalized priority value
    """
    priority_map = {
        "H": "High", "1": "High",
        "M": "Medium", "2": "Medium", 
        "L": "Low", "3": "Low"
    }
    
    normalized = priority.capitalize()
    if normalized in priority_map:
        return priority_map[normalized]
    return normalized


def normalize_tags(tags_input):
    """
    Normalizes tags input by splitting on commas and stripping whitespace.

    Args:
        tags_input (str): Comma-separated tags string

    Returns:
        list: List of normalized tags
    """
    if not tags_input:
        return []
    
    # Split by comma, strip whitespace, and filter out empty strings
    tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
    return tags


def delete_task(task_id):
    """
    Deletes a task by its ID.

    Args:
        task_id (int): The ID of the task to delete

    Returns:
        bool: True if the task was deleted successfully, False otherwise
    """
    global tasks_storage
    for i, task in enumerate(tasks_storage):
        if task["id"] == task_id:
            del tasks_storage[i]
            return True
    return False


def sort_tasks(tasks_list=None, sort_by="priority"):
    """
    Sorts tasks based on specified criteria.

    Args:
        tasks_list (list, optional): List of tasks to sort (defaults to all tasks)
        sort_by (str): Sort criteria ('priority', 'title', 'id', 'due_date')

    Returns:
        list: A list of tasks sorted according to the specified criteria
    """
    if tasks_list is None:
        tasks_list = tasks_storage[:]

    if sort_by.lower() == "priority":
        # Define priority order: High > Medium > Low
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        return sorted(tasks_list, key=lambda x: priority_order.get(x["priority"], 4))
    elif sort_by.lower() == "title":
        return sorted(tasks_list, key=lambda x: x["title"].lower())
    elif sort_by.lower() == "id":
        return sorted(tasks_list, key=lambda x: x["id"])
    elif sort_by.lower() == "due_date":
        # Sort by due date, with tasks without due dates appearing last
        def due_date_key(task):
            if task.get('due_date'):
                try:
                    return datetime.datetime.fromisoformat(task['due_date'].replace('Z', '+00:00'))
                except ValueError:
                    # If due_date is not in ISO format, try parsing it as a string
                    parsed_date = parse_datetime_input(task['due_date'])
                    return parsed_date if parsed_date else datetime.datetime.max
            else:
                # Tasks without due dates go to the end
                return datetime.datetime.max
        return sorted(tasks_list, key=due_date_key)
    else:
        # Default to priority sort if invalid sort_by provided
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        return sorted(tasks_list, key=lambda x: priority_order.get(x["priority"], 4))


def filter_tasks(status=None, priority=None, tag=None, overdue=None, upcoming=None, recurring=None):
    """
    Filters tasks based on specified criteria.

    Args:
        status (str, optional): Filter by status ('completed', 'incomplete', or None for all)
        priority (str, optional): Filter by priority level ('High', 'Medium', 'Low')
        tag (str, optional): Filter by specific tag
        overdue (bool, optional): Filter by overdue status (True for overdue, False for not overdue)
        upcoming (bool, optional): Filter by upcoming status (True for upcoming, False for not upcoming)
        recurring (bool, optional): Filter by recurring status (True for recurring, False for non-recurring)

    Returns:
        list: A list of tasks that match the filter criteria
    """
    filtered_tasks = tasks_storage[:]

    # Filter by status
    if status:
        if status.lower() == 'completed':
            filtered_tasks = [task for task in filtered_tasks if task["completed"]]
        elif status.lower() == 'incomplete':
            filtered_tasks = [task for task in filtered_tasks if not task["completed"]]

    # Filter by priority
    if priority:
        normalized_priority = normalize_priority(priority)
        filtered_tasks = [task for task in filtered_tasks if task["priority"] == normalized_priority]

    # Filter by tag
    if tag:
        filtered_tasks = [task for task in filtered_tasks if tag in task["tags"]]

    # Filter by overdue status
    if overdue is not None:
        if overdue:
            filtered_tasks = [task for task in filtered_tasks if is_task_overdue(task)]
        else:
            filtered_tasks = [task for task in filtered_tasks if not is_task_overdue(task)]

    # Filter by upcoming status
    if upcoming is not None:
        if upcoming:
            filtered_tasks = [task for task in filtered_tasks if is_task_upcoming(task)]
        else:
            filtered_tasks = [task for task in filtered_tasks if not is_task_upcoming(task)]

    # Filter by recurring status
    if recurring is not None:
        if recurring:
            filtered_tasks = [task for task in filtered_tasks if task.get('recurring')]
        else:
            filtered_tasks = [task for task in filtered_tasks if not task.get('recurring')]

    return filtered_tasks


def search_tasks(keyword):
    """
    Searches for tasks containing the keyword in title or description.

    Args:
        keyword (str): The keyword to search for

    Returns:
        list: A list of tasks that match the search criteria
    """
    if not keyword:
        return []
    
    keyword_lower = keyword.lower()
    matching_tasks = []
    
    for task in tasks_storage:
        # Check if keyword is in title or description (case insensitive)
        if (keyword_lower in task["title"].lower() or 
            (task["description"] and keyword_lower in task["description"].lower())):
            matching_tasks.append(task)
    
    return matching_tasks


def parse_datetime_input(date_input: str) -> Optional[datetime.datetime]:
    """
    Parse various date/time input formats into a datetime object.

    Args:
        date_input (str): Date/time input string in various formats

    Returns:
        datetime.datetime or None: Parsed datetime object or None if invalid
    """
    if not date_input:
        return None
    
    # Common date formats to try
    formats = [
        "%Y-%m-%d %H:%M",  # YYYY-MM-DD HH:MM
        "%Y-%m-%d",        # YYYY-MM-DD
        "%m/%d/%Y",        # MM/DD/YYYY
        "%m/%d/%Y %H:%M",  # MM/DD/YYYY HH:MM
        "%d/%m/%Y",        # DD/MM/YYYY
        "%d/%m/%Y %H:%M",  # DD/MM/YYYY HH:MM
        "%m-%d-%Y",        # MM-DD-YYYY
        "%m-%d-%Y %H:%M",  # MM-DD-YYYY HH:MM
        "%d-%m-%Y",        # DD-MM-YYYY
        "%d-%m-%Y %H:%M",  # DD-MM-YYYY HH:MM
    ]
    
    # Try to parse with each format
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_input.strip(), fmt)
        except ValueError:
            continue
    
    # Handle relative terms
    today = datetime.date.today()
    if date_input.lower() == "today":
        return datetime.datetime.combine(today, datetime.time.min)
    elif date_input.lower() == "tomorrow":
        tomorrow = today + datetime.timedelta(days=1)
        return datetime.datetime.combine(tomorrow, datetime.time.min)
    elif date_input.lower() == "yesterday":
        yesterday = today - datetime.timedelta(days=1)
        return datetime.datetime.combine(yesterday, datetime.time.min)
    
    # Handle relative days like "in 3 days", "next monday", etc.
    if date_input.lower().startswith("in "):
        try:
            parts = date_input.lower().split()
            if len(parts) >= 2 and parts[1].isdigit():
                days = int(parts[1])
                future_date = today + datetime.timedelta(days=days)
                return datetime.datetime.combine(future_date, datetime.time.min)
        except:
            pass
    
    return None


def is_task_overdue(task: Dict[str, Any]) -> bool:
    """
    Check if a task is overdue based on its due date.

    Args:
        task (dict): The task dictionary

    Returns:
        bool: True if the task is overdue, False otherwise
    """
    if not task.get('due_date'):
        return False
    
    try:
        due_date = datetime.datetime.fromisoformat(task['due_date'].replace('Z', '+00:00'))
        now = datetime.datetime.now()
        
        # Compare only the date part if no time is specified
        if due_date.hour == 0 and due_date.minute == 0 and due_date.second == 0:
            return due_date.date() < now.date()
        else:
            return due_date < now
    except ValueError:
        # If due_date is not in ISO format, try parsing it as a string
        try:
            parsed_date = parse_datetime_input(task['due_date'])
            if parsed_date:
                now = datetime.datetime.now()
                return parsed_date < now
        except:
            pass
        
    return False


def is_task_due_today(task: Dict[str, Any]) -> bool:
    """
    Check if a task is due today based on its due date.

    Args:
        task (dict): The task dictionary

    Returns:
        bool: True if the task is due today, False otherwise
    """
    if not task.get('due_date'):
        return False
    
    try:
        due_date = datetime.datetime.fromisoformat(task['due_date'].replace('Z', '+00:00'))
        today = datetime.date.today()
        
        return due_date.date() == today
    except ValueError:
        # If due_date is not in ISO format, try parsing it as a string
        try:
            parsed_date = parse_datetime_input(task['due_date'])
            if parsed_date:
                today = datetime.date.today()
                return parsed_date.date() == today
        except:
            pass
        
    return False


def is_task_upcoming(task: Dict[str, Any]) -> bool:
    """
    Check if a task is upcoming (due in the future) based on its due date.

    Args:
        task (dict): The task dictionary

    Returns:
        bool: True if the task is upcoming, False otherwise
    """
    if not task.get('due_date'):
        return False
    
    try:
        due_date = datetime.datetime.fromisoformat(task['due_date'].replace('Z', '+00:00'))
        now = datetime.datetime.now()
        
        # Compare only the date part if no time is specified
        if due_date.hour == 0 and due_date.minute == 0 and due_date.second == 0:
            return due_date.date() > now.date()
        else:
            return due_date > now
    except ValueError:
        # If due_date is not in ISO format, try parsing it as a string
        try:
            parsed_date = parse_datetime_input(task['due_date'])
            if parsed_date:
                now = datetime.datetime.now()
                return parsed_date > now
        except:
            pass
        
    return False


def calculate_next_occurrence(task: Dict[str, Any]) -> Optional[datetime.datetime]:
    """
    Calculate the next occurrence date based on the recurrence pattern.

    Args:
        task (dict): The task dictionary with recurrence information

    Returns:
        datetime.datetime or None: The next occurrence date or None if invalid
    """
    if not task.get('recurring'):
        return None
    
    recurring_info = task['recurring']
    if not isinstance(recurring_info, dict):
        return None
    
    # Get the last occurrence date (current task's due date)
    last_due_date = None
    if task.get('due_date'):
        try:
            last_due_date = datetime.datetime.fromisoformat(task['due_date'].replace('Z', '+00:00'))
        except ValueError:
            last_due_date = parse_datetime_input(task['due_date'])
    
    if not last_due_date:
        # If no due date, use current date
        last_due_date = datetime.datetime.now()
    
    interval = recurring_info.get('interval', 'daily')
    every = recurring_info.get('every', 1)
    
    if interval == 'daily':
        next_date = last_due_date + datetime.timedelta(days=every)
    elif interval == 'weekly':
        next_date = last_due_date + datetime.timedelta(weeks=every)
        # If specific days are specified, adjust to the next occurrence of that day
        if 'days' in recurring_info and recurring_info['days']:
            next_date = get_next_weekday(last_due_date, recurring_info['days'])
    elif interval == 'monthly':
        next_date = add_months(last_due_date, every)
    elif interval == 'yearly':
        next_date = add_years(last_due_date, every)
    elif interval == 'custom':
        # For custom intervals, use 'every' as the number of days
        next_date = last_due_date + datetime.timedelta(days=every)
    else:
        # Default to daily if interval is not recognized
        next_date = last_due_date + datetime.timedelta(days=every)
    
    return next_date


def get_next_weekday(current_date: datetime.datetime, target_days: list) -> datetime.datetime:
    """
    Get the next occurrence of one of the specified weekdays.

    Args:
        current_date (datetime.datetime): The starting date
        target_days (list): List of target weekday names (e.g., ['Monday', 'Wednesday'])

    Returns:
        datetime.datetime: The next occurrence of one of the target days
    """
    # Map day names to weekday numbers (Monday=0, Sunday=6)
    day_to_num = {
        'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3,
        'friday': 4, 'saturday': 5, 'sunday': 6
    }
    
    # Convert target days to numbers
    target_nums = []
    for day in target_days:
        day_lower = day.lower()
        if day_lower in day_to_num:
            target_nums.append(day_to_num[day_lower])
    
    if not target_nums:
        # If no valid days, return the same date plus one week
        return current_date + datetime.timedelta(weeks=1)
    
    # Find the next occurrence
    current_weekday = current_date.weekday()
    min_days_ahead = float('inf')
    
    for target_num in target_nums:
        if target_num > current_weekday:
            # Target day is later this week
            days_ahead = target_num - current_weekday
        else:
            # Target day is next week
            days_ahead = 7 - current_weekday + target_num
            
        if days_ahead < min_days_ahead:
            min_days_ahead = days_ahead
    
    return current_date + datetime.timedelta(days=min_days_ahead)


def add_months(source_date: datetime.datetime, months: int) -> datetime.datetime:
    """
    Add months to a date, handling month-end edge cases.

    Args:
        source_date (datetime.datetime): The source date
        months (int): Number of months to add

    Returns:
        datetime.datetime: The resulting date
    """
    month = source_date.month - 1 + months
    year = source_date.year + month // 12
    month = month % 12 + 1
    
    # Handle month-end edge cases (e.g., Jan 31 + 1 month should be Feb 28/29, not Mar 3)
    day = min(source_date.day, calendar.monthrange(year, month)[1])
    
    return source_date.replace(year=year, month=month, day=day)


def add_years(source_date: datetime.datetime, years: int) -> datetime.datetime:
    """
    Add years to a date, handling leap year edge cases.

    Args:
        source_date (datetime.datetime): The source date
        years (int): Number of years to add

    Returns:
        datetime.datetime: The resulting date
    """
    year = source_date.year + years
    
    # Handle leap year edge cases (e.g., Feb 29, 2020 + 1 year should be Feb 28, 2021)
    if source_date.month == 2 and source_date.day == 29 and not calendar.isleap(year):
        return source_date.replace(year=year, day=28)
    
    return source_date.replace(year=year)


def filter_overdue_tasks():
    """
    Filters tasks that are overdue.

    Returns:
        list: A list of tasks that are overdue
    """
    return [task for task in tasks_storage if is_task_overdue(task)]


def filter_upcoming_tasks():
    """
    Filters tasks that are upcoming.

    Returns:
        list: A list of tasks that are upcoming
    """
    return [task for task in tasks_storage if is_task_upcoming(task)]


def filter_recurring_tasks():
    """
    Filters tasks that are recurring.

    Returns:
        list: A list of tasks that are recurring
    """
    return [task for task in tasks_storage if task.get('recurring')]


def toggle_task_status(task_id):
    """
    Toggles the completion status of a task by its ID.

    Args:
        task_id (int): The ID of the task to toggle

    Returns:
        bool: True if the task status was toggled successfully, False otherwise
    """
    global tasks_storage
    for i, task in enumerate(tasks_storage):
        if task["id"] == task_id:
            # Check if this is a recurring task
            if task.get("recurring"):
                # Create the next occurrence before toggling the status
                next_occurrence = calculate_next_occurrence(task)
                if next_occurrence:
                    # Create a new task with the next occurrence
                    new_task = create_task(
                        title=task["title"],
                        description=task["description"],
                        completed=False,  # New occurrence starts as incomplete
                        priority=task["priority"],
                        tags=task["tags"],
                        due_date=next_occurrence,
                        recurring=task["recurring"]
                    )
                    add_task(new_task)
            
            # Mark the current task as completed
            tasks_storage[i]["completed"] = True
            return True
    return False