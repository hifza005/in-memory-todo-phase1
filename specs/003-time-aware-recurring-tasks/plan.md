# Development Plan – Advanced Level - In-Memory Todo Console App

## Overview & Total Estimated Time

This plan outlines the implementation of advanced features for the in-memory Python console todo app, specifically focusing on due dates and recurring tasks. The implementation follows an incremental approach, building upon the existing basic and intermediate features while maintaining the clean, console-only interface.

**Total Estimated Time**: 8-10 hours for a solo developer

## Prerequisites / Current State Assumptions

- Working basic and intermediate todo app features (add/view/update/delete/mark, priority/tags/search/filter/sort)
- Modular structure with src/main.py, src/tasks.py, src/ui.py
- Python 3.13+ environment with standard library only
- Understanding of existing data model and UI flow
- UV virtual environment management

## Step-by-step Plan

### Phase 0: Research and Preparation (0.5 hours)

1. **Review current codebase structure**
   - Examine src/main.py, src/tasks.py, src/ui.py
   - Understand existing data model and task dictionary structure
   - Identify extension points for new features
   - Time estimate: 20 minutes

2. **Research datetime handling in Python standard library**
   - Explore datetime, time, and calendar modules
   - Identify best practices for date parsing and manipulation
   - Time estimate: 15 minutes

3. **Research recurrence pattern implementations**
   - Study common patterns for handling recurring tasks
   - Consider different interval types (daily, weekly, monthly, custom)
   - Time estimate: 15 minutes

### Phase 1: Data Model Updates (1 hour)

1. **Extend task data model**
   - Add 'due_date' field (datetime object or ISO string)
   - Add 'recurring' field (dictionary with interval information)
   - Update existing task creation functions to include new fields
   - Time estimate: 30 minutes

2. **Create helper functions for date operations**
   - Function to parse date/time input from user
   - Function to determine if a task is overdue
   - Function to determine if a task is due today
   - Function to determine if a task is upcoming
   - Time estimate: 30 minutes

### Phase 2: Due Date Implementation (2 hours)

1. **Update task creation flow**
   - Modify add_task function to accept optional due date
   - Add date input validation and parsing
   - Handle various date formats (YYYY-MM-DD, MM/DD/YYYY, relative terms)
   - Time estimate: 45 minutes

2. **Update task update flow**
   - Modify update_task function to allow due date modification
   - Add date input validation and parsing
   - Time estimate: 30 minutes

3. **Implement due date display logic**
   - Update view_tasks function to show due dates
   - Highlight overdue tasks with visual indicators
   - Highlight today's tasks with visual indicators
   - Highlight upcoming tasks with visual indicators
   - Time estimate: 45 minutes

### Phase 3: Recurring Task Implementation (2.5 hours)

1. **Design recurrence pattern structure**
   - Define format for storing recurrence information
   - Support for daily, weekly, monthly, custom intervals
   - Time estimate: 30 minutes

2. **Update task creation flow for recurring tasks**
   - Add option to make a task recurring during creation
   - Collect recurrence pattern from user
   - Store recurrence information in task dictionary
   - Time estimate: 45 minutes

3. **Implement recurring task completion logic**
   - When a recurring task is marked complete, create next occurrence
   - Calculate next due date based on recurrence pattern
   - Preserve other task properties in the new occurrence
   - Time estimate: 1 hour

4. **Update task display to show recurrence patterns**
   - Show recurrence information in task list view
   - Format recurrence information for readability
   - Time estimate: 15 minutes

### Phase 4: Filtering and Sorting Enhancements (1.5 hours)

1. **Add filtering options for time-sensitive tasks**
   - Filter for overdue tasks
   - Filter for upcoming tasks
   - Filter for recurring tasks
   - Time estimate: 45 minutes

2. **Enhance sorting capabilities**
   - Add option to sort by due date
   - Default sorting behavior when due dates are present
   - Time estimate: 30 minutes

3. **Update menu system**
   - Add new menu options for filtering time-sensitive tasks
   - Organize menu to accommodate new features
   - Time estimate: 15 minutes

### Phase 5: Validation and Error Handling (1 hour)

1. **Implement input validation**
   - Validate date formats and ranges
   - Validate recurrence patterns
   - Provide clear error messages for invalid inputs
   - Time estimate: 40 minutes

2. **Test edge cases**
   - Handle month-end dates in recurring tasks
   - Handle leap years in recurrence calculations
   - Handle invalid date combinations
   - Time estimate: 20 minutes

### Phase 6: Testing and Integration (1 hour)

1. **Manual testing of new features**
   - Test due date functionality end-to-end
   - Test recurring task functionality end-to-end
   - Test filtering and sorting features
   - Time estimate: 45 minutes

2. **Integration testing**
   - Ensure new features work with existing functionality
   - Verify no regressions in basic/intermediate features
   - Time estimate: 15 minutes

### Phase 7: Documentation and Finalization (0.5 hours)

1. **Update README.md**
   - Document new features and usage
   - Update any new run instructions
   - Time estimate: 20 minutes

2. **Update QWEN.md**
   - Add new prompts or commands used
   - Document new functionality
   - Time estimate: 10 minutes

3. **Final code review and cleanup**
   - Review code for consistency
   - Ensure adherence to project standards
   - Time estimate: 20 minutes

## Time Estimates Summary

- Research and Preparation: 0.5 hours
- Data Model Updates: 1 hour
- Due Date Implementation: 2 hours
- Recurring Task Implementation: 2.5 hours
- Filtering and Sorting Enhancements: 1.5 hours
- Validation and Error Handling: 1 hour
- Testing and Integration: 1 hour
- Documentation and Finalization: 0.5 hours

**Total Estimated Time: 9.5 hours**

## Final Deliverables Checklist

- [ ] Updated task data model with due_date and recurring fields
- [ ] Functionality to add/update tasks with due dates
- [ ] Visual indicators for overdue, today's, and upcoming tasks
- [ ] Functionality to create recurring tasks with various patterns
- [ ] Automatic creation of next occurrence when recurring task is completed
- [ ] Filtering options for time-sensitive tasks
- [ ] Sorting options by due date
- [ ] Input validation for dates and recurrence patterns
- [ ] Updated README.md with new features documentation
- [ ] Updated QWEN.md with new functionality
- [ ] All existing features continue to work without regression
- [ ] Clean, readable console interface maintained

## Tips for avoiding common datetime/recurrence pitfalls

1. **Date Parsing**: Use Python's datetime.strptime() with multiple format attempts to handle various user inputs gracefully.

2. **Timezone Handling**: Since this is a console app for a single user, stick to local time but be consistent in all operations.

3. **Month Boundary Issues**: When calculating next occurrence for monthly recurring tasks, handle months with different numbers of days appropriately (e.g., a task scheduled for January 31st shouldn't fail in February).

4. **Weekday Calculations**: Use Python's calendar module to properly calculate next occurrence for weekly patterns with specific weekdays.

5. **Performance**: For a console app, performance isn't critical, but avoid recalculating due date status repeatedly in loops.

6. **Validation**: Always validate user input for dates and recurrence patterns to prevent runtime errors.

7. **Testing**: Manually test edge cases like leap years, month boundaries, and different recurrence patterns to ensure robustness.