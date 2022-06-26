Web application:

<h1>DjangoPlants</h1>

This is my app for management and maintenance of home plants.
![Zrzut ekranu z 2022-06-25 23-35-39](https://user-images.githubusercontent.com/66016783/175791187-2e4f82de-86c2-4041-a532-bf41ed3b0449.png)


<h2>Project purpise and description</h2>
The purpose of this app is to help organize the manage all the plants at home. 
User can view, add and modify:
1. plants 
    - name: plant name,
    - price: purchase cost,
    - location: relation one-to-many with location
    - created: when the plant arrived to your home
    - updated: last date when the plant was watered, fertilized, ect.
    - difficulty: liczba głosów na przepis (domyślnie 0)
    - picture: graphical representation
    - notes: additional info about a plant (special care, sun requirements, ect)


2. locations
    - name (living room, baclony, terrace, ect.)
    - sunlight level (high, medium, low)


3. soil
    - name: name of the soil
    - type relation many-to-many with Plant,
    - price: purchase cost,

4. pots
    - type: plastic, stone, ect.
    - price: purchase cost,
    - radius (in cm)
    - plant: relation one to one with pot

5. suppliers
    - name (shop, garden centre, ect.)
    - address
    - relaction many to many with plant, soil, pot


6. plans
    - name (watering, ferilizing, cleaning)
    - description: detail work in this place
    - created - date of creation   

User can plan tasks regarding to particular plants in particular locations, like fertilizing, cutting, watering, application of plant protection substances.

<h2>Technologies used:</h2>
    <li>Python 3.8</li>
    <li>Django</li>
    <li>PostgreSQL</li>
    <li>HTML</li>
    <li>Bootstrap</li>
    <li>FontAwesome</li>

<h2>Running and using the app</h2>

1. Fork the repo and then clone it to PyCharm for example.
2. In Pycharm terminal or console go to the web app folder.
3. Use the the command to create a virtual environment (source venv/bin/activate).
4. Go to the folder with manage.py file and use the command (in console) to create own superuser (python manage.py createsuperuser) to get own account.
5. Use the command python manage.py runserver to start the app.
6. Enjoy.

The app has a very intuitive menu and easily allows to add, view and modify specific fiels.

![Zrzut ekranu z 2022-06-25 22-50-37](https://user-images.githubusercontent.com/66016783/175791229-864e97a5-dbce-4016-ba0d-5606c08d6300.png)

![Zrzut ekranu z 2022-06-25 22-49-13](https://user-images.githubusercontent.com/66016783/175791146-867d9be9-2b24-46f6-be2c-998724d34927.png)

![Zrzut ekranu z 2022-06-25 22-51-55](https://user-images.githubusercontent.com/66016783/175791205-93202036-6e06-4426-b151-27b577ee4fac.png)

![Zrzut ekranu z 2022-06-25 22-51-01](https://user-images.githubusercontent.com/66016783/175791220-ce5f7426-a289-4cd4-a3b4-e723d225c7c7.png)

Added, modified items are stored in database.

<h2>Credits</h2>

Thanks to Michał Dobrzycki from CodersLab (https://github.com/michal-dobrzycki-coderslab) for excellent mentorship and CodersLab.

<h2>LICENSE:</h2>
Feel free to use and modify this app but please add the author info. Hope it will help you in your home gardens.
