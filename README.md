# photography website

Setting up the environment

1. Setting up the virtual environment. The system is currently developed with Python3. Please make sure that the Flask, Pymysql is properly installed in the virtual environment. Refer to <http://flask.pocoo.org/docs/1.0/installation/#virtual-environments>

2. Before initialize the database, we need to install dependency packages in virtual environment: cryptography and pymysql
   ```
   pip install pymysql
   pip install cryptography
   ```

3. To simplify development, create a mysql database called 'photo'. 

   ```
   CREATE DATABASE photo;
   ```

4. Create a  user 'photodev' and grant privilege.

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
```

 The index page should be on

```http
http://127.0.0.1:5000/
```

