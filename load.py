
import csv
import os
import sys
import json
import requests

# If you find a solution that does not need the two paths, please comment!
sys.path.append('/home/zack/program/prova/tivit')
os.environ['DJANGO_SETTINGS_MODULE'] = 'tivit.settings'

import django
django.setup()

from feiras.models import Feira
from feiras.serializers import FeiraSerializer
args = sys.argv

OK = 1
NOK = 0

ERROR_INVALID_ARG_NUMBER = "script execution requires one .csv file argument."
ERROR_ARG_INVALID_FILE = "the argument provided is not a a valid .csv file."

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
    serializer = FeiraSerializer(data=dicData)
    if (serializer.is_valid()):
        serializer.save()
        return OK
    else:
        return N_OK
         

    

def loadData(csvFile):
    
    csvfile = open(csvFile, 'r')
    json_data = json.dumps({})

    reader = csv.DictReader( csvfile, CSV_NAMES)    
    
    i=1   
    for row in reader:

        if(i != 1):           
       
            # translate cvs column names to model field names        
            for csvColumn in DIC_TRANSLATE_FIELDS:
                row[DIC_TRANSLATE_FIELDS[csvColumn]] = row.pop(csvColumn)

            
            result = storeData(row) 
            if(result == NOK):
                message = "invalid data at row - %s" %i            
            
        
        i = i+1       

    

if (len(args) != 2):
    print (ERROR_INVALID_ARG_NUMBER)

else:
    arg1 = args[1]

    if(not os.path.isfile(arg1)):
        print (ERROR_ARG_INVALID_FILE)
    
    elif not arg1.endswith('.csv'):
        print (ERROR_ARG_INVALID_FILE)

    else:
        loadData(arg1)


