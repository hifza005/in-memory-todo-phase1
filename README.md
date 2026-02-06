# Enhanced In-Memory Python Console Todo Application

An enhanced command-line todo list application with advanced organization and management features:
1. Add task (title + optional description + priority + tags)
2. View all tasks (show ID, status, priority, title, tags, and description)
3. Mark task complete / incomplete
4. Update task (title, description, priority, tags)
5. Delete task by ID
6. Search tasks (by keyword in title or description)
7. Filter tasks (by status, priority, or tag)
8. Sort tasks (by priority, title, or creation order)

## Features

- Pure Python 3.13+ implementation
- In-memory storage (list of dictionaries)
- Console-only interface (input/print)
- No external dependencies
- **Priority Management**: Assign High/Medium/Low priority to tasks
- **Tagging System**: Add one or more tags to categorize tasks
- **Search Functionality**: Search tasks by keyword in title or description
- **Filter Options**: Filter tasks by status, priority, or tag
- **Sorting Capabilities**: Sort tasks by priority, title, or creation order
- Clean, tabular display of tasks with priority indicators and tags

## Usage

Run the application with Python:

```bash
python src/main.py
```

Follow the on-screen menu to interact with your todo list:

1. **Add a new task**: Enter a title, optional description, priority level, and tags
2. **View all tasks**: See all tasks with their ID, status, priority, title, tags, and description
3. **Update a task**: Modify title, description, priority, or tags by entering task ID
4. **Delete a task**: Remove a task by entering task ID
5. **Mark task as complete/incomplete**: Toggle completion status by entering task ID
6. **Search tasks**: Find tasks containing a specific keyword in title or description
7. **Filter tasks**: Show only tasks that match specific criteria (status, priority, or tag)
8. **Sort tasks**: Arrange tasks in different orders based on priority, title, or creation order
9. **Exit**: Quit the application

### Priority Levels
- High (H/1): Highest priority tasks
- Medium (M/2): Medium priority tasks  
- Low (L/3): Lowest priority tasks

### Tagging
Tasks can be assigned multiple tags for better organization (e.g., work, personal, urgent).

## Project Structure

- `src/` - Source code files
  - `main.py` - Main application entry point with menu loop
  - `tasks.py` - Task management functions (add, update, delete, search, filter, sort, etc.)
  - `ui.py` - User interface functions (display, input handling, menu options)
- `tests/` - Test files
- `specs/` - Feature specifications
- `checklists/` - Quality checklists

## Development

This project follows spec-driven development principles using Spec-Kit Plus.