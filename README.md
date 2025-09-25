# 📝 Kanban Board (CLI-based)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)  
![Status](https://img.shields.io/badge/Status-Active-success)  
![License](https://img.shields.io/badge/License-MIT-green)  

A simple **command-line Kanban Board application** built in Python.  
This project allows users to create multiple boards, add tasks, assign priorities, and manage tasks interactively — all saved persistently using Python’s `pickle` module.  

---

## 🚀 Features

- **Multiple Boards**  
  Create and manage multiple Kanban boards.

- **Task Management**  
  - Add new tasks with a title and priority (`High`, `Medium`, `Low`).  
  - View tasks in a board.  
  - Remove tasks by task number.  
  - Print tasks sorted by priority.

- **Persistence**  
  Saves all boards and tasks automatically to `kanban.pkl` so your data is preserved between runs.

- **Interactive Menu**  
  User-friendly CLI menus for both **Boards** and **Tasks**.

---

## 📂 Project Structure
├── kanban.py # Main Python file
├── kanban.pkl # Auto-generated file for storing boards & tasks
└── README.md # Project documentation


1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. ```Run the program:
   python kanban.py
    ```
3. Follow the interactive menu

## Demo

```
Enter 1 to add Kanban Board
Enter 2 to view all boards
Enter 3 to select a board
Enter 4 to save and exit
> 1
Enter board name :
> GDSC Interview Prep

Enter 1 to add Task
Enter 2 to view tasks
Enter 3 to remove task
Enter 4 to print tasks according to priority
Enter any other no to go to Kanban Board menu
> 1
Enter Task Name: Revise Python
Enter priority of Task: High
```
