# Django-CRUD-Restaurant
With this app, you can fully manage a restaurant's website. Made with Python in Django Framework, SQLite3, HTML, CSS and Bootstrap.
<h2>Key features:</h2>
<ul>
  <li>User registration</li>
  <li>User login</li>
  <li>Logged-in user profile</li>
  <li>Admin user authorized pages</li>
  <li>Menu display with sections and their meals</li>
  <li>Menu that adapts to the user's choice of diet type, showing only the meals for that diet type.</li>
  <li>Meal search by name</li>
  <li>Meal deletion</li>
  <li>Meal editing</li>
  <li>Meal adding</li>
  <li>Menu printing</li>
</ul>
To get it running on your local machine, follow the steps below:
<ol>
  <li>Run the commands below in your terminal:</li>
  ```
  <li>$ git clone https://github.com/nemcve/Django-CRUD-Restaurant.git</li>
  <li>$ cd Django-CRUD-Restaurant/Restaurant</li>
  <li>$ pip install -r requirements.txt</li>
  <li>$ python manage.py runserver</li>
  <li>Open your browser and navigate to http://127.0.0.1:8000/</li>
  <li>Admin login username: admin password: admin</li>
  ```
</ol>
If you want to create a new admin user:
<br>$ python manage.py createsuperuser, and follow the prompts
<br>To access the admin control panel, in the url field, add /admin. Like this: https://127.0.0.1:8000/admin
