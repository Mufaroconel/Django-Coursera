# Configuring MySQL Connection

By default, Django uses the SQLite database for storage and retrieval of the app data, as Python has built-in support for it. However, you can use any of the following databases supported by Django:

- PostgreSQL
- MariaDB
- MySQL
- Oracle
- SQLite

In this Reading, you’ll learn the steps to enable a MySQL connection with a Django application.

## Advantage of MySQL

The SQLite database has a lot of limitations. It is serverless and doesn't have a user management system. It is useful for smaller applications and for the development of a prototype to be upgraded eventually for databases that are scalable and support client-server architecture.

MySQL is an open-source database and has a lot of advantages over SQLite, such as scalability and authentication.

## Install MySQL

To install the MySQL server, download the installer appropriate for your operating system from [MySQL Downloads](https://www.mysql.com/downloads/). For Windows, use the `mysql-installer-web-community-8.0.30.0.msi` and follow the wizard-based installation steps.

First open a command line terminal, then start the MySQL command line client with the following command:

```bash
mysql -u root -p
```

You will be prompted to enter the password set at the time of installation. In the command terminal, you will get the MySQL prompt. You can now enter any SQL statement in it.

Start by creating a database with the following command:

```sql
Create database mydatabase;
```
![alt text](image.png)

The `show databases;` command will show the list of currently available databases.

## Install MySQL DB API Driver

To interface a Python program with MySQL, ensure you have a DB API-compliant driver. There are a number of Python drivers for MySQL available. Django recommends `mysqlclient` to be used. Install it with pip installer.

```bash
pip3 install mysqlclient
```

## Enable MySQL

To be able to use MySQL, the `DATABASES` variable in the Django project’s settings file must be properly configured. By default, it is set to the connection parameters for SQLite. Remove those statements. You have to add MySQL-specific settings in their place.

You must configure at least one database in the `DATABASES` variable. For the configuration of the first database, its name should be ‘default’.

The settings include the database engine, name of the database, username, and password, along with the host IP address. This defaults to the localhost `127.0.0.1` and the port defaults to `3306`.

```python
#Settings.py

DATABASES = {   
    'default': {   
        'ENGINE': 'django.db.backends.mysql',   
        'NAME': 'mydatabase',   
        'USER': 'root',   
        'PASSWORD': '',   
        'HOST': '127.0.0.1',   
        'PORT': '3306',   
        'OPTIONS': {   
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

```python
# DATABASES = {
#     'default':{
#         'ENGINE' : 'django.db.backends.mysql',
#         'NAME': 'Feedback',   
#         'USER': 'admindjango',   
#         'PASSWORD': 'password',   
#         'HOST': '127.0.0.1',   
#         'PORT': '3306',   
#         'OPTIONS': {   
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#         }
#     }
# }
```



The other optional parameters include:

- `sql_mode`: The session SQL mode will be set to the given string. It defaults to `'STATIC_TRANS_TABLES'` to prevent invalid or missing values from being stored in the database.
- `default-character-set`: The character set to be used. Default is `utf8`.
- `read_default_file`: MySQL configuration file to read.
- `init_command`: Initial command to issue to the server upon connection.

## Create database tables

The `startproject` template installs some Django apps by default. Some examples include admin, auth, and sessions.

Remember that you need to create the necessary database tables for these apps.

Run the `migrate` command to use the models in these apps and build their respective table structure in the current MySQL database.

```bash
python manage.py migrate
```

Inside the MySQL terminal, run the following commands:

```sql
use mydatabase;
Show tables;
```

Instead of viewing the data in the MySQL terminal, add a MySQL extension from VS Code extension library.

## VS Code extension for MySQL

From the VS Code extension marketplace, search for MySQL and install the extension.

MySQL appears in the explorer.

Click on the + button and enter the following details:

- Domain name: localhost
- User: root
- Password: ''

Now, the localhost appears in the explorer bar.

Expand the section by selecting the drop-down arrow and choose `mydatabase`. All the tables required for the `INSTALLED_APPS` will be visible.

In this reading, you have explored how to connect MySQL database with Django.
```