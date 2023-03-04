import os
import shutil

# Define the path to PythonWebServer.py
python_web_server_path = '/home/john/myapp/PythonWebServer.py'

# Check if the file exists in /etc/systemd/system
if not os.path.exists('/etc/systemd/system/coffee.service'):
    # Copy the file to /etc/systemd/system
    shutil.copy('coffee.service', '/etc/systemd/system/')
    print('File copied to /etc/systemd/system')

    # Modify the copied service file
    with open('/etc/systemd/system/coffee.service', 'r') as f:
        service_file_contents = f.read()

    # Replace the directory path in WorkingDirectory and ExecStart
    service_file_contents = service_file_contents.replace('/path/to/script/directory', '/home/john/myapp')

    # Replace the ExecStart command
    service_file_contents = service_file_contents.replace('/path/to/script.sh', '/home/john/myapp/script.sh')

    # Write the modified file back to disk
    with open('/etc/systemd/system/coffee.service', 'w') as f:
        f.write(service_file_contents)

    # Reload systemd daemon and enable/start coffee.service
    os.system('sudo systemctl daemon-reload')
    os.system('sudo systemctl enable coffee.service')
    os.system('sudo systemctl start coffee.service')

    print('Modified and started coffee.service')
else:
    print('Configured to start on boot')
