"""
UI module for the console todo application.
Handles user interface elements and input validation.
"""

import datetime
from tasks import *


def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n" + "="*40)
    print("Console Todo Application")
    print("="*40)
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Mark task as complete/incomplete")
    print("6. Search tasks")
    print("7. Filter tasks")
    print("8. Sort tasks")
    print("9. View overdue tasks")
    print("10. View upcoming tasks")
    print("11. View recurring tasks")
    print("12. Exit")
    print("-"*40)


def get_user_choice():
    """
    Gets the user's menu choice.

    Returns:
        str: The user's choice
    """
    choice = input("Enter your choice (1-12): ").strip()
    return choice


def display_invalid_input():
    """
    Displays a message for invalid input.
    """
    print("\n❌ Invalid input. Please enter a number between 1 and 6.")


def get_priority_indicator(priority):
    """
    Returns a string indicator for the priority level.
    
    Args:
        priority (str): The priority level
        
    Returns:
        str: The priority indicator (e.g., [H], [M], [L])
    """
    priority_map = {
        "High": "[H]",
        "H": "[H]",
        "1": "[H]",
        "Medium": "[M]",
        "M": "[M]",
        "2": "[M]",
        "Low": "[L]",
        "L": "[L]",
        "3": "[L]"
    }
    
    normalized_priority = normalize_priority(priority)
    return priority_map.get(normalized_priority, "[M]")  # Default to [M] if not found


def handle_add_task():
    """
    Handles the process of adding a new task.
    """
    print("\n➕ Adding a new task...")

    # Get task title
    title = input("Enter task title: ").strip()

    # Validate title
    if not title:
        print("❌ Task title cannot be empty.")
        return

    # Get task description (optional)
    description = input("Enter task description (optional, press Enter to skip): ").strip()

    # Get task priority
    print("Enter priority (High/H/1, Medium/M/2, Low/L/3) [default: Medium]: ", end="")
    priority_input = input().strip()
    if not priority_input:
        priority_input = "Medium"

    # Validate and normalize priority
    if not validate_priority(priority_input):
        print("❌ Invalid priority. Using 'Medium' as default.")
        priority_input = "Medium"
    else:
        priority_input = normalize_priority(priority_input)

    # Get task tags (optional)
    tags_input = input("Enter tags (comma-separated, press Enter to skip): ").strip()
    tags = normalize_tags(tags_input)

    # Get due date (optional)
    due_date_input = input("Enter due date (YYYY-MM-DD, MM/DD/YYYY, or relative terms like 'tomorrow', press Enter to skip): ").strip()
    due_date = None
    if due_date_input:
        due_date = parse_datetime_input(due_date_input)
        if not due_date:
            print("⚠️  Invalid date format. Due date will be skipped.")
        else:
            due_date = due_date.isoformat()

    # Ask if the task should recur
    recurring_input = input("Should this task repeat? (y/N): ").strip().lower()
    recurring = None
    if recurring_input in ['y', 'yes']:
        print("Select recurrence pattern:")
        print("1. Daily")
        print("2. Weekly")
        print("3. Monthly")
        print("4. Yearly")
        print("5. Custom (every X days)")
        
        recurrence_choice = input("Enter choice (1-5): ").strip()
        
        recurring = {}
        if recurrence_choice == '1':
            recurring['interval'] = 'daily'
            recurring['every'] = 1
        elif recurrence_choice == '2':
            recurring['interval'] = 'weekly'
            recurring['every'] = 1
            # Ask for specific days of the week
            days_input = input("Enter days of the week (comma-separated, e.g., Monday, Wednesday): ").strip()
            if days_input:
                recurring['days'] = [day.strip().capitalize() for day in days_input.split(',')]
        elif recurrence_choice == '3':
            recurring['interval'] = 'monthly'
            recurring['every'] = 1
        elif recurrence_choice == '4':
            recurring['interval'] = 'yearly'
            recurring['every'] = 1
        elif recurrence_choice == '5':
            recurring['interval'] = 'custom'
            try:
                every_n = int(input("Repeat every how many days?: "))
                recurring['every'] = every_n
            except ValueError:
                print("Invalid number. Using default of 1 day.")
                recurring['every'] = 1
        else:
            print("Invalid choice. Recurrence will be skipped.")
            recurring = None

    # Create and add the task
    task = create_task(title, description, priority=priority_input, tags=tags, due_date=due_date, recurring=recurring)
    add_task(task)

    print(f"✅ Task '{title}' added successfully with ID {task['id']}!")


