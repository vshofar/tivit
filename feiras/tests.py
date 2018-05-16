
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

        self.assertEqual(response.status_code,requests.codes.ok)

        lresponse = response.json()

          
        
        self.assertListEqual(lstored,lresponse)
 
        
        
    def test_retrieve_no_records_over_empty_data(self):

        """
            GET feiras/ retrieve no records when database is empty
        """

        #request remote data
        response = self.client.get('/feira/', format='json')

              
        # valaidate status code
        self.assertEqual(response.status_code,requests.codes.ok)

        #validate reponse content 
        self.assertListEqual([],response.json()) 

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
        response = self.client.get('/feira/%s/'%fstored.registro, format='json')

        #validate status code
        self.assertEqual(response.status_code,requests.codes.ok)

        remote_data = response.json()

        #validate remote data retrieved             
        self.assertDictEqual(stored,remote_data) 




class InsertFeiraTests(APITestCase):

    test_data_path = 'feiras/data/test-data.csv'

    
    def test_insert_new_valid_record(self):


        """
            POST feiras/ data={new valid data} insert a new record
        """
        
        ldata = load.readCsvData(self.test_data_path)
        feira_to_insert = ldata[0]
            
        #request data insert
        response = self.client.post('/feira/', data=feira_to_insert ,format='json')

        self.assertEqual(response.status_code,requests.codes.created)

        #get feira records in json format
        fstored = Feira.objects.all()[0].toJson()

        #convert all field data to string to let comparison with csv data
        fstored = dict((k,str(v)) for k,v in fstored.items())

        # remove id field. it must be diferent.     
        feira_to_insert.pop('ID')
        fstored.pop('id')

        self.assertDictEqual(feira_to_insert,fstored)



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

        self.assertEqual(response.status_code,requests.codes.bad_request)



    def test_insert_new_empty_record(self):

        """
            POST feiras/ data={empty} must not insert the new record
        """        
        
        feira_to_insert = {}

                    
        #request data insert
        response = self.client.post('/feira/', data=feira_to_insert ,format='json')

        self.assertEqual(response.status_code,requests.codes.bad_request)



class RemoveFeiraTests(APITestCase):

    test_data_path = 'feiras/data/test-data.csv'

    
    def test_remove_valid_record(self):


        """
            DELETE feiras/registro remove a valid record
        """
        
        #populate database with valid data
        load.loadData(os.path.abspath(self.test_data_path))

        #get specific record 
        registro_to_remove = Feira.objects.all()[0].registro      
            
        #request delete data
        response = self.client.delete('/feira/%s/'%registro_to_remove, format='json')

        #validate status code        
        self.assertEqual(response.status_code,requests.codes.no_content)

        #validate database status
        self.assertEqual(len(Feira.objects.filter(registro=registro_to_remove)),0)



    def test_remove_invalid_record(self):


        """
            DELETE feiras/id must not remove invalid record
        """
        
        #populate database with valid data
        load.loadData(os.path.abspath(self.test_data_path))

        qtd_stored_before = len(Feira.objects.all())
        self.assertIs(qtd_stored_before>1,True)

        #get specific record 
        registro_to_remove = 200     
            
        #request delete data
        response = self.client.delete('/feira/%s/'%registro_to_remove, format='json')

        #validate status code        
        self.assertEqual(response.status_code,requests.codes.not_found)

        qtd_stored_after = len(Feira.objects.all())

        #validate database status
        self.assertEqual(qtd_stored_before,qtd_stored_after)


class UpdateFeiraTests(APITestCase):

    test_data_path = 'feiras/data/test-data.csv'

    
    def test_update_valid_record(self):


        """
            PUT feiras/{valid data} must update a record
        """
        
        #populate database with valid data
        load.loadData(os.path.abspath(self.test_data_path))

        #get specific record 
        f_object = Feira.objects.all()[0]

        #change some data        
        f_object.regiao5 = 'nova regiao'
        f_object.log    = 34343434       
            
        #request update data
        response = self.client.put('/feira/%s/'%f_object.registro,data=f_object.toJson(),format='json')

        #validate status code        
        self.assertEqual(response.status_code,requests.codes.ok)

        #validate database status  

        self.assertDictEqual(Feira.objects.get(registro=f_object.registro).toJson(),f_object.toJson())


    def test_update_invalid_record(self):


        """
            PUT feiras/{invalid data} must not update a record
        """
        
        #populate database with valid data
        load.loadData(os.path.abspath(self.test_data_path))

        #get specific record 
        f_object = Feira.objects.all()[0]

        #change some data        
        f_object.regiao5 = 'nova regiao'
        f_object.log    = 'invalid value'      
            
        #request update data
        response = self.client.put('/feira/%s/'%f_object.registro,data=f_object.toJson(),format='json')

        #validate status code        
        self.assertEqual(response.status_code,requests.codes.bad_request)

        #validate database status 
        self.assertNotEqual(Feira.objects.get(registro=f_object.registro).toJson(),f_object.toJson())

        
        

        


        
 
          
        

