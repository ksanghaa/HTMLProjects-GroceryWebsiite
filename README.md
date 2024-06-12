# Grocery store application

## Project idea

Building a grocery store management system following a tutorial in order to become familiar with data concepts. The backend will be developed using Python and Flask, the development system used is MySQL.

# Prerequisities

Python 3
MySQL Server
Python packages: 'mysql-connector-python'

## Backend

Used VS code for this project as it supports many languages including Python which was used. It's extensive features and support for extensions me

I have chosen to use MySQL workbench because it is an open-source relational database management system. It is also compatiable with various operating systems and programming languages.

Encapsulation was used to in this project. For example, '.gitignore' was used to keep configuratoin and sensitive information seperate from the main codebase. in this project to protect sensitive information. Configuration Files 'config.py' contained passwords in this project.

# Common errors encountered:

The first error encounted was compatability/ version issues within MySQL workbench providing a connection warning message of "Incompatible/nonstandard server version or connection protocol detected (8.4.0) this was fixed through downloaded a later version of MySQL workbench and version 8.0.37 of MySQL which solved the error.

The basic logic and fundumentals learned from the tutorial were key when transposing it into vs code.

Error code 1364 when trying to input information into tables. Resolved this through looking at valid sql command syntax and incoprating it within mysql workbench query:
INSERT INTO `sys`.`products` (`product_id`, `name`, `uom_id`, `price_per_unit`)
VALUES ('2', 'soap', '1', '10.00');

To make the code readable made a new 'sql_connection.py' folder. However, unable to connect as the error ImportError: attempted relative import with no known parent package appears. Revolved this by including import sys
from pathlib import Path
sys.path.insert(0, str(Path(**file**).resolve().parent.parent)) to products_dao.py file

Common errors?
not null value exceptions,
how you fixed it