def handle_view_tasks():
    """
    Handles the process of viewing all tasks.
    """
    print("\n📋 Viewing all tasks...")

    tasks = get_all_tasks()

    if not tasks:
        print("📭 No tasks found.")
        return

    print(f"\nTotal tasks: {len(tasks)}")
    # Print header for better readability
    print(f"{'ID':<4} | {'Status':<7} | {'Pri':<4} | {'Due Date':<12} | {'Title':<25} | Tags | Recurrence")
    print("-" * 120)

    for task in tasks:
        status = "[x]" if task["completed"] else "[ ]"
        priority_indicator = get_priority_indicator(task['priority'])
        
        # Format due date
        due_date_str = ""
        if task.get('due_date'):
            try:
                dt = datetime.datetime.fromisoformat(task['due_date'].replace('Z', '+00:00'))
                due_date_str = dt.strftime("%Y-%m-%d")
                
                # Add visual indicators for overdue, today, or upcoming tasks
                if is_task_overdue(task):
                    due_date_str = f"[OVERDUE: {due_date_str}]"
                elif is_task_due_today(task):
                    due_date_str = f"[TODAY: {due_date_str}]"
                elif is_task_upcoming(task):
                    due_date_str = f"[UPCOMING: {due_date_str}]"
            except ValueError:
                due_date_str = task['due_date'][:10]  # Just show the date part
        
        tags_str = f"{', '.join(task['tags'])}" if task['tags'] else ""

        # Format recurrence info
        recurrence_str = ""
        if task.get('recurring'):
            recurring_info = task['recurring']
            interval = recurring_info.get('interval', 'Unknown')
            every = recurring_info.get('every', 1)
            if interval == 'daily':
                recurrence_str = f"Daily" if every == 1 else f"Every {every} days"
            elif interval == 'weekly':
                recurrence_str = f"Weekly" if every == 1 else f"Every {every} weeks"
                if 'days' in recurring_info:
                    recurrence_str += f" on {', '.join(recurring_info['days'])}"
            elif interval == 'monthly':
                recurrence_str = f"Monthly" if every == 1 else f"Every {every} months"
            elif interval == 'yearly':
                recurrence_str = f"Yearly" if every == 1 else f"Every {every} years"
            elif interval == 'custom':
                recurrence_str = f"Every {every} days"
            else:
                recurrence_str = f"Every {every} {interval}"

        # Truncate title if too long
        title = task['title'][:23] + ".." if len(task['title']) > 25 else task['title']

        print(f"{task['id']:<4} | {status:<7} | {priority_indicator:<4} | {due_date_str:<12} | {title:<25} | {tags_str} | {recurrence_str}")

        if task["description"]:
            print(f"       Description: {task['description']}")
        print()


