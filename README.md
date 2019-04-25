# photography website

Setting up the environment

1. Setting up the virtual environment. The system is currently developed with Python3. Please make sure that the Flask, Pymysql is properly installed in the `virtual environment`. Refer to <http://flask.pocoo.org/docs/1.0/installation/#virtual-environments>

   - For Linux and Mac:

     ```
     mkdir myproject
     cd myproject
     python3 -m venv venv
     . venv/bin/activate
     ```

   - For Windows:

     ```
     py -3 -m venv venv
     venv\Scripts\activate
     ```

     

2. Install dependency packages in virtual environment:

   ```
   pip install Flask
   pip install pymysql
   pip install cryptography
   ```

3. To simplify development, create a mysql database called 'photo'. 

   ```
   CREATE DATABASE photo;
   ```

4. When log in mysql as root, create a  user 'photodev' and grant privilege.

   ```
   CREATE USER 'photodev'@'localhost' IDENTIFIED BY '123456';
   GRANT ALL PRIVILEGES ON photo.* TO 'photodev'@'localhost';
   ```

   

For Linux and Mac:

```shell
export FLASK_APP=photo
export FLASK_ENV=development
flask run
```

For Windows cmd, use set instead of export:

```
set FLASK_APP=photo
set FLASK_ENV=development
flask run
```

For Windows PowerShell, use $env: instead of export:

```powershell
$env:FLASK_APP = "photo"
$env:FLASK_ENV = "development"
flask run
```

To initialize the database, the following command should be executed. This command will overwrite all data in the database 'photo'

```shell
flask init-db
flask run
```

 The log in page should be on

```http
http://127.0.0.1:5000/auth/login
```

