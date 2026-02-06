# Data Model for Enhanced Todo Features

## Task Entity

The Task entity will be extended to include priority and tags fields while maintaining existing properties.

### Fields
- **id** (int): Unique identifier for the task (auto-generated)
- **title** (str): The title of the task (required)
- **description** (str): The description of the task (optional)
- **completed** (bool): Whether the task is completed (default False)
- **priority** (str): Priority level of the task (values: "High", "Medium", "Low"; default: "Medium")
- **tags** (list[str]): List of tags associated with the task (default: empty list)

### Validation Rules
- **title**: Cannot be empty or consist only of whitespace
- **priority**: Must be one of "High", "Medium", "Low" (case-insensitive)
- **tags**: Each tag must be a non-empty string with no leading/trailing whitespace

### State Transitions
- **completed**: Can transition from False to True or True to False via toggle operation
- **priority**: Can be updated to any valid priority value
- **tags**: Can be updated to any valid list of tags

## Priority Entity

Represents the priority level of a task.

### Values
- **High**: Highest priority tasks (displayed as [H])
- **Medium**: Medium priority tasks (displayed as [M])
- **Low**: Lowest priority tasks (displayed as [L])

## Tag Entity

Represents a category or label that can be associated with a task.

### Properties
- **name** (str): The name of the tag (non-empty, trimmed of whitespace)

### Constraints
- Tag names must be non-empty strings
- Duplicate tags on a single task should be removed
- Tag names should be normalized (lowercase, trimmed)