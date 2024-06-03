import os
import shutil
import stat
import subprocess

def make_executable(filepath):
    mode = os.stat(filepath).st_mode
    os.chmod(filepath, mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

def remove_file(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

# Paths to Docker-related files and directories
dockerfile_path = os.path.join(os.getcwd(), 'src', 'Dockerfile')
docker_dir_path = os.path.join(os.getcwd(), 'docker-compose.yml')
docker_nginx_dir_path = os.path.join(os.getcwd(), 'nginx')


# Check if Docker should be included
include_docker = '{{ cookiecutter.include_docker }}' == 'yes'

if not include_docker:
    remove_file(dockerfile_path)
    remove_file(docker_dir_path)
    remove_file(docker_nginx_dir_path)


# Path to the setup script
setup_script_path = os.path.join(os.getcwd(), 'setup.sh')
make_executable(setup_script_path)

# Run the setup script
subprocess.run(['bash', setup_script_path], check=True)