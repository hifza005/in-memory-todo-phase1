# Data Model - Advanced Todo Features

## Task Entity

The Task entity is extended from the basic implementation to include due dates and recurrence information.

### Fields

- **id** (int): Unique identifier for the task
- **title** (str): The task title/description
- **description** (str): Detailed description of the task (optional)
- **completed** (bool): Whether the task is completed
- **priority** (str): Priority level (High, Medium, Low) - from intermediate features
- **tags** (list[str]): List of tags associated with the task - from intermediate features
- **due_date** (str or None): ISO format datetime string (YYYY-MM-DDTHH:MM:SS) indicating when the task is due
- **recurring** (dict or None): Dictionary containing recurrence information:
  - **interval** (str): Type of interval ('daily', 'weekly', 'monthly', 'yearly', 'custom')
  - **every** (int): Number of intervals to skip (e.g., every 2 weeks)
  - **days** (list[str], optional): Days of the week for weekly patterns (e.g., ['Monday', 'Wednesday'])
  - **on_day** (int, optional): Day of the month for monthly patterns
  - **end_date** (str, optional): ISO format date when recurrence should stop

### Example Task Dictionary

```
{
    'id': 1,
    'title': 'Weekly team meeting',
    'description': 'Team sync meeting',
    'completed': False,
    'priority': 'Medium',
    'tags': ['work', 'meeting'],
    'due_date': '2026-02-13T10:00:00',
    'recurring': {
        'interval': 'weekly',
        'every': 1,
        'days': ['Friday']
    }
}
```

### Validation Rules

- **due_date**: Must be a valid ISO format datetime string or None
- **recurring**: Must be a dictionary with required keys or None
- **id**: Must be unique across all tasks
- **priority**: Must be one of 'High', 'Medium', 'Low'
- **tags**: Must be a list of strings

### State Transitions

- **New Task**: Created with provided information, completed=False
- **Completed**: When marked complete, if recurring:
  - A new task is created with updated due date based on recurrence pattern
  - Original task is marked completed=True
- **Updated**: Properties can be modified except for id

### Relationships

- Tasks are independent entities with no direct relationships to other tasks
- Tags connect tasks through shared tag strings