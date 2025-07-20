=============================
AUTO GIT PUSH SETUP - README
=============================

📂 FILES:
- git_auto_push_datasci.py  -> Auto-push for entire Data Science folder
- git_auto_push_excel.py    -> Auto-push for Excel subfolder only
- .gitignore                -> Ignores temp and system files
- README_setup.txt          -> You're reading it

📌 REQUIREMENTS:
- Git must be installed
- Python 3.x installed (verify with `python --version`)
- Git repo already initialized in your folders

⚙️ SETUP STEPS:

1. Edit the .py script file and make sure the folder path is correct.
2. Open Task Scheduler > Create Basic Task > Trigger: Daily > Repeat every: 10 minutes
3. Action: Start a Program
   - Program/script: path to your python.exe (usually in Program Files)
   - Add arguments: "D:\Data Science\git_auto_push_datasci.py" (or Excel one)
4. Finish > Test it manually once (Right-click > Run)

🧠 TIP:
Use `git status` anytime in Git Bash to see if your folder is being tracked properly.

✅ You're done. Automatic Git updates every 10 minutes!
