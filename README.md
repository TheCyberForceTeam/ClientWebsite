# ClientWebsite
https://github.com/TheCyberForceTeam - CI5450_ALL_TY13_22 - Cyber Group Work - Phase 2 (Build)

```
88888 8           .d88b        8               8888                       88888                      
  8   8d8b. .d88b 8P    Yb  dP 88b. .d88b 8d8b 8www .d8b. 8d8b .d8b .d88b   8   .d88b .d88 8d8b.d8b. 
  8   8P Y8 8.dP' 8b     YbdP  8  8 8.dP' 8P   8    8' .8 8P   8    8.dP'   8   8.dP' 8  8 8P Y8P Y8 
  8   8   8 `Y88P `Y88P   dP   88P' `Y88P 8    8    `Y8P' 8    `Y8P `Y88P   8   `Y88P `Y88 8   8   8 
```

View the full document of what we have to do here - https://docs.google.com/document/d/1Z0D9u-bFFbjJ0FQu-HYUcbuyqvMbEu-wcGJ8RNaeVow/edit?usp=sharing

Web Authentication System with Flask
This is a web authentication system that uses Flask to provide user authentication and authorization features.

How to Use
Clone the repository: git clone https://github.com/TheCyberForceTeam/ClientWebsite.git
Install the required modules: pip install -r requirements.txt
Run the autorun script to always boot on startup: sudo chmod +x autorun.sh && ./autorun.sh
Start the server manually: uwsgi --http :8080 --wsgi-file PythonWebServer.py 
The webserver will be accessible via localhost:8080 on your browser.

Files
PythonWebServer.py: This script is responsible for handling the server and client requests. It contains the Flask routes and user authentication logic.

autorun.sh: This script is responsible for installing required modules, checking for updates from the Github repository, running the autorun script that sets up this webserver to always boot on startup, and starting the uWSGI server.

database.db: This file is an SQLite database that stores the user data.

index.html: This file is the homepage for the web application.

Dependencies
This project uses the following dependencies:

Flask
SQLite3

Contributing
Contributions are welcome! Feel free to submit a pull request or raise an issue.

Main Tasks 


News/Media page (Made up news about the coffee shop, include photoshopped coffee shop stuff in a twitter / instagram way)
Staff Page (Only appears on staff login) should show chat box of messages from clients , Should show database in html of customer purchases , ip logged, failed login attempts, option to manually send a reset password link for other staff and options to see what’s on the store and remove options 
Main backend / front end html page for login and authentication 
Shop page to view store catalog (fake coffee and stuff) with add to basket and a booking page
Database made to store login details for admin and staff, include customer ips , emails, frequency of logins
Analysis script, to store log of logins
We should allow these to be stored as a csv, 
We should include charts, abdullahs design for ethical hacking was pretty good as an idea for staff to be able to access, we should be able to see three charts:
password strengths vs number of users (colour coded by their security levels)
Number of failed logins vs email account (colour coded by highest number)
Most sold item vs location ( sorted by highest to lowest)
And save them as a pdf
