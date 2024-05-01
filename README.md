# Fruit Shop web application using Django.
Fruit Web Shop:
Create a simple Fruit Shop web application using Django. 
This project should include an admin portal for easy management of fruits.
Users should have the ability to view a list of available fruits and add or delete fruits from the web shop.
The project should also maintain a description for each fruit, and this description can be updated when adding or editing fruits in the shop.
# Key Features:
Fruit Listing: Users should be able to view a list of available fruits in the shop, including their names, prices, and descriptions.
# Admin Portal:
The admin portal should be set up to allow authorized users to manage fruits easily.
This includes adding new fruits with their names, descriptions, and prices, as well as deleting existing fruits.


### 
for window
Step: 1 - git clone https://chundrumanohar.github.io/Fruits_web_shop/

Step: 2 - pip install virtualenv

Step: 3 - virtualenv venv

Step: 4 - venv\Scripts\activate.bat

Step: 5 - pip install -r requirements.txt (install all library & dependencies)

Step: 6 - py manage.py runserver

OUTPUT: ADD,LIST,UPDATE,DELETE Fruits IN FRUIT SHOP



***** API endpoints ******
METHOD  URL                                   description

POST     http://127.0.0.1:8000/fruits/add/ Create Add Fruits

GET      http://127.0.0.1:8000/fruits/listFruits/ get all Fruits

PUT      http://127.0.0.1:8000/fruits/update/13/ Update Fruits by id

DELETE   http://127.0.0.1:8000/fruits/delete/12/ Delete Fruits by id




