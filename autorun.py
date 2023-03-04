import os
import shutil

# Get the directory path of the currently running file
current_directory_path = os.path.dirname(__file__)

# Set the path to PythonWebServer.py by joining the directory path and the filename
python_web_server_path = os.path.join(current_directory_path, "PythonWebServer.py")

# Install required modules
os.system("pip install -r requirements.txt")

# Check for updates from GitHub
os.system("git pull")

# Check if coffee.service exists in /etc/systemd/system
if not os.path.exists("/etc/systemd/system/coffee.service"):
    # Copy coffee.service to /etc/systemd/system
    shutil.copy("coffee.service", "/etc/systemd/system/")
    print("File copied to /etc/systemd/system")

    # Modify coffee.service
    with open("/etc/systemd/system/coffee.service", "r") as f:
        service_file_contents = f.read()

    # Replace the directory path in WorkingDirectory and ExecStart
    service_file_contents = service_file_contents.replace(
        "/path/to/script/directory", current_directory_path
    )

    # Replace the ExecStart command
    service_file_contents = service_file_contents.replace(
        "/path/to/script.sh", python_web_server_path
    )

    # Write the modified file back to disk
    with open("/etc/systemd/system/coffee.service", "w") as f:
        f.write(service_file_contents)

    # Reload systemd daemon and enable/start coffee.service
    os.system("sudo systemctl daemon-reload")
    os.system("sudo systemctl enable coffee.service")
    os.system("sudo systemctl start coffee.service")

    print("Modified and started coffee.service")
else:
    print("Configured to start on boot")

# Start uWSGI server
os.system("uwsgi --http :8080 --wsgi-file " + python_web_server_path)