def handle_update_task():
    """
    Handles the process of updating a task.
    """
    print("\n✏️  Updating a task...")

    tasks = get_all_tasks()

    if not tasks:
        print("📭 No tasks found to update.")
        return

    # Show current tasks
    print("Current tasks:")
    for task in tasks:
        status = "[x]" if task["completed"] else "[ ]"
        priority_indicator = get_priority_indicator(task['priority'])
        tags_str = f" ({', '.join(task['tags'])})" if task['tags'] else ""
        print(f"ID: {task['id']} | {status} | {priority_indicator} | Title: {task['title']} {tags_str}")

    try:
        task_id = int(input("\nEnter the ID of the task to update: "))
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")
        return

    # Check if task exists
    task = get_task_by_id(task_id)
    if not task:
        print(f"❌ Task with ID {task_id} not found.")
        return

    # Get new title (keep current if empty input)
    new_title = input(f"Enter new title (current: '{task['title']}', press Enter to keep current): ").strip()
    if not new_title:
        new_title = task['title']

    # Get new description (keep current if empty input)
    new_description = input(f"Enter new description (current: '{task['description']}', press Enter to keep current): ").strip()
    if not new_description:
        new_description = task['description']

    # Get new priority (keep current if empty input)
    print(f"Enter new priority (current: '{task['priority']}', High/H/1, Medium/M/2, Low/L/3, press Enter to keep current): ", end="")
    new_priority = input().strip()
    if not new_priority:
        new_priority = task['priority']
    else:
        # Validate and normalize priority
        if not validate_priority(new_priority):
            print("❌ Invalid priority. Keeping current priority.")
            new_priority = task['priority']
        else:
            new_priority = normalize_priority(new_priority)

    # Get new tags (keep current if empty input)
    current_tags_str = ', '.join(task['tags']) if task['tags'] else ''
    new_tags_input = input(f"Enter new tags (current: '{current_tags_str}', comma-separated, press Enter to keep current): ").strip()
    if not new_tags_input:
        new_tags = task['tags']
    else:
        new_tags = normalize_tags(new_tags_input)

    # Get new due date (keep current if empty input)
    current_due_date = task.get('due_date', '')
    new_due_date_input = input(f"Enter new due date (current: '{current_due_date}', YYYY-MM-DD, MM/DD/YYYY, or relative terms like 'tomorrow', press Enter to keep current): ").strip()
    new_due_date = None
    if not new_due_date_input:
        new_due_date = task.get('due_date')
    elif new_due_date_input.lower() == 'none' or new_due_date_input.lower() == 'clear':
        new_due_date = None
    else:
        new_due_date_parsed = parse_datetime_input(new_due_date_input)
        if new_due_date_parsed:
            new_due_date = new_due_date_parsed.isoformat()
        else:
            print("⚠️  Invalid date format. Keeping current due date.")
            new_due_date = task.get('due_date')

    # Get new recurring info (keep current if empty input)
    current_recurring = task.get('recurring', {})
    if current_recurring:
        recurring_str = f"interval: {current_recurring.get('interval', 'N/A')}, every: {current_recurring.get('every', 'N/A')}"
        if current_recurring.get('days'):
            recurring_str += f", days: {', '.join(current_recurring['days'])}"
    else:
        recurring_str = "None"
    
    update_recurring = input(f"Update recurrence? (current: {recurring_str}, y/N/clear): ").strip().lower()
    new_recurring = task.get('recurring')
    if update_recurring in ['y', 'yes']:
        print("Select recurrence pattern:")
        print("1. Daily")
        print("2. Weekly")
        print("3. Monthly")
        print("4. Yearly")
        print("5. Custom (every X days)")
        
        recurrence_choice = input("Enter choice (1-5): ").strip()
        
        new_recurring = {}
        if recurrence_choice == '1':
            new_recurring['interval'] = 'daily'
            new_recurring['every'] = 1
        elif recurrence_choice == '2':
            new_recurring['interval'] = 'weekly'
            new_recurring['every'] = 1
            # Ask for specific days of the week
            days_input = input("Enter days of the week (comma-separated, e.g., Monday, Wednesday): ").strip()
            if days_input:
                new_recurring['days'] = [day.strip().capitalize() for day in days_input.split(',')]
        elif recurrence_choice == '3':
            new_recurring['interval'] = 'monthly'
            new_recurring['every'] = 1
        elif recurrence_choice == '4':
            new_recurring['interval'] = 'yearly'
            new_recurring['every'] = 1
        elif recurrence_choice == '5':
            new_recurring['interval'] = 'custom'
            try:
                every_n = int(input("Repeat every how many days?: "))
                new_recurring['every'] = every_n
            except ValueError:
                print("Invalid number. Using default of 1 day.")
                new_recurring['every'] = 1
        else:
            print("Invalid choice. Keeping current recurrence.")
            new_recurring = task.get('recurring')
    elif update_recurring == 'clear':
        new_recurring = None

    # Update the task
    update_task(task_id, new_title, new_description, priority=new_priority, tags=new_tags, due_date=new_due_date, recurring=new_recurring)

    print(f"✅ Task with ID {task_id} updated successfully!")


