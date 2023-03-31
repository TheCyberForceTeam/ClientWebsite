#!/bin/bash
#Auto-configure the webserver, make this script executable with sudo chmod +x autorun.sh
# Change directory to where the script is located
cd "$(dirname "$0")"

# Install required modules
pip install -r requirements.txt

# Check for updates from GitHub
git pull

# Run the autorun script that sets up this webserver to always boot on startup
python3 autorun.py

# Start uWSGI server
uwsgi --http :8080 --wsgi-file PythonWebServer.py --buffer-size 65536
