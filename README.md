
# Cryptocurrency mining as a monetization method

### This product is an experimental platform to deduce a general end-user's opinion on advertisement, cryptocurrency and their demographic.
Using this data we will be able to evaluate whether cryptocurrency mining as a monetization method is feasible.


To run this product in a local envirnoment.

1. Ensure all pip requirements are installed from requirements.txt
2. Navigate to miner/mysite in the command line and run the commands `python3 manage.py migrate` followed by `python3 manage.py makemigrations`
3. To create a superuser in the local enviroment run the command `python3 manage.py createsuperuser`
4. Finally run `python3 manage.py runserver`



There are two accessible pages that you may enter on the local environment: The splash page and the admin page.
These may be found at http://127.0.0.1:8000/home/ and http://127.0.0.1:8000/admin

To see this product in a remote environment, follow the link: https://minersite.herokuapp.com/home/
