# Specification – Intermediate Level Features - In-Memory Todo Console App

**Feature Branch**: `002-enhanced-todo-features`
**Created**: 2026-02-06
**Status**: Draft
**Input**: User description: "Intermediate Level Features for In-Memory Python Console Todo App Target audience: Hackathon judges and participants evaluating usability and organization improvements on top of a basic MVP todo app Focus: Extend the existing basic in-memory console todo app with better organization, searchability and sorting features to make it feel more practical and polished Success criteria: - All 3 new major areas are fully implemented and work smoothly in the console menu - Priorities: user can assign High/Medium/Low to tasks (or 1/2/3 numeric scale) - Tags/Categories: user can add one or more labels (work, personal, home, study, urgent, etc.) - Search: keyword search in title or description - Filter: by status (complete/incomplete), by priority, by tag/category - Sort: by priority (high first), by due date (if added), alphabetically by title - All new features are accessible via the existing main menu or sub-menus - Existing basic features (Add, View, Update, Delete, Mark Complete) remain fully functional - Input validation and helpful error messages for new fields - Console output remains clean and readable (use alignment, colors if possible without external libs) - Data still stored only in memory (no files/database) Constraints: - Python 3.13+ standard library only (no external packages) - Pure console interface (input/print only) - Keep modular structure: src/main.py, src/tasks.py, src/ui.py or similar - Do NOT add due dates unless explicitly requested (focus on priority, tags, search, filter, sort) - No persistence — everything still disappears when app closes - Language: English for code, comments and UI Must include these features: 1. Priority support - When adding or updating a task, user can set priority (High/Medium/Low or 3/2/1) - View list should show priority clearly (e.g. [H], [M], [L] or colored if possible) - Sort by priority (High → Medium → Low) 2. Tags / Categories - User can add one or more tags when creating/updating task (comma-separated input) - View list shows tags next to task - Filter tasks by one specific tag 3. Search - Search by keyword that appears in title OR description - Show matching tasks in a separate list or highlighted in main view 4. Filter options - Filter by status (only incomplete, only complete, all) - Filter by priority level - Filter by tag 5. Sort options - Sort by priority (descending) - Sort alphabetically by title - (optional) sort by creation order / ID if time allows Output format: - Markdown document - Title: Specification – Intermediate Level Features - In-Memory Todo Console App - Sections: - Overview & Goals - Data Model Changes (new fields: priority, tags) - New/Updated Functional Requirements (detailed for each feature) - User Interface Flow (updated main menu + sub-menus if needed) - Acceptance Criteria (10–15 clear statements) - Edge Cases & Error Handling - Non-functional notes (console readability, no external libs) Write in clear, precise, actionable language. Output ONLY the markdown content — no extra explanation."

## Overview & Goals

Extend the existing basic in-memory console todo app with advanced organization, searchability, and sorting features to enhance user productivity and task management capabilities. The goal is to transform the basic todo app into a more practical and polished tool that supports priority management, categorization with tags, and flexible filtering and sorting options.

## Data Model Changes

- **Priority Field**: Add a priority attribute to tasks with values of High/Medium/Low or 1/2/3 numeric scale
- **Tags Field**: Add a tags attribute to tasks allowing multiple labels (stored as a list of strings)
- **Task Status**: Maintain existing status field (complete/incomplete) for filtering purposes

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Assign and View Task Priority (Priority: P1)

A user wants to assign priority levels to tasks to identify which tasks need immediate attention. The user can set High/Medium/Low priority when creating or updating tasks, and the priority is clearly displayed when viewing the task list.

**Why this priority**: Critical for task organization and helping users focus on important tasks first.

**Independent Test**: Can be fully tested by adding tasks with different priority levels and verifying they appear with clear priority indicators in the list view.

**Acceptance Scenarios**:

1. **Given** user is on the add/update task screen, **When** user selects priority level (High/Medium/Low), **Then** the task is saved with the selected priority and displays the priority indicator in the task list
2. **Given** task list contains tasks with different priorities, **When** user views the list, **Then** each task shows its priority level clearly (e.g. [H], [M], [L])

---

### User Story 2 - Tag Tasks for Categorization (Priority: P1)

A user wants to categorize tasks using tags to group related activities (work, personal, home, study, urgent, etc.). The user can add one or more tags when creating or updating tasks, and the tags are displayed when viewing the task list.

**Why this priority**: Essential for organizing tasks into meaningful categories that reflect different aspects of a user's life or work.

**Independent Test**: Can be fully tested by adding tasks with various tags and verifying they appear with their tags in the list view.

**Acceptance Scenarios**:

1. **Given** user is on the add/update task screen, **When** user enters comma-separated tags, **Then** the task is saved with the tags and displays them in the task list
2. **Given** task list contains tasks with different tags, **When** user views the list, **Then** each task shows its associated tags clearly

---

### User Story 3 - Search Tasks by Keyword (Priority: P2)

A user wants to quickly find specific tasks by searching for keywords that appear in the task title or description. The system should return matching tasks in a separate list or highlight them in the main view.

