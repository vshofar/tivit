# 'Feiras' REST api

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

    This section wil describe aboud data forma used for .csv files to be loaded by 'load.py' script and
    json data format to be used on request and responde REST operations.

    - .csv format:
        The .csv file must contain the follwing 'header' columns:
            ID,LONG,LAT,SETCENS,AREAP,CODDIST,DISTRITO,CODSUBPREF,SUBPREFE,REGIAO5,REGIAO8,NOME_FEIRA,REGISTRO,LOGRADOURO,NUMERO,BAIRRO,REFERENCIA

        Only REFERENCIA and NUMERO fields are optional.
        The other required field values must be compliat with cotraints decribed bellow.

    - json format:
        The fields that must be available in json data must be constraint with following description:
        
        log             = BigIntegerField()
        lat             = BigIntegerField()
        set_sens        = BigIntegerField()
        area_p          = BigIntegerField()
        
        cod_dist        = IntegerField()
        distrito        = CharField(max_length=100)

        cod_sub_pref    = IntegerField()
        sub_pref        = CharField(max_length=100)

        regiao5         = CharField(max_length=20)
        regiao8         = CharField(max_length=20)

        nome_feira      = CharField(max_length=200)
        registro        = CharField(max_length=20,unique=True)
        
        logradouro      = CharField(max_length=250)
        numero          = CharField(max_length=50,blank=True)
        bairro          = CharField(max_length=50)
        referencia      = CharField(max_length=200,blank=True)
        


# Running tests

    inside 'project' folder:
        source env/bin/activate
        cd tivit

        python manage.py test feiras
        # the 14 test cases described in 'Test Cases' secition must be executed.

# Test Cases

    The project test cases are available in django framework 'APITestCase' present in 'feiras/tests.py' file.
    The test case methods validate the following contraints:

    - test_retrieve_all_records_over_existent_data

        """
            GET feiras/ retrieve all records present on database
        """

    - test_retrieve_no_records_over_empty_data

        """
            GET feiras/ retrieve no records when database is empty
        """

    - test_retrieve_specific_data


        """
            GET feiras/id/ retrieve specific record by id field
        """

    - test_query_by_distrito


        """
            GET feiras/distrito/ retrieve records by 'distrito' field
        """

    - test_query_by_regiao5


        """
            GET feiras/regiao5/ retrieve records by 'distrito' field
        """

    - test_query_by_bairro


        """
            GET feiras/bairro/ retrieve records by 'bairro' field
        """

    - test_query_by_bairro


        """
            GET feiras/nome-feira/ retrieve records by 'nome_feira' field
        """

    - test_insert_new_valid_record


        """
            POST feiras/ data={new valid data} insert a new record
        """
        

    - test_insert_new_invalid_record


        """
            POST feiras/ data={new invalid data} must not insert the new record
        """

    - test_insert_new_empty_record

        """
            POST feiras/ data={empty} must not insert the new record
        """       

    - test_remove_valid_record


        """
            DELETE feiras/registro remove a valid record
        """

    - test_remove_invalid_record


        """
            DELETE feiras/id must not remove invalid record
        """

    - test_update_valid_record


        """
            PUT feiras/{valid data} must update a record
        """

    - test_update_invalid_record


        """
            PUT feiras/{invalid data} must not update a record
        """

    - test_update_registro


        """
            PUT feiras/{registro changed} must not update a record
        """

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









