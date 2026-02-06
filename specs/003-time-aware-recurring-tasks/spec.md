# Specification – Advanced Level Features - In-Memory Todo Console App

**Feature Branch**: `003-time-aware-recurring-tasks`
**Created**: 2026-02-06
**Status**: Draft
**Input**: User description: "Advanced Level Features for In-Memory Python Console Todo App Target audience: Hackathon judges evaluating intelligent, real-world usable todo features on top of basic + intermediate level app Focus: Add smart, time-aware and recurring task capabilities to make the console todo app significantly more practical and advanced Success criteria: - All 2 major advanced features are fully implemented and work smoothly in console - Recurring tasks: support for repeating intervals (daily, weekly, monthly, custom days) - Due dates: user can set date + time for tasks - Reminders: show upcoming/overdue tasks prominently in view - Existing basic (add/view/update/delete/mark) + intermediate (priority/tags/search/filter/sort) features remain fully functional - Console remains clean, readable and user-friendly - Input validation for dates and recurring patterns - No external libraries (standard library only) - Still completely in-memory (no files/database/persistence) Constraints: - Python 3.13+ standard library only - Pure console interface (input/print) - Keep modular structure: src/main.py, src/tasks.py, src/ui.py - No GUI, no browser notifications (console-only reminders via view list) - No external packages (datetime, time modules are allowed) - Language: English for code, comments and UI Must include these features: 1. Recurring Tasks - When adding/updating a task, user can set it as recurring - Supported intervals: daily, weekly, monthly, every X days, custom weekdays - When a recurring task is marked complete, it auto-creates the next occurrence with updated due date - View list shows recurrence pattern (e.g. "Repeats weekly") 2. Due Dates & Time Reminders - Tasks can have optional due date + time (YYYY-MM-DD HH:MM format or simple input) - View list highlights: - Overdue tasks (red or marked) - Today's tasks - Upcoming tasks (tomorrow/this week) - Add "show upcoming" or "show overdue" filter/view option - Due date affects sorting (optional: sort by due date as default when present) Data Model Changes: - Add 'due_date' (datetime object or ISO string) - Add 'recurring' (dict or string pattern, e.g. {'interval': 'weekly', 'every': 7}) User Interface Flow: - Update add/update task flow to ask for due date/time and recurring option - Enhance view list to show due date/time and recurrence info - Add new menu options or flags: - Show overdue/upcoming - Show recurring tasks - Keep input simple and forgiving (accept various date formats if possible) Acceptance Criteria (examples): - User can create a task that repeats every Monday - Completing a recurring task creates next instance with shifted due date - Overdue tasks are clearly marked in view list - Tasks with due date sort correctly when chosen - All previous features continue to work without regression Output format: - Markdown document - Title: Specification – Advanced Level Features - In-Memory Todo Console App - Sections: - Overview & Goals - Data Model Changes (new fields + example task dict) - New/Updated Functional Requirements (detailed for recurring & due dates) - User Interface Flow (updated menu + input examples) - Acceptance Criteria (10–15 clear statements) - Edge Cases & Error Handling (invalid dates, recurring logic errors) - Non-functional notes (console readability, no libs, in-memory only) Write in clear, precise, actionable language. Output ONLY the markdown content — no extra explanation."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Schedule Recurring Tasks (Priority: P1)

As a busy professional, I want to schedule recurring tasks (like weekly team meetings, monthly reports, daily exercise) so that I don't have to manually recreate them each time they come up.

**Why this priority**: This is the core functionality that differentiates the app from basic todo lists and provides significant time savings for users managing repetitive tasks.

**Independent Test**: Can be fully tested by creating a recurring task with a specific interval and verifying that completing the task generates the next occurrence with an updated due date.

**Acceptance Scenarios**:

1. **Given** I have opened the todo app, **When** I add a new task and select the recurring option with a weekly interval, **Then** the task is saved with the recurrence pattern and appears in my task list.
2. **Given** I have a recurring task scheduled for today, **When** I mark it as complete, **Then** the next occurrence of the task is automatically created with the due date shifted by the recurrence interval.

---

### User Story 2 - Track Task Deadlines (Priority: P1)

As a user, I want to assign due dates and times to my tasks so that I can prioritize and manage my time effectively.

**Why this priority**: Setting deadlines is essential for task management and helps users stay organized and meet their commitments.

**Independent Test**: Can be fully tested by adding a task with a due date and verifying that it appears in the appropriate view (upcoming, overdue) based on the current date.

**Acceptance Scenarios**:

1. **Given** I have opened the todo app, **When** I add a new task with a due date, **Then** the task is saved with the due date and appears in my task list with the deadline visible.
2. **Given** I have tasks with various due dates, **When** I view the task list, **Then** overdue tasks are highlighted and upcoming tasks are clearly marked.

---

### User Story 3 - View Time-Sensitive Information (Priority: P2)

As a user, I want to quickly identify overdue and upcoming tasks so that I can prioritize my work effectively.

**Why this priority**: Visual cues for time-sensitive tasks help users focus on what needs immediate attention and prevent missed deadlines.

**Independent Test**: Can be fully tested by viewing the task list with various tasks having different due date statuses and verifying that overdue and upcoming tasks are appropriately highlighted.

**Acceptance Scenarios**:

1. **Given** I have tasks with past due dates, **When** I view my task list, **Then** overdue tasks are clearly marked with visual indicators.
2. **Given** I have tasks due today or in the near future, **When** I view my task list, **Then** these tasks are highlighted as upcoming.

