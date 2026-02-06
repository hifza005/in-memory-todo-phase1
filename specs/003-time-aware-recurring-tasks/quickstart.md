# Quickstart Guide - Advanced Todo Features

## Setup

1. Ensure you have Python 3.13+ installed
2. Navigate to the project directory
3. Activate your virtual environment (using UV as recommended):
   ```
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

## Running the Application

To run the advanced todo app with due dates and recurring tasks:

```
cd src
python main.py
```

## Key Features Overview

### Adding Tasks with Due Dates
- From the main menu, select "Add Task"
- Enter the task title and description
- When prompted, enter a due date in YYYY-MM-DD format (e.g., 2026-12-25) or leave blank
- Set priority and tags as usual

### Creating Recurring Tasks
- When adding a task, you'll be prompted if it should recur
- Choose recurrence pattern: daily, weekly, monthly, or custom
- For weekly patterns, specify days (e.g., Monday, Wednesday, Friday)
- For custom patterns, specify interval (e.g., every 3 days)

### Viewing Tasks
- The task list now shows due dates and recurrence patterns
- Overdue tasks are highlighted
- Today's tasks are specially marked
- Upcoming tasks are identified

### Completing Recurring Tasks
- When you mark a recurring task as complete, the app automatically creates the next occurrence
- The new occurrence will have an updated due date based on the recurrence pattern

### Filtering Tasks
- Use the filtering options to view only overdue, upcoming, or recurring tasks
- Access these options from the main menu

## Example Usage

1. Add a recurring task: "Water plants" that repeats every Tuesday and Thursday
2. Add a task with a due date: "Submit report" due on 2026-02-15
3. View your tasks to see the due date highlighting and recurrence information
4. Mark the "Water plants" task as complete - notice how the app creates the next occurrence