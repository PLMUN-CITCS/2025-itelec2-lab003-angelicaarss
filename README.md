# 2025-ITELEC2-WK02S01E01
Week 02 - Python Variables, Operators and I/O Statements

Exercise # 01 - Guided Coding Exercise: Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Exercise # 01 - Guided Coding Exercise: Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)**

   **Objective:**
   This exercise aims to solidify your understanding of variable declaration, data types (integers, floats, and strings), the crucial concept of case-sensitivity in Python, and best practices for variable naming. You will learn how to create variables, assign values of different types, observe how Python distinguishes between variables based on their case, and write code that is more readable and maintainable.

   **Desired Output:**
   ```txt
   Integer (count): 10
   Integer (total_count): 20
   Decimal: 3.14
   Text: Hello, Python!
   Boolean: True
   None Value: None
   ```
   **Notable Observations (to be discussed after completing the exercise):**
   - Python is case-sensitive. count and total_count are treated as distinct variables.
   - Variable names can be assigned and reassigned. The last assignment to a variable is the value it holds.
   - Different data types are used to represent different kinds of data (numbers vs. text).
   - Following naming conventions makes code more readable and understandable.

   **Best Practices for Variable Naming:**
   - Descriptive Names: Choose names that clearly indicate the variable's purpose (e.g., count instead of x, total_price instead of tp).
   - Lowercase with Underscores (Snake Case): Use lowercase letters and separate words with underscores (e.g., total_count, item_name, user_age). This is the most common and recommended convention in Python.
   - Avoid Single-Character Names (except for very short loops): Unless you're using a variable in a very limited scope (like a loop counter i), avoid single-letter names like a, b, or x. Descriptive names are much better.
   - Be Consistent: Stick to one naming convention throughout your code.
   - Avoid Reserved Keywords: Don't use Python's reserved keywords (e.g., for, while, if, else, print, class, def) as variable names.
   - Start with a Letter or Underscore: Variable names must start with a letter (a-z, A-Z) or an underscore (_). They cannot start with a number.
   - Can Contain Numbers: After the first character, variable names can contain letters, underscores, and numbers.
   
   **Literals:**
   A literal is a raw value that is directly written in the code. It represents a fixed value.
   - Examples:
      - 10 (integer literal)
      - 3.14 (floating-point literal)
      - "Hello, Python!" (string literal)
      - True (boolean literal)
      - None (None literal)
   
   **Step-by-Step Instructions:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `exercise_01.py`
      
   3. Create variables with numeric literals:
      - Declare a variable named `count` and assign it the integer literal `10`.
      - Declare another variable named `decimal_value` and assign it the floating-point literal `3.14`.
         ```python
         count = 10                  # 10 is an integer literal
         decimal_value = 3.14        # 3.14 is a float literal
         ```
      
   4. Create a variable with a string literal:
      - Declare a variable named `message` and assign it the string literal `"Hello, Python!"`.
         ```python
         message = "Hello, Python!"   # "Hello, Python!" is a string literal
         ```

   5. Create a variable with a boolean literal:
      - Declare a variable named `is_active` and assign it the boolean literal `True`.
         ```python
         is_active = True              # True is a boolean literal
         ```

   6. Create a variable with the None literal:
      - Declare a variable named result and assign it the `None` literal. `None` represents the absence of a value.
         ```python
         result = None                # None is the None literal
         ```

   7. Demonstrate case-sensitivity and reassignment:
      - Reassign the variable count to a new value (e.g., 10).
      - Declare a new variable named total_count and assign it a different value (e.g., 20).
         ```python
         count = 10                    # or any integer literal
         total_count = 20              # or any other integer literal
         ```

   8. Display the values:
      - Use the print() function to display the values of all variables, including the boolean and None variables. Include descriptive labels.
         ```python
         print("Integer (count):", count)
         print("Integer (total_count):", total_count)
         print("Decimal:", decimal_value)
         print("Text:", message)
         print("Boolean:", is_active)
         print("None Value:", result)
         ```
         
   9. Run the code: Execute your Python code.
   10. Observe the output: Compare your output with the "Desired Output" shown above.
   11. Discussion (Notable Observations):  Discuss the same points as before, and discuss the concept of literals.  How are they different from variables?  Why are they important?  Give examples of different types of literals.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
   ```bash
   git status
   ```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
   ```bash
   git add .
   ```
   
3. Commit your changes:
   Write a meaningful commit message:
   
   ```bash
   git commit -m "Submitting Python Week 02 - Session 01 - Exercise 01"
   ```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
   ```bash
   git push origin main
   ```