**Why this priority**: Important for users with many tasks who need to quickly locate specific items without scrolling through long lists.

**Independent Test**: Can be fully tested by creating tasks with specific keywords and verifying search returns the correct results.

**Acceptance Scenarios**:

1. **Given** user has multiple tasks with various titles and descriptions, **When** user enters a search keyword, **Then** the system displays only tasks containing that keyword in title or description
2. **Given** user performs a search, **When** no tasks match the keyword, **Then** the system displays a clear message indicating no results found

---

### User Story 4 - Filter Tasks by Various Criteria (Priority: P2)

A user wants to filter the task list by status (complete/incomplete), priority level, or specific tag to focus on subsets of tasks that meet certain criteria.

**Why this priority**: Critical for managing large task lists by allowing users to focus on specific subsets relevant to their current needs.

**Independent Test**: Can be fully tested by applying different filters and verifying the task list updates accordingly.

**Acceptance Scenarios**:

1. **Given** task list contains both complete and incomplete tasks, **When** user applies "incomplete only" filter, **Then** only incomplete tasks are displayed
2. **Given** task list contains tasks with different priorities, **When** user applies "High priority" filter, **Then** only high priority tasks are displayed
3. **Given** task list contains tasks with various tags, **When** user applies "work" tag filter, **Then** only tasks tagged with "work" are displayed

---

### User Story 5 - Sort Tasks by Different Criteria (Priority: P3)

A user wants to sort the task list by priority (high first), alphabetically by title, or by creation order to better organize their view of tasks.

**Why this priority**: Enhances usability by allowing users to arrange tasks in ways that make sense for their workflow.

**Independent Test**: Can be fully tested by applying different sorting options and verifying the task order updates correctly.

**Acceptance Scenarios**:

1. **Given** task list contains tasks with various priorities, **When** user selects "sort by priority" option, **Then** tasks are arranged with high priority first, followed by medium, then low
2. **Given** task list contains multiple tasks, **When** user selects "sort alphabetically" option, **Then** tasks are arranged in alphabetical order by title

---

### Edge Cases

- What happens when a user enters invalid priority values?
- How does the system handle empty or malformed tags?
- What occurs when a search term matches multiple tasks?
- How does the system handle extremely long task titles or descriptions in the UI?
- What happens when a user tries to filter by a tag that doesn't exist on any tasks?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to assign priority (High/Medium/Low or 1/2/3) when creating or updating tasks
- **FR-002**: System MUST display priority indicators clearly in the task list view (e.g. [H], [M], [L])
- **FR-003**: System MUST allow users to add one or more tags when creating or updating tasks (comma-separated input)
- **FR-004**: System MUST display tags associated with each task in the task list view
- **FR-005**: System MUST provide keyword search functionality that searches in both title and description fields
- **FR-006**: System MUST filter tasks by status (complete/incomplete/all)
- **FR-007**: System MUST filter tasks by priority level (high, medium, low)
- **FR-008**: System MUST filter tasks by specific tag
- **FR-009**: System MUST sort tasks by priority (high first)
- **FR-010**: System MUST sort tasks alphabetically by title
- **FR-011**: System MUST sort tasks by creation order/ID
- **FR-012**: System MUST maintain all existing basic functionality (Add, View, Update, Delete, Mark Complete)
- **FR-013**: System MUST provide input validation and helpful error messages for new fields
- **FR-014**: System MUST maintain clean and readable console output with proper alignment
- **FR-015**: System MUST store all data in memory only (no file/database persistence)

### Key Entities

- **Task**: Represents a user task with title, description, status (complete/incomplete), priority (High/Medium/Low), and tags (list of strings)
- **Priority**: Enumerated values representing task importance (High, Medium, Low or 1, 2, 3)
- **Tag**: String labels used to categorize tasks (work, personal, home, study, urgent, etc.)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can assign priority levels to tasks with 100% success rate and see priority indicators displayed clearly in the task list
- **SC-002**: Users can add tags to tasks with 100% success rate and see tags displayed next to tasks in the list
- **SC-003**: Search functionality returns accurate results in under 1 second for task lists up to 100 tasks
- **SC-004**: All filtering options (status, priority, tag) update the task list in under 1 second
- **SC-005**: All sorting options (priority, alphabetical, creation order) rearrange the task list in under 1 second
- **SC-006**: 95% of users can successfully use all new features (priority, tags, search, filter, sort) on first attempt
- **SC-007**: Console output remains clean and readable with proper alignment of all elements including priority indicators and tags
- **SC-008**: All existing basic functionality (Add, View, Update, Delete, Mark Complete) continues to work without degradation
- **SC-009**: Input validation prevents invalid data entry and provides helpful error messages under 100ms
- **SC-010**: All new features are accessible through the existing main menu or intuitive submenu navigation

## Non-functional notes

- Console readability: Use consistent formatting, alignment, and clear indicators for priority and tags
- No external libraries: Implementation must use Python 3.13+ standard library only
- Memory-only storage: All data remains in memory and is lost when the application closes
- Clean UI: Maintain readable console output with appropriate spacing and formatting