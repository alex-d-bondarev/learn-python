# web server

This section covers chapter 5-7

## Prerequisites

1. Install FLASK `python3 -m pip install flask`
1. Install MySQL Python Driver:
    1. Go to https://dev.mysql.com/downloads/connector/python/
    1. Download `Platform Independent` driver
    1. Unzip downloaded driver
    1. Open unziped folder via console
    1. Install driver `python3 setup.py install` 
1. Install MySQL or start docker-compose:
    1. `docker-compose up -d`
    1. Connect via any MySQL IDE as:
        1. Host = 127.0.0.1
        1. Port = 3306
        1. User = root
        1. Password = test_pass
1. Set up DB: 
```sql
create database vsearchlogDB;
CREATE USER 'vsearch' IDENTIFIED BY 'vsearchpasswd';
GRANT ALL ON vsearchlogDB.* TO 'vsearch';

Use vsearchlogDB;
create table log (
id int auto_increment primary key,
ts timestamp default current_timestamp,
phrase varchar(128) not null,
letters varchar(32) not null,
ip varchar(16) not null,
browser_string varchar(256) not null,
results varchar(64) not null );
```
        
## Run

1. Open [hello_flask](hello_flask.py) via IDE and launch it
    OR run via concole `python3 hello_flask.py`
1. Browse http://127.0.0.1:5000/
