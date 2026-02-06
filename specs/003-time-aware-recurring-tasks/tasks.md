# Implementation Tasks – Advanced Level - In-Memory Todo Console App

## Feature Overview

This document outlines the implementation tasks for adding advanced features to the in-memory Python console todo app, specifically focusing on due dates and recurring tasks. The implementation follows an incremental approach, building upon the existing basic and intermediate features while maintaining the clean, console-only interface.

## Phase 1: Setup

- [ ] T001 Create feature branch 003-time-aware-recurring-tasks
- [ ] T002 Review existing codebase structure in src/main.py, src/tasks.py, src/ui.py
- [ ] T003 Understand existing data model and task dictionary structure
- [ ] T004 Identify extension points for new features in the codebase

## Phase 2: Foundational Tasks

- [X] T005 [P] Extend task data model to include due_date field in src/tasks.py
- [X] T006 [P] Extend task data model to include recurring field in src/tasks.py
- [X] T007 [P] Create helper function to parse date/time input from user in src/tasks.py
- [X] T008 [P] Create helper function to determine if a task is overdue in src/tasks.py
- [X] T009 [P] Create helper function to determine if a task is due today in src/tasks.py
- [X] T010 [P] Create helper function to determine if a task is upcoming in src/tasks.py
- [X] T011 [P] Create helper function to calculate next occurrence based on recurrence pattern in src/tasks.py

## Phase 3: User Story 1 - Schedule Recurring Tasks (Priority: P1)

**Story Goal**: As a busy professional, I want to schedule recurring tasks (like weekly team meetings, monthly reports, daily exercise) so that I don't have to manually recreate them each time they come up.

**Independent Test**: Can be fully tested by creating a recurring task with a specific interval and verifying that completing the task generates the next occurrence with an updated due date.

- [X] T012 [US1] Update add_task function to include recurring option in src/tasks.py
- [X] T013 [US1] Implement recurrence pattern collection from user in src/tasks.py
- [X] T014 [US1] Store recurrence information in task dictionary in src/tasks.py
- [X] T015 [US1] Implement recurring task completion logic in src/tasks.py
- [X] T016 [US1] Create next occurrence with updated due date when recurring task is completed in src/tasks.py
- [X] T017 [US1] Preserve other task properties in the new occurrence in src/tasks.py
- [X] T018 [US1] Update UI to prompt for recurring task options in src/ui.py
- [X] T019 [US1] Test creating a recurring task and completing it to verify next occurrence is created

## Phase 4: User Story 2 - Track Task Deadlines (Priority: P1)

**Story Goal**: As a user, I want to assign due dates and times to my tasks so that I can prioritize and manage my time effectively.

**Independent Test**: Can be fully tested by adding a task with a due date and verifying that it appears in the appropriate view (upcoming, overdue) based on the current date.

- [X] T020 [US2] Update add_task function to accept optional due date in src/tasks.py
- [X] T021 [US2] Add date input validation and parsing in src/tasks.py
- [X] T022 [US2] Handle various date formats (YYYY-MM-DD, MM/DD/YYYY, relative terms) in src/tasks.py
- [X] T023 [US2] Update update_task function to allow due date modification in src/tasks.py
- [X] T024 [US2] Add date input validation for update operations in src/tasks.py
- [X] T025 [US2] Update UI to prompt for due date during task creation in src/ui.py
- [X] T026 [US2] Update UI to allow due date modification during task update in src/ui.py
- [X] T027 [US2] Test adding tasks with due dates and verifying they appear correctly

## Phase 5: User Story 3 - View Time-Sensitive Information (Priority: P2)

**Story Goal**: As a user, I want to quickly identify overdue and upcoming tasks so that I can prioritize my work effectively.

**Independent Test**: Can be fully tested by viewing the task list with various tasks having different due date statuses and verifying that overdue and upcoming tasks are appropriately highlighted.

- [X] T028 [US3] Update view_tasks function to show due dates in src/tasks.py
- [X] T029 [US3] Highlight overdue tasks with visual indicators in src/ui.py
- [X] T030 [US3] Highlight today's tasks with visual indicators in src/ui.py
- [X] T031 [US3] Highlight upcoming tasks with visual indicators in src/ui.py
- [X] T032 [US3] Format due date display for readability in src/ui.py
- [X] T033 [US3] Test viewing tasks with different due date statuses to verify highlighting works

## Phase 6: User Story 4 - Manage Recurrence Patterns (Priority: P2)

