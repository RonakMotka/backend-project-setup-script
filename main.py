import os
import argparse

structure = {
    "files": [
        ".gitignore",
        "config.py",
        "config.template.py",
        "database.py",
        "dependencies.py",
        "main.py",
        "models.py",
        "README.md",
        "requirements.txt"
    ],
    "main_folders": [
        {
            "name": "uploads",
        },
        {
            "name": "libs",
            "files": ["utils.py"]
        },
        {
            "name": "routers",
            "next_dir": {
                "name": "admin",
                "next_dir": {
                    "name": "v1",
                    "files": ["schemas.py", "api.py"],
                    "next_dir": {
                        "name": "crud"
                    }
                }
            }
        }
    ]
}

def get_arguments():
    parser = argparse.ArgumentParser(description='Create a new project directory structure.')
    parser.add_argument('project', help='Name of your project')
    parser.add_argument('directory', help='Path to set up the new project')
    return parser.parse_args()

def create_file(path):
    open(path, 'a').close()

def create_directory_structure(folder, base_path):
    if "name" in folder:
        dir_name = os.path.join(base_path, folder["name"])
        os.makedirs(dir_name, exist_ok=True)
        create_file(os.path.join(dir_name, "__init__.py"))
        
        if "files" in folder:
            for file in folder["files"]:
                create_file(os.path.join(dir_name, file))
        
        if "next_dir" in folder:
            create_directory_structure(folder["next_dir"], dir_name)  

def main():
    args = get_arguments()
    project_path = os.path.join(args.directory, args.project)
    
    if os.path.exists(project_path):
        raise Exception("Project already exists!")
    
    os.makedirs(project_path)
    create_file(os.path.join(project_path, "__init__.py"))

    if "files" in structure:
        for file in structure["files"]:
            create_file(os.path.join(project_path, file))
    
    if "main_folders" in structure:
        for folder in structure["main_folders"]:
            create_directory_structure(folder, project_path)

if __name__ == "__main__":
    main()