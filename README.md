photography website

Catalog

- Setting up environment

- Website Demo

<br>

<br>

Setting up the environment

1. Setting up the virtual environment. The system is currently developed with Python3. Please make sure that the Flask, Pymysql is properly installed in the virtual environment. Refer to http://flask.pocoo.org/docs/1.0/installation/#virtual-environments
   - For Linux and Mac:
         mkdir myproject
         cd myproject
         python3 -m venv venv
         . venv/bin/activate
   - For Windows:
         py -3 -m venv venv
         venv\Scripts\activate
     
2. Install dependency packages in virtual environment:
       pip install Flask
       pip install pymysql
       pip install cryptography
3. To simplify development, create a mysql database called 'photo'. 
       CREATE DATABASE photo;
4. When log in mysql as root, create a  user 'photodev' and grant privilege.
       CREATE USER 'photodev'@'localhost' IDENTIFIED BY '123456';
       GRANT ALL PRIVILEGES ON photo.* TO 'photodev'@'localhost';
   

For Linux and Mac:

    export FLASK_APP=photo
    export FLASK_ENV=development
    flask run

For Windows cmd, use set instead of export:

    set FLASK_APP=photo
    set FLASK_ENV=development
    flask run

For Windows PowerShell, use $env: instead of export:

    $env:FLASK_APP = "photo"
    $env:FLASK_ENV = "development"
    flask run

To initialize the database, the following command should be executed. This command will overwrite all data in the database 'photo'

    flask init-db
    flask run

 The log in page should be on

    http://127.0.0.1:5000/auth/login





<br>

<br>

Website demo 

Website page

(For TA) How to test our website

We have four views:

1. login & Initialize page
2. dashboard page (charts are specific for different positions)
3. order pages (create order/ order details/ completed order)
4. profile page

<br>

Note: Since the photographer website is designed for internal members, users can only login using the existing accounts. That's the reason why we set the "Initialize" page, not "register" page.

We provide several account for you to test our website:

All passwords is preset to 123456. You can initialize it through Initialize page for the first time. Later if you want to change the password again, please visit the profile page.

Project Manager:

  Account  	Password
  yifanlan 	123456  
  Mary Chen	123456  

Photographer:

  Account     	Password
  wenjingcai  	123456  
  Barbara Yang	123456  

After Effect:

  Account   	Password
  Charles An	123456  
  Susan Bao 	123456  


