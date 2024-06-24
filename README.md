# Backend Project Setup Script

A script to automate the setup of your backend project file structure.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Customization](#customization)
- [Requirements](#requirements)
- [Installation](#installation)

## Description

This script automates the creation of a standardized backend project file structure tailored for the FastAPI framework. It generates directories and files based on a predefined template, ensuring consistency and saving time.

## Features

- Creates main project files such as `.gitignore`, `README.md`, `requirements.txt`, etc.
- Generates nested directories and files based on the specified structure.
- Automatically adds `__init__.py` files in directories to make them Python packages.

## Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/backend-project-setup-script.git
    cd backend-project-setup-script
    ```

2. **Run the script**:
    ```bash
    python setup_script.py <project_name> <directory_path>
    ```

    - `<project_name>`: The name of your project.
    - `<directory_path>`: The path where the project directory will be created.

    Example:
    ```bash
    python setup_script.py my_project /home/user/projects
    ```

## Project Structure

The script creates the following file structure:

project_name/
│
├── .gitignore
├── README.md
├── config.py
├── config.template.py
├── database.py
├── dependencies.py
├── main.py
├── models.py
├── requirements.txt
│
├── uploads/
│ └── init.py
│
├── libs/
│ ├── init.py
│ └── utils.py
│
└── routers/
├── init.py
└── admin/
├── init.py
└── v1/
├── init.py
├── api.py
├── schemas.py
└── crud/
└── init.py


## Customization

The default structure is designed for a FastAPI project, but you can easily customize it to fit your needs. Modify the `structure` dictionary in the script to add or remove files and directories as required.

## Requirements

- Python 3.6 or higher

## Installation

1. **Ensure you have Python installed**. You can download it from [python.org](https://www.python.org/).

2. **Clone this repository**:
    ```bash
    git clone https://github.com/yourusername/backend-project-setup-script.git
    ```

3. **Navigate to the project directory**:
    ```bash
    cd backend-project-setup-script
    ```

4. **Run the script** with the project name and directory path as arguments:
    ```bash
    python setup_script.py <project_name> <directory_path>
    ```
