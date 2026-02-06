"""
Main module for the console todo application.
"""

from tasks import *
from ui import display_menu, get_user_choice, handle_add_task, handle_view_tasks, handle_update_task, handle_delete_task, handle_toggle_task_status, handle_search_tasks, handle_filter_tasks, handle_sort_tasks, display_invalid_input, handle_view_overdue_tasks, handle_view_upcoming_tasks, handle_view_recurring_tasks


def main():
    """
    Main function to run the console todo application.
    """
    print("Welcome to the Console Todo Application!")
    print("This application allows you to manage your tasks.")

    while True:
        # Display the menu
        display_menu()

        # Get user choice
        choice = get_user_choice()

        # Handle user choice
        if choice == '1':
            handle_add_task()
        elif choice == '2':
            handle_view_tasks()
        elif choice == '3':
            handle_update_task()
        elif choice == '4':
            handle_delete_task()
        elif choice == '5':
            handle_toggle_task_status()
        elif choice == '6':
            handle_search_tasks()
        elif choice == '7':
            handle_filter_tasks()
        elif choice == '8':
            handle_sort_tasks()
        elif choice == '9':
            handle_view_overdue_tasks()
        elif choice == '10':
            handle_view_upcoming_tasks()
        elif choice == '11':
            handle_view_recurring_tasks()
        elif choice == '12':
            print("Thank you for using the Console Todo Application. Goodbye!")
            break
        else:
            display_invalid_input()


if __name__ == "__main__":
    main()