def handle_delete_task():
    """
    Handles the process of deleting a task.
    """
    print("\n🗑️  Deleting a task...")
    
    tasks = get_all_tasks()
    
    if not tasks:
        print("📭 No tasks found to delete.")
        return
    
    # Show current tasks
    print("Current tasks:")
    for task in tasks:
        status = "[x]" if task["completed"] else "[ ]"
        print(f"ID: {task['id']} | {status} | Title: {task['title']}")
    
    try:
        task_id = int(input("\nEnter the ID of the task to delete: "))
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")
        return
    
    # Check if task exists
    task = get_task_by_id(task_id)
    if not task:
        print(f"❌ Task with ID {task_id} not found.")
        return
    
    # Confirm deletion
    confirm = input(f"Are you sure you want to delete task '{task['title']}'? (y/N): ").lower()
    if confirm != 'y':
        print("❌ Task deletion cancelled.")
        return
    
    # Delete the task
    delete_task(task_id)
    
    print(f"✅ Task with ID {task_id} deleted successfully!")


def handle_filter_tasks():
    """
    Handles the process of filtering tasks.
    """
    print("\n🔍 Filtering tasks...")
    print("Filter options:")
    print("1. Filter by status")
    print("2. Filter by priority")
    print("3. Filter by tag")
    print("4. Filter by overdue status")
    print("5. Filter by upcoming status")
    print("6. Filter by recurring status")
    print("7. Back to main menu")

    choice = input("Choose filter option (1-7): ").strip()

    if choice == '1':
        print("Filter by status:")
        print("1. Completed only")
        print("2. Incomplete only")
        print("3. All tasks")

        status_choice = input("Choose status filter (1-3): ").strip()

        if status_choice == '1':
            status = 'completed'
        elif status_choice == '2':
            status = 'incomplete'
        elif status_choice == '3':
            status = None  # All tasks
        else:
            print("❌ Invalid choice.")
            return

        filtered_tasks = filter_tasks(status=status)

    elif choice == '2':
        print("Filter by priority:")
        print("1. High priority")
        print("2. Medium priority")
        print("3. Low priority")

        priority_choice = input("Choose priority filter (1-3): ").strip()

        if priority_choice == '1':
            priority = 'High'
        elif priority_choice == '2':
            priority = 'Medium'
        elif priority_choice == '3':
            priority = 'Low'
        else:
            print("❌ Invalid choice.")
            return

        filtered_tasks = filter_tasks(priority=priority)

    elif choice == '3':
        tag = input("Enter tag to filter by: ").strip()
        if not tag:
            print("❌ Tag cannot be empty.")
            return

        filtered_tasks = filter_tasks(tag=tag)

    elif choice == '4':
        print("Filter by overdue status:")
        print("1. Overdue only")
        print("2. Not overdue only")
        print("3. All tasks")

        overdue_choice = input("Choose overdue filter (1-3): ").strip()

        if overdue_choice == '1':
            overdue = True
        elif overdue_choice == '2':
            overdue = False
        elif overdue_choice == '3':
            overdue = None  # All tasks
        else:
            print("❌ Invalid choice.")
            return

        filtered_tasks = filter_tasks(overdue=overdue)

    elif choice == '5':
        print("Filter by upcoming status:")
        print("1. Upcoming only")
        print("2. Not upcoming only")
        print("3. All tasks")

        upcoming_choice = input("Choose upcoming filter (1-3): ").strip()

        if upcoming_choice == '1':
            upcoming = True
        elif upcoming_choice == '2':
            upcoming = False
        elif upcoming_choice == '3':
            upcoming = None  # All tasks
        else:
            print("❌ Invalid choice.")
            return

        filtered_tasks = filter_tasks(upcoming=upcoming)

    elif choice == '6':
        print("Filter by recurring status:")
        print("1. Recurring only")
        print("2. Non-recurring only")
        print("3. All tasks")

        recurring_choice = input("Choose recurring filter (1-3): ").strip()

        if recurring_choice == '1':
            recurring = True
        elif recurring_choice == '2':
            recurring = False
        elif recurring_choice == '3':
            recurring = None  # All tasks
        else:
            print("❌ Invalid choice.")
            return

        filtered_tasks = filter_tasks(recurring=recurring)

    elif choice == '7':
        return  # Go back to main menu

    else:
        print("❌ Invalid choice.")
        return

    if not filtered_tasks:
        print(f"📭 No tasks found matching the filter criteria.")
        return

    print(f"\nFiltered tasks ({len(filtered_tasks)} found):")
    # Print header for better readability
    print(f"{'ID':<4} | {'Status':<7} | {'Pri':<4} | {'Due Date':<12} | {'Title':<25} | Tags | Recurrence")
    print("-" * 120)

    for task in filtered_tasks:
        status = "[x]" if task["completed"] else "[ ]"
        priority_indicator = get_priority_indicator(task['priority'])
        
        # Format due date
        due_date_str = ""
        if task.get('due_date'):
            try:
                dt = datetime.datetime.fromisoformat(task['due_date'].replace('Z', '+00:00'))
                due_date_str = dt.strftime("%Y-%m-%d")
                
                # Add visual indicators for overdue, today, or upcoming tasks
                if is_task_overdue(task):
                    due_date_str = f"[OVERDUE: {due_date_str}]"
                elif is_task_due_today(task):
                    due_date_str = f"[TODAY: {due_date_str}]"
                elif is_task_upcoming(task):
                    due_date_str = f"[UPCOMING: {due_date_str}]"
            except ValueError:
                due_date_str = task['due_date'][:10]  # Just show the date part
        
        tags_str = f"{', '.join(task['tags'])}" if task['tags'] else ""

        # Format recurrence info
        recurrence_str = ""
        if task.get('recurring'):
            recurring_info = task['recurring']
            interval = recurring_info.get('interval', 'Unknown')
            every = recurring_info.get('every', 1)
            if interval == 'daily':
                recurrence_str = f"Daily" if every == 1 else f"Every {every} days"
            elif interval == 'weekly':
                recurrence_str = f"Weekly" if every == 1 else f"Every {every} weeks"
                if 'days' in recurring_info:
                    recurrence_str += f" on {', '.join(recurring_info['days'])}"
            elif interval == 'monthly':
                recurrence_str = f"Monthly" if every == 1 else f"Every {every} months"
            elif interval == 'yearly':
                recurrence_str = f"Yearly" if every == 1 else f"Every {every} years"
            elif interval == 'custom':
                recurrence_str = f"Every {every} days"
            else:
                recurrence_str = f"Every {every} {interval}"

        # Truncate title if too long
        title = task['title'][:23] + ".." if len(task['title']) > 25 else task['title']

        print(f"{task['id']:<4} | {status:<7} | {priority_indicator:<4} | {due_date_str:<12} | {title:<25} | {tags_str} | {recurrence_str}")

        if task["description"]:
            print(f"       Description: {task['description']}")
        print()


