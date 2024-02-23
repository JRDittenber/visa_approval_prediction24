import os #creating folder and creating files 
from pathlib import Path

project_name = "us_visa_approval"

list_of_files = [
    
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evalutaion.py",
    f"{project_name}/components/model_pusher.py",    
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",    
    f"{project_name}/constants/__init__.py",    
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",   
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",   
    "app.py",
    "requests.txt",
    "Dockerfile",    
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/models.yaml", 
    "config/schemas.yaml",     
    
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":        
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):    
        with open(filepath, "w") as f:
            pass
    else: 
        print(f"File {filepath} already exists and is not empty")   
        


"""
This code snippet is designed to automate the setup of a project structure for a Python application, specifically aimed at creating a project named "us_visa_approval". It uses a combination of Python's os module and the pathlib library to create a series of directories and files that follow a conventional project layout. Here's a breakdown of its functionality:

1. **Imports and Initial Setup**:
   - The `os` module is imported to provide functions for interacting with the operating system, allowing the creation of directories and manipulation of paths.
   - The `Path` class from the `pathlib` module is imported to facilitate file path operations in an object-oriented way.

2. **Project Name and Structure Definition**:
   - A variable `project_name` is defined with the value "us_visa_approval", which is used as the root directory name for the project structure.
   - `list_of_files` contains a list of file paths, defined as strings. These paths include the project's directory structure (like `components`, `configuration`, `entity`, etc.) and file names. This structure mimics a typical layout for a Python project, with separate directories for different aspects of the project (data ingestion, validation, model training, etc.) and special files for configuration, Docker setup, and Python packaging.

3. **Directory and File Creation Loop**:
   - The script iterates over each path in the `list_of_files`. For each path, it performs the following steps:
     a. Splits the path into a directory (`filedir`) and file name (`filename`) using `os.path.split`.
     b. If the directory part of the path is not empty, it creates the directory (and any necessary parent directories) using `os.makedirs`, with `exist_ok=True` to avoid raising an error if the directory already exists.
     c. Checks if the file exists and is not empty. If the file doesn't exist or is empty, it creates (or truncates) the file by opening it in write mode. If the file already exists and is not empty, it prints a message indicating this.

This approach provides a quick and automated way to set up the file and directory structure for a new Python project, ensuring that all necessary components and configuration files are in place from the start. The use of `os.makedirs` with `exist_ok=True` and the check for file existence and size before creating files are precautions to avoid overwriting existing work.
"""
        