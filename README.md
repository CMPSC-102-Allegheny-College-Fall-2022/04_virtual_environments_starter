# Working in Virtual Environments

## Assigned: Tuesday, September 27, 2022

## Due: Tuesday, October 4, 2022

## Project Goals

In class, we have been talking about using virtual environments for the development of projects in computer science. Often developers will have several projects going at the same time where each project requires the same library but, perhaps, a different version of the library. With a virtual environment, all associated resources remain tied to specific projects, and do not haphazardly become inter-twined with other projects by accident.

- __Project Overview__: This _open_ engineering effort invites you to use virtual environments to build a professional-grade project having at least two different dependencies (other than `poetry` and `typer`), parameter-driven executable code in a driver source file (`main.py`), and meaningful and insightful documentation. The project is to have clear and meaningful documentation. You may choose the objectives of your project as long as they center around the goal of demonstrating some phenomena inspired by the libraries. Some of the points of this work are included below. You should be able to run your project using a command similar to; `poetry run myproject <parameters>`. For example, try `poetry run myproject --help` to see the help menu pop-up.

- __Virtual Environment__: The project must must use `poetry` to handle dependencies and its virtual envirnment requirements. The project must also use `typer` to handle at least two command-line parameters for integers, floating points, strings, bools or other to engage some functionality from your code. Your project will be _shipped_ using a pre-configured `poetry.lock` file to facilitate the user to setup an environment to run your code. In other words, the user will use the command, `poetry install` to install the virtual environment that your project utilizes. 

- __Source Code__: Your main source code file (`main.py`) is located in `myproject/myproject/`. Any other files that your project requires will be called from this driver file. Note: this project was created with the command, `poetry new myproject` and for convenience, some code has already been completed on the File `myproject/myproject/main.py`.

- __Dependancies__: Your project is to have two chosen dependancies, in addition to `poetry` and `typer`. You may choose any dependency such as; `scikit-learn`, `numpy`, `piglet`, or something else that attracts your interest. The body of the project code may come from the authors of the dependancies as long as the code is clearly cited. 

- __Documentation__: Your project must contain clear and meaningful language to help explain the goals of the project. You are to introduce the selected libraries and to clearly explain the demonstration and objectives of the code in your project. The documentation is also to facilitate the user in installing the virtual environment using `poetry install`, and to help the user run any other relevant commands to execute the project.


## Project Access

You can access this assignment by clicking the link provided to you in Discord or in the course schedule. Once you click this link it will create a GitHub repository that you can clone to your computer by using the `git clone` command to download the project from GitHub to your computer. Now you are ready to add source code and documentation to the project!

## Running Checks

Although not required for this lab, you can use the command `poetry run black myproject tests` to check your code in your Project (`myproject/`) to determine the readability of code using Black. If there are formatting problems, then Black will reformat the source code automatically.

By following a [tutorial](https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0), you can also configure your VS Code text editor to use the `black` tool to automatically reformat you source code every time you save a file.

Note: in addition to having software tests being run on GitHub, you can also run `gatorgrade --config config/gatorgrade.yml` locally on your machine to check your work in the same way. For example, if you see a red 'x' on your GitHub repository, then you can also learn why the build did not pass using a local check.

### Note

Do not forget that when you commit source code or technical writing to your GitHub repository for this project, it will trigger the run of a GitHub Actions workflow. If you are a student at Allegheny College, then running this workflow consumes build minutes for the organization of the course!

As such, we ask that you only commit to your repository once you have made substantive changes to your project and you are ready to confirm its correctness. Before you commit to your repository, you can still run checks on your own computer by either using Poetry or Docker and GatorGrader.

## Project Reflection

Once you have finished both of the previous technical tasks, you can use a text editor to answer all of the questions in the `writing/reflection.md` file. For instance, you should provide the output of the Python program in a fenced code block, explain the meaning of the Python source code segments that you implemented and used, and answer all of the other questions about your experiences in completing this project.

## Submission

As you are working on your lab, you are to commit and push regularly. The commands are the following.

```bash
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Assessment

The grade that a student receives on this assignment will have the following components.

- **GitHub Actions CI Build Status [up to 25%]:**: For the lab01 repository associated with this assignment students will receive a checkmark grade if their last before-the-deadline build passes. This is only checking some baseline writing and commit requirements as well as correct running of the program. An additional reduction will given if the commit log shows a cluster of commits at the end clearly used just to pass this requirement. An addition reduction will also be given if there is no commit during lab work times. All other requirements are evaluated manually.

- **Mastery of Technical Writing [up to 25%]:**: Students will also receive a checkmark grade when the responses to the writing questions presented in the `reflection.md` reveal a proficiency of both writing skills and technical knowledge. To receive a checkmark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 50%]**: Students will receive a portion of their assignment grade when their program implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this assignment. As a part of this grade, the instructor will assess aspects of the programming including, but not limited to, the completeness and the correctness of the program and the use of effective source code comments.

## Seeking Assistance

Students who have questions about this project outside of the lab time are invited to ask them in the course's Discord channel or during instructor's or TL's office hours.
