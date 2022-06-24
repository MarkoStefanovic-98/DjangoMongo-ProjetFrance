# DjangoMongo-ProjetFrance

Requiert MongoDB en Local avec une base de données nommée "franceidee".

Une fois la base de données créée sur MongoDB, executer sur Pycharm :
- python manage.py makemigrations
- python manage.py migrate

Enfin, lancer  l'application.

Enjoy <3

Systeme :
- Connexion / Inscription
- CRUD
- Like / Dislike avancé expert (par user) + leur count

Index du site
![index](https://user-images.githubusercontent.com/31990307/174184967-372ad05b-d0e9-4abe-890e-3bb28c54a0a8.PNG)

Connexion
![connexion](https://user-images.githubusercontent.com/31990307/174184976-4f6e80bd-e497-4e4a-b858-205cf43dff87.PNG)

Page inscription
![inscription](https://user-images.githubusercontent.com/31990307/174184969-31d87cc9-10b3-405a-9812-e6786cd90ca0.PNG)

Les lois avec leur like / dislike
![les-lois-like-dislike](https://user-images.githubusercontent.com/31990307/174184970-5a4a1958-022c-44e4-b1c0-9fee4f71da6d.PNG)

Ajouter 
![ajouter](https://user-images.githubusercontent.com/31990307/174184974-9f6861c0-1f10-4857-86e7-d051c4f6bc5f.PNG)

Modifier
![modifer](https://user-images.githubusercontent.com/31990307/174184972-de7c71d3-30de-411b-b727-1c528b5c80de.PNG)


Note :

Le projet Django ne fonctionnait pas au début avec Mongo, en utilisant Djongo.
La solution a été trouvé en utilisant une version inférieur de Django (2.2.8) et en installant Mongo (Djongo), cela fonctionnait.
Par la suite, j'ai réussi tout de même une fois le projet terminé a repasser en 4.5.0 de Django tout en faisant marcher Djongo.

En conclusion, il m'a fallut faire le projet en Django 2.2.8 pour faire marcher Djongo (mongo) puis de repasser en 4.5.0 (Django).
