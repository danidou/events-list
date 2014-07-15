events-list
===========

## Installation instructions (development version)

1. Create a virtual environment. Get beer (and optionnaly glass) while it's being created.
   ```bash
   $ mkvirtualenv events-list
   ```
2. Install required packages. Open beer while being installed.
   ```bash
   $ pip install -r requirements.txt
   ```
3. Create database. Pour beer into glass (optionnal).
   ```bash
   $ ./manage.py syncdb
   
   Creating tables ...
   [...]
   ```
   ```bash
   You just installed Django's auth system, which means you don't have any superusers defined.
   Would you like to create one now? (yes/no):
   ```
   *Enter 'yes' and press return*

   ```bash
   Username (leave blank to use 'username'): 
   ```
   *Enter desired username, and press return*
   ```bash
   Email address: 
   ```
   *Enter desired email address, and press return*
   ```bash
   Password:
   Password (again):
   ```
   *Enter desired password and press return, twice.*
   
   ```bash
   Superuser created successfully.
   [...]
   ```
3. Start server. Enjoy beer!
   ```bash
   $ ./manage.py runserver
   ```
