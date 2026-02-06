# Quickstart Guide for Enhanced Todo Features

## Setting Up the Enhanced Todo App

1. Navigate to the project directory:
   ```
   cd D:\todo-app-phase1
   ```

2. Activate the virtual environment (if using UV):
   ```
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Using New Features

### Adding Tasks with Priority and Tags

When adding a task, you'll now be prompted for:
- Priority level (High, Medium, Low)
- Tags (comma-separated list)

Example: Add a task with "High" priority and tags "work,urgent"

### Viewing Tasks

Tasks now display with:
- Priority indicators: [H], [M], [L]
- Associated tags in parentheses

### Searching Tasks

Select the search option from the main menu and enter a keyword.
The app will display all tasks containing the keyword in title or description.

### Filtering Tasks

Access the filter submenu to filter by:
- Status (completed, incomplete, all)
- Priority (High, Medium, Low)
- Specific tag

### Sorting Tasks

Access the sort submenu to sort by:
- Priority (High first)
- Alphabetical (by title)
- Creation order (oldest first)

## Menu Navigation

The enhanced menu includes:
- Option 7: Search tasks
- Option 8: Filter tasks
- Option 9: Sort tasks
- Option 10: Return to main menu (from submenus)

## Example Workflow

1. Add a few tasks with different priorities and tags
2. Use search to find specific tasks
3. Filter by "work" tag to see only work-related tasks
4. Sort by priority to see most important tasks first
5. Update tasks to change priorities or tags as needed