def handle_sort_tasks():
    """
    Handles the process of sorting tasks.
    """
    print("\n📊 Sorting tasks...")
    print("Sort options:")
    print("1. Sort by priority (High first)")
    print("2. Sort alphabetically by title")
    print("3. Sort by creation order (ID)")
    print("4. Sort by due date")
    print("5. Back to main menu")

    choice = input("Choose sort option (1-5): ").strip()

    if choice == '1':
        sort_by = 'priority'
    elif choice == '2':
        sort_by = 'title'
    elif choice == '3':
        sort_by = 'id'
    elif choice == '4':
        sort_by = 'due_date'
    elif choice == '5':
        return  # Go back to main menu
    else:
        print("❌ Invalid choice.")
        return

    # Get all tasks and sort them
    all_tasks = get_all_tasks()
    sorted_tasks = sort_tasks(all_tasks, sort_by)

    if not sorted_tasks:
        print("📭 No tasks found.")
        return

    print(f"\nSorted tasks ({len(sorted_tasks)} found) - Sorted by {sort_by}:")
    # Print header for better readability
    print(f"{'ID':<4} | {'Status':<7} | {'Pri':<4} | {'Due Date':<12} | {'Title':<25} | Tags | Recurrence")
    print("-" * 120)

    for task in sorted_tasks:
        status = "[x]" if task["completed"] else "[ ]"
        priority_indicator = get_priority_indicator(task['priority'])
        
        # Format due date
        due_date_str = ""
        if task.get('due_date'):
            try:
                dt = datetime.datetime.fromisoformat(task['due_date'].replace('Z', '+00:00'))
                due_date_str = dt.strftime("%Y-%m-%d")
                
                # Add visual indicators for overdue, today, or upcoming tasks
                if is_task_overdue(task):
                    due_date_str = f"[OVERDUE: {due_date_str}]"
                elif is_task_due_today(task):
                    due_date_str = f"[TODAY: {due_date_str}]"
                elif is_task_upcoming(task):
                    due_date_str = f"[UPCOMING: {due_date_str}]"
            except ValueError:
                due_date_str = task['due_date'][:10]  # Just show the date part
        
        tags_str = f"{', '.join(task['tags'])}" if task['tags'] else ""

        # Format recurrence info
        recurrence_str = ""
        if task.get('recurring'):
            recurring_info = task['recurring']
            interval = recurring_info.get('interval', 'Unknown')
            every = recurring_info.get('every', 1)
            if interval == 'daily':
                recurrence_str = f"Daily" if every == 1 else f"Every {every} days"
            elif interval == 'weekly':
                recurrence_str = f"Weekly" if every == 1 else f"Every {every} weeks"
                if 'days' in recurring_info:
                    recurrence_str += f" on {', '.join(recurring_info['days'])}"
            elif interval == 'monthly':
                recurrence_str = f"Monthly" if every == 1 else f"Every {every} months"
            elif interval == 'yearly':
                recurrence_str = f"Yearly" if every == 1 else f"Every {every} years"
            elif interval == 'custom':
                recurrence_str = f"Every {every} days"
            else:
                recurrence_str = f"Every {every} {interval}"

        # Truncate title if too long
        title = task['title'][:23] + ".." if len(task['title']) > 25 else task['title']

        print(f"{task['id']:<4} | {status:<7} | {priority_indicator:<4} | {due_date_str:<12} | {title:<25} | {tags_str} | {recurrence_str}")

        if task["description"]:
            print(f"       Description: {task['description']}")
        print()


