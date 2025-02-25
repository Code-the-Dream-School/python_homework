# Repository for Code the Dream Python 100 Homework

Before using this repository, you must install Python and must complete the rest of the setup as described in Python Essentials Lesson 1. Several steps are needed to configure VSCode, and you need to have installed the virtualenv pip package.

To use this repository:

1. Sign into your GitHub, and create a repository called python_homework.  It must be a public repository.  Do not create a .gitignore or a README.md.
2. On your computer, clone the [https://github.com/Code-the-Dream-School/python_homework](https://github.com/Code-the-Dream-School/python_homework) repository. (Do not clone the repository you just created.)
3. Change to the python_homework directory you just cloned.  Enter the following commands:
```shell
# if you use ssh authentication:
git remote set-url origin git@github.com/your-github-id/python_homework
# if you use token based authentication:
git remote set-url origin https://github.com/your-github-id/python_homework

git remote add upstream https://github.com/Code-the-Dream-School/python_homework
git push origin main
```
4. While still within the python_homework directory, enter the following commands:
```shell
python -m venv .venv
source .venv/bin/activate
code .
```
For some environments, you have to use the `python3` command.  For Windows users (you should use Git Bash in Windows), the command is different:
```shell
python -m venv .venv
source .venv/Scripts/activate
code .
```
4. Important: Open the VSCode command pallette (ctrl-shift P).  In the `Python: Select Interpreter` option, choose the one with `.venv`.  You can use the search box at the top to find it.  If you have any terminal sessions open, close them, and open a new one.  You will see `(.venv)` in your terminal prompt.
5. From the VSCode terminal session, enter the command:
```shell
pip install -r requirements.txt
```

Once this is done, you are ready to create your assignment1 git branch.  You create a separate branch for each lesson.  The assignment2 branch is created when the assignment1 branch is active, so that the lessons build on one another.  The files you create or modify for each assignment are described in the assignment itself.  They are to be created in the root of your python_homework repository, unless the lesson specifies otherwise.

In some cases, you will need to install additional pip packages to complete the lesson.

When you have completed the lesson, add and commit your changes and push them to your GitHub.  Then create a pull request.

Once you have created the pull request, include a link for the pull request in your homework submission.  Your reviewer will be notified, and will approve your request or ask for rework.  **Do not merge your pull request until your reviewer has approved it.**

Good luck with the class!