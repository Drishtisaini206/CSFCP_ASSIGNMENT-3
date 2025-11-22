Development Process and Tools Usage
The project followed a structured development approach, leveraging modern tools (VS Code, Python, Git, and GitHub) to ensure stability, clarity, and effective version control.
1. Development Environment
The entire project was built using Python and Visual Studio Code (VS Code).
Integrated Terminal: VS Code's terminal was essential for executing the Python script (python calculator.py) and for running all necessary Git commands without needing to switch applications.
Code Structure: The project was structured to separate source code (calculator.py), documentation (docs/), and configuration (.gitignore, README.md).
2. Code Implementation (calculator.py)
The Python code was implemented with an emphasis on modularity and robustness.
A. Modular Design
The core logic is broken down into four distinct functions (add, subtract, multiply, divide). This modular approach simplifies testing and maintenance. The main calculator logic then calls these functions based on user choice.
B. Robust Error Handling (Crucial for Reliability)
To ensure the calculator would not crash, two specific error-handling mechanisms were implemented:
Input Validation (try-except): A try...except ValueError block was implemented around the input() function to catch attempts by the user to enter text or symbols when a numeric value was required. This prevents the program from stopping unexpectedly.
Zero Division Prevention (if condition): The divide function includes a specific if num2 == 0: check to handle division by zero. Instead of allowing a Python error, it returns a friendly error message, maintaining program control.
3. Version Control Workflow (Git & GitHub)
Git was used throughout the development cycle to track every change, and GitHub was used for remote hosting as required by the assignment.
A. Setup and Configuration
.gitignore: This file was configured to exclude unnecessary local files (like __pycache__ and .vscode/) from the remote repository, ensuring the repository remains clean and professional.
Commit Frequency: The project was managed using multiple, atomic commits to create a clear history of feature additions and bug fixes.
B. Resolving the First Push Conflict
The initial attempt to push the local project failed because the remote repository already contained files (README, license) that were not present in the local history. This required a specific solution to merge the unrelated histories:
git add . Staged all local files (code, documentation).
git commit -m "..." Saved the local changes.
git pull origin main --allow-unrelated-histories Fetched the remote changes and merged them with the local history to resolve the "rejected" error.
git push -u origin main Successfully uploaded the fully merged project to GitHub.

Commit added:
Commit 1 Initial project setup, including calculator.py, README.md, and .gitignore. Setup (Creating the foundation files)
Commit 2 Implemented add() and subtract() functions. Feature (Basic functionality)
Commit 3 Implemented multiply() and divide() with zero-division error handling. Feature (Completing core math)
Commit 4 Added the main_calculator() execution logic and user interface. Refactor (Adding the user menu and input loop)
Commit 5 Final testing and code cleanup, concluding the development phase. Fix/polish (Last review before final documentation)