def handle_search_tasks():
    """
    Handles the process of searching tasks.
    """
    print("\n🔍 Searching tasks...")

    keyword = input("Enter keyword to search in title or description: ").strip()

    if not keyword:
        print("❌ Search keyword cannot be empty.")
        return

    matching_tasks = search_tasks(keyword)

    if not matching_tasks:
        print(f"📭 No tasks found containing '{keyword}'.")
        return

    print(f"\nFound {len(matching_tasks)} task(s) containing '{keyword}':")
    # Print header for better readability
    print(f"{'ID':<4} | {'Status':<7} | {'Pri':<4} | {'Title':<25} | Tags")
    print("-" * 80)

    for task in matching_tasks:
        status = "[x]" if task["completed"] else "[ ]"
        priority_indicator = get_priority_indicator(task['priority'])
        tags_str = f"{', '.join(task['tags'])}" if task['tags'] else ""
        
        # Truncate title if too long
        title = task['title'][:23] + ".." if len(task['title']) > 25 else task['title']
        
        print(f"{task['id']:<4} | {status:<7} | {priority_indicator:<4} | {title:<25} | {tags_str}")

        if task["description"]:
            print(f"       Description: {task['description']}")
        print()


def handle_view_overdue_tasks():
    """
    Handles the process of viewing overdue tasks.
    """
    print("\n📋 Viewing overdue tasks...")

    tasks = get_all_tasks()
    overdue_tasks = [task for task in tasks if is_task_overdue(task)]

    if not overdue_tasks:
        print("📭 No overdue tasks found.")
        return

    print(f"\nOverdue tasks: {len(overdue_tasks)}")
    # Print header for better readability
    print(f"{'ID':<4} | {'Status':<7} | {'Pri':<4} | {'Due Date':<12} | {'Title':<25} | Tags | Recurrence")
    print("-" * 120)

    for task in overdue_tasks:
        status = "[x]" if task["completed"] else "[ ]"
        priority_indicator = get_priority_indicator(task['priority'])
        
        # Format due date
        due_date_str = ""
        if task.get('due_date'):
            try:
                dt = datetime.datetime.fromisoformat(task['due_date'].replace('Z', '+00:00'))
                due_date_str = dt.strftime("%Y-%m-%d")
            except ValueError:
                due_date_str = task['due_date'][:10]  # Just show the date part
        
        tags_str = f"{', '.join(task['tags'])}" if task['tags'] else ""

        # Format recurrence info
        recurrence_str = ""
        if task.get('recurring'):
            recurring_info = task['recurring']
            interval = recurring_info.get('interval', 'Unknown')
            every = recurring_info.get('every', 1)
            if interval == 'daily':
                recurrence_str = f"Daily" if every == 1 else f"Every {every} days"
            elif interval == 'weekly':
                recurrence_str = f"Weekly" if every == 1 else f"Every {every} weeks"
                if 'days' in recurring_info:
                    recurrence_str += f" on {', '.join(recurring_info['days'])}"
            elif interval == 'monthly':
                recurrence_str = f"Monthly" if every == 1 else f"Every {every} months"
            elif interval == 'yearly':
                recurrence_str = f"Yearly" if every == 1 else f"Every {every} years"
            elif interval == 'custom':
                recurrence_str = f"Every {every} days"
            else:
                recurrence_str = f"Every {every} {interval}"

        # Truncate title if too long
        title = task['title'][:23] + ".." if len(task['title']) > 25 else task['title']

        print(f"{task['id']:<4} | {status:<7} | {priority_indicator:<4} | {due_date_str:<12} | {title:<25} | {tags_str} | {recurrence_str}")

        if task["description"]:
            print(f"       Description: {task['description']}")
        print()


