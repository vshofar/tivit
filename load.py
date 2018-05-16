
import csv
import os
import sys
import json


#add django project path to sys.path to let project 'feira' app loading in offline mode
os.environ['DJANGO_SETTINGS_MODULE'] = 'tivit.settings'

#load django project 
import django
django.setup()

from feiras.models import Feira
from feiras.serializers import FeiraSerializer
args = sys.argv

OK = 1
NOK = 0

# error message strings
ERROR_INVALID_ARG_NUMBER = "script execution requires one .csv file argument."
ERROR_ARG_INVALID_FILE = "the argument provided is not a a valid .csv file."


'''
 dictionary to store relation between cvs colunm field names and django 'feira' model field names
 must be use to translate cvs jason load data to 'feira' serialized objects.
'''
DIC_TRANSLATE_FIELDS = { 
                        'LONG'      :'log',
                        'LAT'       :'lat',
                        'SETCENS'   :'set_sens',
                        'AREAP'     :'area_p',
                        'CODDIST'   :'cod_dist',
                        'DISTRITO'  :'distrito',
                        'CODSUBPREF':'cod_sub_pref',
                        'SUBPREFE'   :'sub_pref',
                        'REGIAO5'   :'regiao5',
                        'REGIAO8'   :'regiao8',
                        'NOME_FEIRA':'nome_feira',
                        'REGISTRO'  :'registro',
                        'LOGRADOURO':'logradouro',
                        'NUMERO'    :'numero',
                        'BAIRRO'    :'bairro',
                        'REFERENCIA':'referencia'}


# cvs column names to be load from .cvs inout file
CSV_NAMES =       ( "ID",
                    "LONG",	
                    "LAT",	
                    "SETCENS",	
                    "AREAP",
                    "CODDIST",
                    "DISTRITO",
                    "CODSUBPREF",
                    "SUBPREFE",
                    "REGIAO5",
                    "REGIAO8",
                    "NOME_FEIRA",
                    "REGISTRO",
                    "LOGRADOURO",
                    "NUMERO",
                    "BAIRRO",
                    "REFERENCIA")


def storeData(dicData): 

    '''
       create 'feira' serialize object from a dictionary
       to validate data and save it to database.  
    '''

    serializer = FeiraSerializer(data=dicData)
    if (not serializer.is_valid()):
        return NOK

    serializer.save()
    return OK
           
         

    

def loadData(csvFile):

    '''
        load 'feira' data records from .csv file, valildate and store it to database.
    '''
    
    # load file    
    csvfile = open(csvFile, 'r')
    json_data = json.dumps({})

    # validate columns    
    reader = csv.DictReader( csvfile, CSV_NAMES)    
    
    i=1   
    result = ""
    for row in reader:

        #discart first column names row        
        if(i != 1):           
       
            # translate cvs column names to 'feira' model field names        
            for csvColumn in DIC_TRANSLATE_FIELDS:
                row[DIC_TRANSLATE_FIELDS[csvColumn]] = row.pop(csvColumn)

            
            # validate and save data            
            s_result = storeData(row) 
            
            # inform about non compliant data
            if(s_result == NOK):
                message = "invalid data at row - %s" %i
            else:
                message = "row %s data inserted." %i
            
            result += "\n %s" %message          
            
        
        i = i+1
    return result

    
def main():

    '''
        validate script input and call method to store csv data
    '''

    #validate args amount    
    if (len(args) != 2):
        print (ERROR_INVALID_ARG_NUMBER)
        return
    
    input_file = args[1]

    # valiate arg[1] is a valid file
    if(not os.path.isfile(input_file)):
        print (ERROR_ARG_INVALID_FILE)
        return
    
    # validate arg[1] is a .csv file        
    if not input_file.endswith('.csv'):
        print (ERROR_ARG_INVALID_FILE)
        return

    #store cvs data                
    print (loadData(input_file))

if __name__ == "__main__":
    main()


