# Python Tutorials
Example projects from various places to work on various skills and coding practices in python

## About This Repository
Each folder is a self-contained project that was derived from a book or website to help learn new things or improve coding practices.
Within each folder will be a README and a requirements file if needed for setting up a specific virtual environment.

## Virtual Environments
Virtual environments ensure you use the appropriate versions of packages -- and the correct packages -- for a given project or codebase. They also provide a way to avoid needing to install all packages within the base python system and potentially causing issues down the road. Virtual environments are easily created and easily deleted, making them ideal in learning (and other) environments when containerizing may not be necessary.

To create a virtual environment, I recommend specifying a folder separate from your project to house the environment. If you prefer it to be in the same directory as your project, be sure it isn't tracked by git as they become quite large. I like to keep mine in one single folder called `pythonVirtualEnvs` and use the following commands to create and activate the environment.

1. Create the environment: `python -m venv "<path/to/env/<env-name>"`  
- **Note 1:** There are ways to go ahead and create an environment with all packages currently on your system. To use currently installed packages, include the `--system-site-packages` flag.
- **Note 2:** If you need a specific version of python, make sure it is available on your system then use the appropriate version for creation. For example: `python3.10 -m venv "<path/to/env/<env-name>"`
2. Activate the environment: `source /path/to/env/<env-name>/bin/activate`
3. Install packages with pip as normal or from a requirements file: `pip install -r <requirements-file>`
4. Create a requirements file if needed: `pip freeze > /path/to/file/<name-of-file.txt>`
5. Deactivate when done: `deactivate`

Alternatively, Anaconda can be used to manage and activate environments.