**Story Goal**: As a user, I want to set various recurrence patterns (daily, weekly, monthly, custom days) so that I can accommodate different types of recurring tasks.

**Independent Test**: Can be fully tested by creating tasks with different recurrence patterns and verifying that they appear correctly in the task list and generate subsequent occurrences as expected.

- [X] T034 [US4] Define format for storing recurrence information in src/tasks.py
- [X] T035 [US4] Support for daily, weekly, monthly, custom intervals in src/tasks.py
- [X] T036 [US4] Update task display to show recurrence patterns in src/ui.py
- [X] T037 [US4] Format recurrence information for readability in src/ui.py
- [X] T038 [US4] Implement logic for different recurrence patterns (daily, weekly, monthly, custom) in src/tasks.py
- [X] T039 [US4] Test creating tasks with different recurrence patterns to verify they work correctly

## Phase 7: User Story 5 - Filter Tasks by Time Status (Priority: P3)

**Story Goal**: As a user, I want to filter my tasks to see only overdue or upcoming tasks so that I can focus on time-sensitive items.

**Independent Test**: Can be fully tested by applying filters to the task list and verifying that only tasks matching the filter criteria are displayed.

- [X] T040 [US5] Add filtering function for overdue tasks in src/tasks.py
- [X] T041 [US5] Add filtering function for upcoming tasks in src/tasks.py
- [X] T042 [US5] Add filtering function for recurring tasks in src/tasks.py
- [X] T043 [US5] Update UI to provide filtering options in src/ui.py
- [X] T044 [US5] Integrate filtering functions with the main menu in src/main.py
- [X] T045 [US5] Test filtering functionality to verify it works correctly

## Phase 8: Enhancement - Sorting Capabilities

- [X] T046 [P] Add option to sort by due date in src/tasks.py
- [X] T047 [P] Implement default sorting behavior when due dates are present in src/tasks.py
- [X] T048 [P] Update UI to allow sorting by due date in src/ui.py
- [X] T049 [P] Test sorting functionality to verify it works correctly

## Phase 9: Validation and Error Handling

- [X] T050 Implement input validation for date formats in src/tasks.py
- [X] T051 Implement input validation for recurrence patterns in src/tasks.py
- [X] T052 Provide clear error messages for invalid date inputs in src/ui.py
- [X] T053 Provide clear error messages for invalid recurrence patterns in src/ui.py
- [X] T054 Handle month-end dates in recurring tasks in src/tasks.py
- [X] T055 Handle leap years in recurrence calculations in src/tasks.py
- [X] T056 Handle invalid date combinations in src/tasks.py
- [X] T057 Test edge cases to ensure robustness

## Phase 10: Integration and Testing

- [X] T058 Manual testing of due date functionality end-to-end
- [X] T059 Manual testing of recurring task functionality end-to-end
- [X] T060 Manual testing of filtering and sorting features
- [X] T061 Integration testing to ensure new features work with existing functionality
- [X] T062 Verify no regressions in basic/intermediate features
- [X] T063 Run complete application to verify all features work together

## Phase 11: Polish & Cross-Cutting Concerns

- [X] T064 Update README.md with new features documentation
- [X] T065 Update QWEN.md with new functionality
- [X] T066 Review code for consistency and adherence to project standards
- [X] T067 Update menu system to accommodate new features in src/ui.py
- [X] T068 Final code cleanup and documentation
- [X] T069 Commit changes with descriptive commit message

## Dependencies

- User Story 2 (Track Task Deadlines) must be completed before User Story 3 (View Time-Sensitive Information)
- User Story 1 (Schedule Recurring Tasks) and User Story 2 (Track Task Deadlines) can be developed in parallel
- User Story 4 (Manage Recurrence Patterns) depends on User Story 1 (Schedule Recurring Tasks)
- User Story 5 (Filter Tasks by Time Status) can be developed independently but benefits from completion of User Stories 2 and 3

## Parallel Execution Opportunities

- T005-T011 (Foundational tasks) can be executed in parallel as they work on different aspects of the data model
- T012-T018 (User Story 1) and T020-T026 (User Story 2) can be developed in parallel
- T040-T044 (Filtering) can be developed in parallel with other UI enhancements

## Implementation Strategy

1. **MVP First**: Implement User Story 2 (Track Task Deadlines) as the minimum viable product with just due date functionality
2. **Incremental Delivery**: Add recurring tasks functionality (User Story 1) in the next increment
3. **Enhancement Layer**: Add filtering, sorting, and visual indicators in subsequent increments
4. **Polish**: Complete documentation, error handling, and final testing