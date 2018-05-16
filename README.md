# Tivit 'feiras' REST api

    This project aims to provide a REST api to query and manage some recorded data.
    It is based on python django framework and SQLite database.

# Install

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

# Running api service
    inside 'project' folder:
        cd tivit
        python manage.py migrate 
        python manage.py runserver #keep the script running

        open following address on web browser:
        http://127.0.0.1:8000/feira/ #an web page must be displayed with empty json data
    

# Loading data from .csv file

    inside 'project' folder:
        source env/bin/activate
        cd tivit
        python load.py feiras/data/test-data.csv #another compliant (read 'Data Model' section) .csv file path may be used.
       
        #refresh in browser the following the 'http://127.0.0.1:8000/feira/' address
        # the web page must display an json array with two objects

# Data Model
    


# Running tests

    inside 'project' folder:
        source env/bin/activate
        cd tivit

        python manage.py test feiras
        # the 14 test cases described in 'Test Cases' secition must be executed.

# API Requests Available
    
    - Register new 'feira' record
        POST http://127.0.0.1:8000/feira/
            #require valid request data in json format

    - Delete 'feira' record by its 'registro' value
        DELETE http://127.0.0.1:8000/feira/$REGISTRO_VALUE            

    - Update 'feira' record
        PUT http://127.0.0.1:8000/feira/$REGISTRO_VALUE
            #require valid request data in json format

    - Query all 'feira' values
        GET http://127.0.0.1:8000/feira/   

    - Query 'feira' by 'distrito' value
        GET http://127.0.0.1:8000/feira/distrito/$DISTRITO_VALUE   

    - Query 'feira' by 'bairro' value
        GET http://127.0.0.1:8000/feira/bairro/$BAIRRO_VALUE  

    - Query 'feira' by 'regiao5' value
        GET http://127.0.0.1:8000/feira/regiao5/$REGIAO5_VALUE 

    - Query 'feira' by 'nome_feira' value
        GET http://127.0.0.1:8000/feira/nome-feira/$NOME_FEIRA_VALUE 









