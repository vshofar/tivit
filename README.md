# tivit 'feiras' rest api

    This project aims to provide a REST api to query and manage some recorded data.
    It is based on python django framework and SQLite database.

# install

    Before try to run django app service the following python dependecies mut be installed.
    I recommend the use of python virtual env to keep your own python installation safe of changes.

    clone repository:
        mkdir project
        cd project
        git clone https://github.com/vshofar/tivit.git

    virtualenv:
                      
        virtualenv env
        source env/bin/activate        

    dependencies:
        
        pip install django
        pip install djangorestframework   
        pip install requests

# running api service
    inside 'project' folder:
        cd tivit
        python manage.py migrate 
        python manage.py runserver #keep the script running

        open following address on web browser:
        http://127.0.0.1:8000/feira/ #an web page must be displayed with empty json data
    

# loading data from .csv file

    inside 'project' folder:
        source env/bin/activate
        cd tivit
        python load.py feiras/data/test-data.csv #another compliant .csv file path may be used.
       
        #refresh in browser the following the 'http://127.0.0.1:8000/feira/' address
        # the web page must display an json array with two objects


# running tests

