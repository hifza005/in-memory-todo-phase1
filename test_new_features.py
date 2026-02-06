#!/usr/bin/env python3
"""
Test script to verify the new advanced features work correctly.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from tasks import *
from ui import *

def test_basic_functionality():
    """Test that basic functionality still works."""
    print("Testing basic functionality...")
    
    # Clear any existing tasks
    global tasks_storage
    tasks_storage.clear()  # Use clear() instead of reassignment
    
    # Add a simple task
    task = create_task("Test task", "This is a test task")
    add_task(task)
    
    # Verify task was added
    tasks = get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0]['title'] == "Test task"
    print("[OK] Basic task creation works")
    
    # Test updating a task
    update_task(tasks[0]['id'], title="Updated test task")
    updated_task = get_task_by_id(tasks[0]['id'])
    assert updated_task['title'] == "Updated test task"
    print("[OK] Task update works")
    
    # Test toggling task status
    toggle_task_status(tasks[0]['id'])
    toggled_task = get_task_by_id(tasks[0]['id'])
    assert toggled_task['completed'] == True
    print("[OK] Task toggle works")


def test_due_dates():
    """Test due date functionality."""
    print("\nTesting due date functionality...")
    
    # Clear any existing tasks
    global tasks_storage
    tasks_storage.clear()
    
    print(f"DEBUG: tasks_storage after reset: {tasks_storage}")
    
    # Add a task with a due date
    from datetime import datetime, timedelta
    future_date = datetime.now() + timedelta(days=2)
    task = create_task("Task with due date", "This task has a due date", due_date=future_date)
    add_task(task)
    
    # Verify the task was added with the due date
    tasks = get_all_tasks()
    print(f"DEBUG: Number of tasks after adding: {len(tasks)}")
    if len(tasks) > 0:
        print(f"DEBUG: First task: {tasks[0]}")
    assert len(tasks) == 1, f"Expected 1 task, got {len(tasks)}"
    assert tasks[0]['due_date'] is not None
    print("[OK] Task with due date creation works")
    
    # Test if task is upcoming
    assert is_task_upcoming(tasks[0]) == True
    print("[OK] Upcoming task detection works")
    
    # Test if task is overdue (should be false)
    assert is_task_overdue(tasks[0]) == False
    print("[OK] Overdue task detection works")
    
    # Test if task is due today (should be false)
    assert is_task_due_today(tasks[0]) == False
    print("[OK] Due today detection works")
    
    # Add a task that is overdue
    past_date = datetime.now() - timedelta(days=2)
    overdue_task = create_task("Overdue task", "This task is overdue", due_date=past_date)
    add_task(overdue_task)
    
    overdue_tasks = get_all_tasks()
    overdue_task_obj = overdue_tasks[1]  # Second task
    assert is_task_overdue(overdue_task_obj) == True
    print("[OK] Overdue task detection works correctly")


def test_recurrence():
    """Test recurrence functionality."""
    print("\nTesting recurrence functionality...")
    
    # Clear any existing tasks
    global tasks_storage
    tasks_storage.clear()
    
    # Add a recurring task
    from datetime import datetime, timedelta
    future_date = datetime.now() + timedelta(days=1)
    recurring_info = {
        'interval': 'daily',
        'every': 1
    }
    task = create_task(
        "Recurring task", 
        "This task recurs daily", 
        due_date=future_date,
        recurring=recurring_info
    )
    add_task(task)
    
    # Verify the task was added with recurrence info
    tasks = get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0]['recurring'] is not None
    assert tasks[0]['recurring']['interval'] == 'daily'
    print("[OK] Recurring task creation works")
    
    # Test calculating next occurrence
    next_occurrence = calculate_next_occurrence(tasks[0])
    assert next_occurrence is not None
    print("[OK] Next occurrence calculation works")


def test_filters_and_sorting():
    """Test filtering and sorting functionality."""
    print("\nTesting filtering and sorting functionality...")
    
    # Clear any existing tasks
    global tasks_storage
    tasks_storage.clear()
    
    from datetime import datetime, timedelta
    
    # Add various tasks
    future_date = datetime.now() + timedelta(days=3)
    past_date = datetime.now() - timedelta(days=3)
    
    # Add a regular task
    task1 = create_task("Regular task", "Just a regular task")
    add_task(task1)
    
    # Add a task with due date
    task2 = create_task("Task with due date", "Has a due date", due_date=future_date)
    add_task(task2)
    
    # Add an overdue task
    task3 = create_task("Overdue task", "This is overdue", due_date=past_date)
    add_task(task3)
    
    # Add a recurring task
    recurring_info = {'interval': 'weekly', 'every': 1}
    task4 = create_task("Recurring task", "This recurs", recurring=recurring_info)
    add_task(task4)
    
    # Test filtering
    overdue_tasks = filter_overdue_tasks()
    assert len(overdue_tasks) == 1
    assert overdue_tasks[0]['title'] == "Overdue task"
    print("[OK] Overdue task filtering works")
    
    upcoming_tasks = filter_upcoming_tasks()
    assert len(upcoming_tasks) == 1
    assert upcoming_tasks[0]['title'] == "Task with due date"
    print("[OK] Upcoming task filtering works")
    
    recurring_tasks = filter_recurring_tasks()
    assert len(recurring_tasks) == 1
    assert recurring_tasks[0]['title'] == "Recurring task"
    print("[OK] Recurring task filtering works")
    
    # Test sorting by due date
    all_tasks = get_all_tasks()
    print(f"DEBUG: All tasks before sorting: {[t['title'] for t in all_tasks]}")
    sorted_tasks = sort_tasks(all_tasks, 'due_date')
    print(f"DEBUG: Sorted tasks: {[t['title'] for t in sorted_tasks]}")
    # Check that tasks with due dates come before tasks without due dates
    # Find the first task without a due date in the sorted list
    first_task_without_due_date_idx = -1
    for i, task in enumerate(sorted_tasks):
        if task.get('due_date') is None:
            first_task_without_due_date_idx = i
            break
    
    # All tasks after this index should also not have due dates
    all_remaining_without_due_date = all(task.get('due_date') is None for task in sorted_tasks[first_task_without_due_date_idx:])
    
    assert first_task_without_due_date_idx != -1, "Expected at least one task without due date"
    assert all_remaining_without_due_date, "Tasks without due dates should come after tasks with due dates"
    print("[OK] Sorting by due date works")


def run_tests():
    """Run all tests."""
    print("Running tests for advanced todo features...\n")
    
    try:
        test_basic_functionality()
        test_due_dates()
        test_recurrence()
        test_filters_and_sorting()
        
        print("\nSUCCESS: All tests passed! The advanced features are working correctly.")
        return True
    except Exception as e:
        print(f"\nFAILURE: Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)