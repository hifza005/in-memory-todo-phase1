---

description: "Task list template for feature implementation"
---

# Tasks: Console Todo Application

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan: src/, tests/, specs/, checklists/
- [X] T002 Initialize Python project with UV virtual environment
- [X] T003 [P] Create basic project files: README.md, QWEN.md, .gitignore

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T004 Define Task data structure in src/tasks.py (dictionary with ID, title, description, status)
- [X] T005 [P] Implement in-memory storage mechanism using list of dictionaries
- [X] T006 Create basic application skeleton with menu loop in src/main.py
- [X] T007 Implement input validation and error handling utilities

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with title and optional description

**Independent Test**: The application allows users to input a task title and optional description, assigns it a unique ID, marks it as incomplete by default, and displays it in the task list.

### Implementation for User Story 1

- [X] T008 [P] [US1] Create add_task() function in src/tasks.py to add tasks to in-memory storage
- [X] T009 [US1] Implement unique ID assignment for new tasks in src/tasks.py
- [X] T010 [US1] Create UI function for adding tasks in src/ui.py
- [X] T011 [US1] Integrate add task functionality with main menu in src/main.py
- [X] T012 [US1] Add validation to ensure task titles are not empty

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Display all tasks with their ID, completion status, title, and description

**Independent Test**: The application displays all tasks with their ID, title, completion status ([ ] for incomplete, [x] for complete), and description in a readable format.

### Implementation for User Story 2

- [X] T013 [P] [US2] Create get_all_tasks() function in src/tasks.py
- [X] T014 [US2] Create display_tasks() function in src/ui.py to format and print task list
- [X] T015 [US2] Handle empty list case with appropriate message in src/ui.py
- [X] T016 [US2] Integrate view tasks functionality with main menu in src/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Details (Priority: P2)

**Goal**: Allow users to update the title or description of a task by specifying its ID

**Independent Test**: The application allows users to specify a task ID and update its title or description while preserving other properties.

### Implementation for User Story 3

- [X] T017 [P] [US3] Create update_task() function in src/tasks.py
- [X] T018 [US3] Implement validation for task ID existence in src/tasks.py
- [X] T019 [US3] Create UI function for updating tasks in src/ui.py
- [X] T020 [US3] Integrate update task functionality with main menu in src/main.py

**Checkpoint**: User Stories 1, 2, and 3 should all work independently

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P2)

**Goal**: Allow users to delete tasks by specifying their ID

**Independent Test**: The application allows users to specify a task ID and removes that task from the list.

### Implementation for User Story 4

- [X] T021 [P] [US4] Create delete_task() function in src/tasks.py
- [X] T022 [US4] Implement validation for task ID existence in src/tasks.py
- [X] T023 [US4] Create UI function for deleting tasks in src/ui.py
- [X] T024 [US4] Integrate delete task functionality with main menu in src/main.py

**Checkpoint**: User Stories 1, 2, 3, and 4 should all work independently

---

## Phase 7: User Story 5 - Mark Tasks Complete/Incomplete (Priority: P2)

**Goal**: Allow users to mark tasks as complete or incomplete by specifying their ID

**Independent Test**: The application allows users to toggle the completion status of a task by specifying its ID.

### Implementation for User Story 5

- [X] T025 [P] [US5] Create toggle_task_status() function in src/tasks.py
- [X] T026 [US5] Implement validation for task ID existence in src/tasks.py
- [X] T027 [US5] Create UI function for marking tasks complete/incomplete in src/ui.py
- [X] T028 [US5] Integrate mark task functionality with main menu in src/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T029 [P] Add comprehensive error handling for all user inputs
- [X] T030 [P] Improve UI formatting and user experience
- [X] T031 [P] Handle all specified edge cases (empty list, invalid IDs, etc.)
- [X] T032 [P] Add input validation for very long titles/descriptions
- [X] T033 [P] Code cleanup and refactoring
- [X] T034 [P] Update README.md with usage instructions
- [X] T035 [P] Document AI prompts used in QWEN.md
- [X] T036 Run complete application test to validate all features work together

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in priority order (P1 → P2)
- **Polish (Final Phase)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Models before services
- Services before UI components
- UI components before menu integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, user stories can start (though in this case, they're implemented sequentially)
- All tasks within a user story that are marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch all parallelizable tasks for User Story 1 together:
Task: "[P] [US1] Create add_task() function in src/tasks.py to add tasks to in-memory storage"
Task: "[US1] Implement unique ID assignment for new tasks in src/tasks.py"
```

---

## Implementation Strategy

### MVP First (User Stories 1-2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add tasks)
4. Complete Phase 4: User Story 2 (View tasks)
5. **STOP and VALIDATE**: Test User Stories 1 and 2 together
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test with US1 → Deploy/Demo
4. Add User Story 3 → Test with US1/US2 → Deploy/Demo
5. Add User Story 4 → Test with previous stories → Deploy/Demo
6. Add User Story 5 → Test with all stories → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5

### Sequential Solo Strategy

For a solo developer:

1. Complete Setup + Foundational
2. Complete User Story 1 (Add tasks)
3. Complete User Story 2 (View tasks)
4. Complete User Story 3 (Update tasks)
5. Complete User Story 4 (Delete tasks)
6. Complete User Story 5 (Mark complete/incomplete)
7. Complete polish phase

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing (if tests are included)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence