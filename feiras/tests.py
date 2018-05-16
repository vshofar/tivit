
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Feira

import load
import json
import requests

import os
import operator


class QueryFeiraTests(APITestCase):

    test_data_path = 'feiras/data/test-data.csv'

    
    def test_retrieve_all_records_over_existent_data(self):


        """
            GET feiras/ retrieve all records present on database
        """

        #populate database with valid data
        load.loadData(os.path.abspath(self.test_data_path))

        #get feira records in json format
        lstored = [f.toJson() for f in Feira.objects.all()]
                
                
        #request remote data
        response = self.client.get('/feira/', format='json')

        self.assertIs(response.status_code,requests.codes.ok)

        lresponse = response.json()

        # sort dictionary list to be compared        
        lstored.sort(key=operator.itemgetter('registro'))
        lresponse.sort(key=operator.itemgetter('registro')) 
       
        
        
        self.assertIs(lstored==lresponse,True)
 
        
        
    def test_retrieve_no_records_over_empty_data(self):

        """
            GET feiras/ retrieve no records when database is empty
        """

        #request remote data
        response = self.client.get('/feira/', format='json')

              
        # valaidate status code
        self.assertIs(response.status_code,requests.codes.ok)

        #validate reponse content 
        self.assertIs(json.dumps([]),json.dumps(response.json())) 

    def test_retrieve_specific_data(self):


        """
            GET feiras/id/ retrieve specific record by id field
        """

        #populate database with valid data
        load.loadData(os.path.abspath(self.test_data_path))

        #get specific record 
        fstored = Feira.objects.all()[0]

        #get feira records in json format
        stored = fstored.toJson()                
                
        #request remote data by id
        response = self.client.get('/feira/%s/'%fstored.id, format='json')

        #validate status code
        self.assertIs(response.status_code,requests.codes.ok)

        remote_data = response.json()

        #validate remote data retrieved             
        self.assertIs(stored==remote_data,True) 




class EditFeiraTests(APITestCase):

    test_data_path = 'feiras/data/test-data.csv'

    
    def test_insert_new_valid_record(self):


        """
            POST feiras/ data={new valid data} insert a new record
        """
        
        ldata = load.readCsvData(self.test_data_path)
        feira_to_insert = ldata[0]
            
        #request data insert
        response = self.client.post('/feira/', data=feira_to_insert ,format='json')

        self.assertIs(response.status_code,requests.codes.created)

        #get feira records in json format
        fstored = Feira.objects.all()[0].toJson()

        #convert all field data to string to let comparison with csv data
        fstored = dict((k,str(v)) for k,v in fstored.items())

        # remove id field. it must be diferent.     
        feira_to_insert.pop('ID')
        fstored.pop('id')

        self.assertIs(feira_to_insert==fstored,True)



    def test_insert_new_invalid_record(self):


        """
            POST feiras/ data={new invalid data} must not insert the new record
        """
        
        ldata = load.readCsvData(self.test_data_path)
        feira_to_insert = ldata[0]

        #insert error on number field
        feira_to_insert['log'] = 'invalid_number'
            
        #request data insert
        response = self.client.post('/feira/', data=feira_to_insert ,format='json')

        self.assertIs(response.status_code==requests.codes.bad_request,True)



    def test_insert_new_empty_record(self):

        """
            POST feiras/ data={empty} must not insert the new record
        """        
        
        feira_to_insert = {}

                    
        #request data insert
        response = self.client.post('/feira/', data=feira_to_insert ,format='json')

        self.assertIs(response.status_code==requests.codes.bad_request,True)

        
 
          
        