def handle_view_upcoming_tasks():
    """
    Handles the process of viewing upcoming tasks.
    """
    print("\n📋 Viewing upcoming tasks...")

    tasks = get_all_tasks()
    upcoming_tasks = [task for task in tasks if is_task_upcoming(task)]

    if not upcoming_tasks:
        print("📭 No upcoming tasks found.")
        return

    print(f"\nUpcoming tasks: {len(upcoming_tasks)}")
    # Print header for better readability
    print(f"{'ID':<4} | {'Status':<7} | {'Pri':<4} | {'Due Date':<12} | {'Title':<25} | Tags | Recurrence")
    print("-" * 120)

    for task in upcoming_tasks:
        status = "[x]" if task["completed"] else "[ ]"
        priority_indicator = get_priority_indicator(task['priority'])
        
        # Format due date
        due_date_str = ""
        if task.get('due_date'):
            try:
                dt = datetime.datetime.fromisoformat(task['due_date'].replace('Z', '+00:00'))
                due_date_str = dt.strftime("%Y-%m-%d")
            except ValueError:
                due_date_str = task['due_date'][:10]  # Just show the date part
        
        tags_str = f"{', '.join(task['tags'])}" if task['tags'] else ""

        # Format recurrence info
        recurrence_str = ""
        if task.get('recurring'):
            recurring_info = task['recurring']
            interval = recurring_info.get('interval', 'Unknown')
            every = recurring_info.get('every', 1)
            if interval == 'daily':
                recurrence_str = f"Daily" if every == 1 else f"Every {every} days"
            elif interval == 'weekly':
                recurrence_str = f"Weekly" if every == 1 else f"Every {every} weeks"
                if 'days' in recurring_info:
                    recurrence_str += f" on {', '.join(recurring_info['days'])}"
            elif interval == 'monthly':
                recurrence_str = f"Monthly" if every == 1 else f"Every {every} months"
            elif interval == 'yearly':
                recurrence_str = f"Yearly" if every == 1 else f"Every {every} years"
            elif interval == 'custom':
                recurrence_str = f"Every {every} days"
            else:
                recurrence_str = f"Every {every} {interval}"

        # Truncate title if too long
        title = task['title'][:23] + ".." if len(task['title']) > 25 else task['title']

        print(f"{task['id']:<4} | {status:<7} | {priority_indicator:<4} | {due_date_str:<12} | {title:<25} | {tags_str} | {recurrence_str}")

        if task["description"]:
            print(f"       Description: {task['description']}")
        print()


