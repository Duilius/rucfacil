import os
import pathlib

def create_project_structure(base_path="peru_tax_services_project"):
    """
    Creates the project directory structure.
    """
    base_path_obj = pathlib.Path(base_path)

    # Lista de directorios a crear. Usamos tuplas para (path_relativo, crear_init_py)
    # Si crear_init_py es True, se crea un archivo __init__.py vacío en ese directorio.
    directories = [
        # Raíz del proyecto (ya se crea si no existe)
        ("", False),

        # Directorio principal de la aplicación
        ("app", True),
        ("app/core", True),
        ("app/db", True),
        ("app/models", True),
        ("app/schemas", True),
        ("app/crud", True),
        ("app/apis", True),
        ("app/apis/v1", True),
        ("app/apis/v1/endpoints", True),
        ("app/services_logic", True),
        ("app/templates", True),
        ("app/templates/services", True), # Subdirectorio para plantillas de servicios
        ("app/static", True),
        ("app/static/css", True),
        ("app/static/js", True),
        ("app/static/img", True), # Carpeta de imágenes como solicitaste
        ("app/chatbot", True),
        ("app/chatbot/intents", True), # Si usas un NLU basado en intenciones

        # Directorio de Alembic (Alembic lo creará con 'alembic init', pero podemos hacer el dir base)
        ("alembic", False), # Alembic init crea el contenido
        # ("alembic/versions", False), # Alembic init crea esto

        # Directorio de Pruebas
        ("tests", True),
    ]

    # Archivos específicos a crear (vacíos)
    files_to_create = [
        "app/main.py",
        "app/core/config.py",
        "app/core/security.py",
        "app/db/database.py",
        "app/db/base_class.py",
        # "app/db/init_db.py", # Comentado ya que usaremos Alembic principalmente
        "app/apis/deps.py", # Para dependencias de FastAPI
        "app/apis/v1/api.py", # Agregador de routers v1
        "app/templates/base.html",
        "app/templates/login.html",
        "app/templates/dashboard_client.html",
        "app/templates/dashboard_staff.html",
        "app/static/css/styles.css",
        "app/static/js/main.js",
        "app/chatbot/main_chatbot.py",
        "tests/conftest.py",
        ".env", # Importante: Archivo vacío para variables de entorno
        ".gitignore",
        "README.md",
        # "pyproject.toml", # Opcional, dependiendo de tu gestor de paquetes
        # "requirements.txt", # Opcional, si no usas pyproject.toml
    ]

    # Crear el directorio base del proyecto
    base_path_obj.mkdir(parents=True, exist_ok=True)
    print(f"Created base directory: {base_path_obj.resolve()}")

    # Crear subdirectorios y archivos __init__.py
    for dir_path_str, create_init in directories:
        if not dir_path_str: # Skip el directorio raíz que ya se creó
            continue
        dir_path = base_path_obj / dir_path_str
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"  Created directory: {dir_path}")
        if create_init:
            init_file = dir_path / "__init__.py"
            init_file.touch()
            print(f"    Created __init__.py in {dir_path}")

    # Crear archivos específicos
    for file_path_str in files_to_create:
        file_path = base_path_obj / file_path_str
        # Asegurarse de que el directorio padre exista si el archivo está en un subdirectorio no listado antes
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch() # Crea un archivo vacío
        print(f"  Created file: {file_path}")

    print("\nProject structure created successfully!")
    print("Next steps suggested:")
    print("1. Initialize git: `git init` (inside peru_tax_services_project)")
    print("2. Create and activate a virtual environment.")
    print("3. Install dependencies (FastAPI, Uvicorn, SQLAlchemy, Pydantic, Alembic, etc.).")
    print("4. Configure Alembic: `alembic init alembic` (if you haven't manually created the dir).")
    print("5. Populate .gitignore (e.g., add .env, __pycache__/, venv/, alembic/versions/* if autogenerated and you want to manage carefully, etc.).")

if __name__ == "__main__":
    project_name = input("Enter the project base directory name (default: peru_tax_services_project): ")
    if not project_name:
        project_name = "peru_tax_services_project"
    create_project_structure(project_name)