---

### User Story 4 - Manage Recurrence Patterns (Priority: P2)

As a user, I want to set various recurrence patterns (daily, weekly, monthly, custom days) so that I can accommodate different types of recurring tasks.

**Why this priority**: Different tasks have different recurrence patterns, and supporting multiple patterns makes the app more versatile and useful.

**Independent Test**: Can be fully tested by creating tasks with different recurrence patterns and verifying that they appear correctly in the task list and generate subsequent occurrences as expected.

**Acceptance Scenarios**:

1. **Given** I want to create a recurring task, **When** I select a custom recurrence pattern like "every Monday", **Then** the task is saved with the correct pattern and appears in my task list.
2. **Given** I have a task with a custom recurrence pattern, **When** I mark it as complete, **Then** the next occurrence is created with the correct date based on the pattern.

---

### User Story 5 - Filter Tasks by Time Status (Priority: P3)

As a user, I want to filter my tasks to see only overdue or upcoming tasks so that I can focus on time-sensitive items.

**Why this priority**: Filtering capabilities enhance usability by allowing users to focus on specific subsets of tasks relevant to their current needs.

**Independent Test**: Can be fully tested by applying filters to the task list and verifying that only tasks matching the filter criteria are displayed.

**Acceptance Scenarios**:

1. **Given** I have various tasks with different due date statuses, **When** I apply an "overdue" filter, **Then** only tasks with past due dates are displayed.
2. **Given** I have various tasks with different due date statuses, **When** I apply an "upcoming" filter, **Then** only tasks with future due dates are displayed.

---

### Edge Cases

- What happens when a recurring task is marked complete on a day that doesn't align with its recurrence pattern (e.g., completing a "weekly on Mondays" task on a Wednesday)?
- How does the system handle invalid date inputs or recurrence patterns?
- What happens when a recurring task is marked complete close to month boundaries (e.g., a monthly task on January 31st)?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add due dates and times to tasks in YYYY-MM-DD HH:MM format or simple input
- **FR-002**: System MUST highlight overdue tasks in the task list view
- **FR-003**: System MUST highlight today's tasks in the task list view
- **FR-004**: System MUST highlight upcoming tasks (tomorrow/this week) in the task list view
- **FR-005**: System MUST allow users to set recurring intervals (daily, weekly, monthly, every X days, custom weekdays)
- **FR-006**: System MUST automatically create the next occurrence of a recurring task when the current one is marked complete
- **FR-007**: System MUST update the due date of the next occurrence based on the recurrence pattern when a recurring task is completed
- **FR-008**: System MUST display recurrence pattern information in the task list view (e.g., "Repeats weekly")
- **FR-009**: System MUST provide filtering options to show only overdue tasks
- **FR-010**: System MUST provide filtering options to show only upcoming tasks
- **FR-011**: System MUST provide filtering options to show only recurring tasks
- **FR-012**: System MUST validate date inputs and provide clear error messages for invalid dates
- **FR-013**: System MUST validate recurrence patterns and provide clear error messages for invalid patterns
- **FR-014**: System MUST sort tasks by due date when the user selects the due date sorting option
- **FR-015**: System MUST maintain all existing basic and intermediate features (add/view/update/delete/mark, priority/tags/search/filter/sort)

### Data Model Changes

- **due_date**: Optional datetime object or ISO string representing the task's deadline
- **recurring**: Optional dictionary or string pattern containing recurrence information (e.g. {'interval': 'weekly', 'every': 7, 'days': ['Monday']})

**Example Task Dictionary**:
```
{
    'id': 1,
    'title': 'Weekly team meeting',
    'description': 'Team sync meeting',
    'completed': False,
    'priority': 'Medium',
    'tags': ['work', 'meeting'],
    'due_date': '2026-02-13T10:00:00',  // ISO format
    'recurring': {
        'interval': 'weekly',
        'every': 1,
        'days': ['Friday']
    }
}
```

### Key Entities

- **Task**: Represents a user's task with optional due date and recurrence information
- **Due Date**: A timestamp indicating when the task is due, affecting its display and sorting
- **Recurrence Pattern**: Defines how often a task repeats and when the next occurrence should be created

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All recurring task features are fully implemented and work smoothly in console without crashes or unexpected behavior
- **SC-002**: All due date features are fully implemented and work smoothly in console without crashes or unexpected behavior
- **SC-003**: Users can create recurring tasks with any supported interval (daily, weekly, monthly, every X days, custom weekdays)
- **SC-004**: When a recurring task is marked complete, the next occurrence is automatically created with the correct updated due date
- **SC-005**: The task list view clearly highlights overdue tasks with visual indicators
- **SC-006**: The task list view clearly highlights today's tasks with visual indicators
- **SC-007**: The task list view clearly highlights upcoming tasks (tomorrow/this week) with visual indicators
- **SC-008**: Users can filter tasks to see only overdue tasks
- **SC-009**: Users can filter tasks to see only upcoming tasks
- **SC-010**: Users can filter tasks to see only recurring tasks
- **SC-011**: All existing basic (add/view/update/delete/mark) and intermediate (priority/tags/search/filter/sort) features remain fully functional
- **SC-012**: The console interface remains clean, readable and user-friendly with the addition of new features
- **SC-013**: Input validation prevents invalid dates and recurrence patterns with clear error messages
- **SC-014**: The application uses only Python 3.13+ standard library without external dependencies
- **SC-015**: The application remains completely in-memory without persistence to files or databases