def handle_view_recurring_tasks():
    """
    Handles the process of viewing recurring tasks.
    """
    print("\n📋 Viewing recurring tasks...")

    tasks = get_all_tasks()
    recurring_tasks = [task for task in tasks if task.get('recurring')]

    if not recurring_tasks:
        print("📭 No recurring tasks found.")
        return

    print(f"\nRecurring tasks: {len(recurring_tasks)}")
    # Print header for better readability
    print(f"{'ID':<4} | {'Status':<7} | {'Pri':<4} | {'Due Date':<12} | {'Title':<25} | Tags | Recurrence")
    print("-" * 120)

    for task in recurring_tasks:
        status = "[x]" if task["completed"] else "[ ]"
        priority_indicator = get_priority_indicator(task['priority'])
        
        # Format due date
        due_date_str = ""
        if task.get('due_date'):
            try:
                dt = datetime.datetime.fromisoformat(task['due_date'].replace('Z', '+00:00'))
                due_date_str = dt.strftime("%Y-%m-%d")
                
                # Add visual indicators for overdue, today, or upcoming tasks
                if is_task_overdue(task):
                    due_date_str = f"[OVERDUE: {due_date_str}]"
                elif is_task_due_today(task):
                    due_date_str = f"[TODAY: {due_date_str}]"
                elif is_task_upcoming(task):
                    due_date_str = f"[UPCOMING: {due_date_str}]"
            except ValueError:
                due_date_str = task['due_date'][:10]  # Just show the date part
        
        tags_str = f"{', '.join(task['tags'])}" if task['tags'] else ""

        # Format recurrence info
        recurrence_str = ""
        if task.get('recurring'):
            recurring_info = task['recurring']
            interval = recurring_info.get('interval', 'Unknown')
            every = recurring_info.get('every', 1)
            if interval == 'daily':
                recurrence_str = f"Daily" if every == 1 else f"Every {every} days"
            elif interval == 'weekly':
                recurrence_str = f"Weekly" if every == 1 else f"Every {every} weeks"
                if 'days' in recurring_info:
                    recurrence_str += f" on {', '.join(recurring_info['days'])}"
            elif interval == 'monthly':
                recurrence_str = f"Monthly" if every == 1 else f"Every {every} months"
            elif interval == 'yearly':
                recurrence_str = f"Yearly" if every == 1 else f"Every {every} years"
            elif interval == 'custom':
                recurrence_str = f"Every {every} days"
            else:
                recurrence_str = f"Every {every} {interval}"

        # Truncate title if too long
        title = task['title'][:23] + ".." if len(task['title']) > 25 else task['title']

        print(f"{task['id']:<4} | {status:<7} | {priority_indicator:<4} | {due_date_str:<12} | {title:<25} | {tags_str} | {recurrence_str}")

        if task["description"]:
            print(f"       Description: {task['description']}")
        print()


def handle_toggle_task_status():
    """
    Handles the process of toggling a task's completion status.
    """
    print("\n🔄 Toggling task status...")

    tasks = get_all_tasks()

    if not tasks:
        print("📭 No tasks found.")
        return

    # Show current tasks
    print("Current tasks:")
    for task in tasks:
        status = "[x]" if task["completed"] else "[ ]"
        print(f"ID: {task['id']} | {status} | Title: {task['title']}")

    try:
        task_id = int(input("\nEnter the ID of the task to toggle: "))
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")
        return

    # Check if task exists
    task = get_task_by_id(task_id)
    if not task:
        print(f"❌ Task with ID {task_id} not found.")
        return

    # Toggle the task status
    toggle_task_status(task_id)

    new_status = "[x]" if task["completed"] else "[ ]"
    print(f"✅ Task '{task['title']}' status updated to {new_status}!")