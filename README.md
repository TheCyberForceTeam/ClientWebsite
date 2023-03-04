# ClientWebsite
https://github.com/TheCyberForceTeam - CI5450_ALL_TY13_22 - Cyber Group Work - Phase 2 (Build)

```
88888 8           .d88b        8               8888                       88888                      
  8   8d8b. .d88b 8P    Yb  dP 88b. .d88b 8d8b 8www .d8b. 8d8b .d8b .d88b   8   .d88b .d88 8d8b.d8b. 
  8   8P Y8 8.dP' 8b     YbdP  8  8 8.dP' 8P   8    8' .8 8P   8    8.dP'   8   8.dP' 8  8 8P Y8P Y8 
  8   8   8 `Y88P `Y88P   dP   88P' `Y88P 8    8    `Y8P' 8    `Y8P `Y88P   8   `Y88P `Y88 8   8   8 
```

View the full document of what we have to do here - https://docs.google.com/document/d/1Z0D9u-bFFbjJ0FQu-HYUcbuyqvMbEu-wcGJ8RNaeVow/edit?usp=sharing


When you clone this script onto your Ubuntu system, 
please modify the "coffee.service" script to include 

Goals
Make an Ubuntu WebServer
Each member of the group should have to take responsibility for a week for overlooking every task and launching the web server for a week and ensure that every week that the web server image is backed up to a shared group space on BOX or OneDrive.
Create a local login account for each person in the group on the Ubuntu server so that log files can be generated each time a person logs in or has a failed login attempt. Include 3 different type of accounts, i.e. staff, customer and admin accounts.
Ensure that each remote access account can login to the web server remotely.
Each member of the group must create a single customised web page of their own, on the same group web server.
Each member of the group must access the webserver over a period of 2 weeks.
Create a shared group folder that is accessible by all members of the group.
Each member of the group must complete the Group’s Contribution Log.
Please include any relevant information such as passwords.
Present your group work by 31st March or prepare a screen captured video recording with a brief voice over description.


Main Tasks 

Milestones
Docker Acccount Created (Nathan & Oskar)
This will allow us to host a cloud webserver and ubuntu machine that we can all acccess
Web Server Main backend created (Nathan & Oskar)
By using Nicepage we will be able to easily create webpages that match the clients demands. We can use python to build the application that will allow authenticated users to access the websites we built, click which one they would like to serve and interact with each one. In a similar way to how google and microsoft one drive work. You’ll be able to login to the webserver first, then click an icon representing each page. 

As an admin you can choose which sites to expose on the ports / run, and view connections and the website in another browser, download a log of recent login attempts based on what credentials were given and the ip of the device connecting and their time. And everything staff can do.

As staff you will be able to download files on the website, such as any customer entries, view customer purchases / requests, reset staff passwords manually, remove options from the store with an approval request key (some random string that we create to make it more secure and must be made by an admin and added to a database) with an option to view or access the site as a guest.

As a customer, connecting to the ip of the webserver is the same for all, you get a blank field, you are asked to enter your email, if the server doesn’t recognise it (not in the database) you are immediately logged in under your email temporarily. No login account necessary as you are a customer visiting a page and you won’t need to store anything for a coffee shop. (If it does appear as an employee a password field will appear requiring a login) 

Web Pages made (Nathan, Oskar, Abdullah, Asmarani, Waj, Jonel)
We need to make a web page each , add your name next to which youre going to do:


Include a GDPR and Offer to use cookies to remember users pop up html pages
Legal Page (Can be copied from another website
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
