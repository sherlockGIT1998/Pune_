import pickle 
import json 
import pandas as pd
import numpy as np 
import warnings
warnings.filterwarnings('ignore')
import config

class PuneHouseData():
    
    def __init__(self,area_type,availability,size,total_sqft,bath,balcony,site_location):
        
        self.availability = availability
        self.total_sqft = total_sqft
        self.bath = bath
        self.balcony = balcony
        self.site_location = site_location
        
        self.area_type_col = 'area_type_' + area_type

        self.size_col = 'size_' + size

    def load_models(self):
        
        with open(config.MODEL_FILE_PATH,'rb') as f :
            self.model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH,'r') as f :
            self.save_data = json.load(f)
            
            self.column_names = self.save_data['column_names']
            
    def get_predicted_price(self):
        
        self.load_models()
        
        area_type_col_index = np.where(self.column_names == self.area_type_col)[0]
        
        size_col_index = np.where(self.column_names == self.size_col)[0]
        
        array = np.zeros(len(self.save_data['column_names']))
        
        array[0] = self.save_data['availability'][self.availability]
        array[1] = self.total_sqft
        array[2] = self.bath
        array[3] = self.balcony
        array[4] = self.save_data['site_location'][self.site_location]

        array[area_type_col_index] == 1 

        array[size_col_index] == 1

        print('Array :',array)
        
        predict = self.model.predict([array])[0]
        
        return predict 
    
if __name__ == '__main__':
    
    availability = '19-Dec'
    total_sqft = '1056.0'
    bath = 2.0
    balcony  = 1.0
    site_location  = 'Alandi Road'

    area_type = 'Built-up Area'

    size = '1 BHK'

    price = PuneHouseData(area_type,availability,size,total_sqft,bath,balcony,site_location)
    
    predict = price.get_predicted_price()
    
    # print('Price of Pune House is : Rs.',round(predict,2),'Lakh/-')
    
    print(f'Price of Pune House is : Rs. {round(predict,2)} Lakh/-')