# Development Plan – Intermediate Level - In-Memory Todo Console App

## Overview & Total Estimated Time

This plan outlines the development of intermediate features for the in-memory Python console todo app. The goal is to enhance the existing basic functionality with priority management, tagging, search, filtering, and sorting capabilities. The total estimated time for completing this plan is 10-12 hours for a solo developer.

## Prerequisites / Current State Assumptions

- Basic todo app is functional with Add, View, Update, Delete, and Mark Complete features
- Codebase consists of main.py, tasks.py, and ui.py modules
- Using Python 3.13+ with standard library only
- Data is stored in-memory only (no persistence)
- UV is available for environment management

## Step-by-Step Plan

### Phase 1: Review and Prepare (Time: 30 minutes)

1. **Review existing codebase**
   - Examine current data model in tasks.py
   - Understand UI flow in ui.py
   - Map out current menu structure in main.py
   - Time estimate: 15 minutes

2. **Plan data model updates**
   - Add priority field to task structure
   - Add tags field to task structure
   - Time estimate: 15 minutes

### Phase 2: Update Data Model (Time: 1 hour)

3. **Modify task creation function**
   - Update create_task() to include priority and tags fields
   - Set default priority to "Medium" and empty tags list
   - Time estimate: 30 minutes

4. **Update task manipulation functions**
   - Modify update_task() to handle priority and tags updates
   - Add helper functions for priority and tag validation
   - Time estimate: 30 minutes

### Phase 3: Implement Priority Feature (Time: 1.5 hours)

5. **Update UI for priority input**
   - Modify handle_add_task() to collect priority input
   - Modify handle_update_task() to allow priority updates
   - Time estimate: 45 minutes

6. **Enhance task display with priority**
   - Update handle_view_tasks() to show priority indicators
   - Format display to include priority markers [H], [M], [L]
   - Time estimate: 45 minutes

7. **Checkpoint: Test priority functionality**
   - Add tasks with different priorities
   - Verify priorities display correctly
   - Update existing tasks with priorities
   - Time estimate: 30 minutes

### Phase 4: Implement Tags Feature (Time: 1.5 hours)

8. **Update UI for tags input**
   - Modify handle_add_task() to collect tags input (comma-separated)
   - Modify handle_update_task() to allow tags updates
   - Time estimate: 45 minutes

9. **Enhance task display with tags**
   - Update handle_view_tasks() to show tags
   - Format display to include tags list
   - Time estimate: 30 minutes

10. **Checkpoint: Test tags functionality**
    - Add tasks with various tags
    - Verify tags display correctly
    - Update existing tasks with tags
    - Time estimate: 15 minutes

### Phase 5: Implement Search Feature (Time: 1.5 hours)

11. **Create search functionality**
    - Add search_tasks() function in tasks.py
    - Implement keyword search in title and description
    - Time estimate: 45 minutes

12. **Create search UI**
    - Add search option to main menu
    - Implement handle_search_tasks() in ui.py
    - Time estimate: 45 minutes

13. **Checkpoint: Test search functionality**
    - Add tasks with searchable keywords
    - Verify search returns correct results
    - Test with no matches scenario
    - Time estimate: 30 minutes

### Phase 6: Implement Filter Feature (Time: 2 hours)

14. **Create filter functionality**
    - Add filter_tasks() function in tasks.py
    - Support filtering by status, priority, and tag
    - Time estimate: 1 hour

15. **Create filter UI**
    - Add filter option to main menu
    - Implement handle_filter_tasks() in ui.py
    - Create submenu for filter options
    - Time estimate: 1 hour

16. **Checkpoint: Test filter functionality**
    - Apply different filters
    - Verify filtered lists are correct
    - Test combined filters
    - Time estimate: 30 minutes

### Phase 7: Implement Sort Feature (Time: 1.5 hours)

17. **Create sort functionality**
    - Add sort_tasks() function in tasks.py
    - Support sorting by priority, title, and creation order
    - Time estimate: 45 minutes

18. **Create sort UI**
    - Add sort option to main menu
    - Implement handle_sort_tasks() in ui.py
    - Create submenu for sort options
    - Time estimate: 45 minutes

19. **Checkpoint: Test sort functionality**
    - Apply different sorting options
    - Verify sorted lists are correct
    - Test with mixed priority tasks
    - Time estimate: 30 minutes

### Phase 8: Menu and Navigation Updates (Time: 1 hour)

20. **Update main menu**
    - Add new options for search, filter, sort
    - Reorganize menu for better flow
    - Time estimate: 30 minutes

21. **Implement submenu navigation**
    - Create submenu functions for filter and sort options
    - Ensure smooth navigation between menus
    - Time estimate: 30 minutes

### Phase 9: Polish and Testing (Time: 1.5 hours)

22. **Input validation and error handling**
    - Add validation for priority inputs
    - Add validation for tag inputs
    - Improve error messages
    - Time estimate: 45 minutes

23. **UI formatting improvements**
    - Align columns in task display
    - Improve readability of priority and tags
    - Add consistent formatting
    - Time estimate: 30 minutes

24. **Comprehensive manual testing**
    - Test all new features together
    - Verify existing functionality still works
    - Test edge cases
    - Time estimate: 45 minutes

### Phase 10: Documentation Updates (Time: 1 hour)

25. **Update README.md**
    - Document new features
    - Update run instructions
    - Add usage examples for new features
    - Time estimate: 30 minutes

26. **Update QWEN.md**
    - Add new prompts used during development
    - Document key implementation decisions
    - Time estimate: 30 minutes

## Time Estimates Summary

- Review and Preparation: 30 minutes
- Data Model Updates: 1 hour
- Priority Feature: 1.5 hours
- Tags Feature: 1.5 hours
- Search Feature: 1.5 hours
- Filter Feature: 2 hours
- Sort Feature: 1.5 hours
- Menu Updates: 1 hour
- Polish and Testing: 1.5 hours
- Documentation: 1 hour

**Total Estimated Time: 12 hours**

## Final Deliverables Checklist

- [ ] Task data model updated with priority and tags fields
- [ ] Priority functionality implemented (assign, display, sort)
- [ ] Tags functionality implemented (assign, display, filter)
- [ ] Search functionality implemented (keyword search)
- [ ] Filter functionality implemented (by status, priority, tag)
- [ ] Sort functionality implemented (by priority, title, creation order)
- [ ] Updated main menu with new options
- [ ] Input validation and error handling for new fields
- [ ] Improved UI formatting and readability
- [ ] Comprehensive manual testing completed
- [ ] README.md updated with new features
- [ ] QWEN.md updated with development prompts

## Tips for Staying Productive in Remaining Hackathon Time

1. **Focus on working increments**: Complete each feature fully before moving to the next
2. **Test frequently**: Run the app after each major change to catch issues early
3. **Keep it simple**: Use basic console formatting rather than complex UI elements
4. **Modular approach**: Work on one module (tasks.py, ui.py) at a time
5. **Leverage existing patterns**: Follow the same patterns used in the original code
6. **Time box each phase**: Don't spend more than the allocated time on any phase
7. **Have a backup plan**: If a complex feature takes too long, implement a simpler version