#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, url_for, request
import requests
import pickle
import numpy as np
import json
from logging.handlers import RotatingFileHandler
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/hello_world', endpoint='hello_world', methods=['GET'])
def hello_world_func():
    app.logger.info('hi')   
    return '"result":"hello world"'

@app.route('/calc_proba', endpoint = 'calc_proba',methods=['POST','GET'])
def get_proba():
    if request.method=='POST':
        result=request.get_json(force=True)
        pkl_file = open('cat', 'rb')
        cat_cols = open('cat_cols','rb')
        num_cols = open('num_cols','rb')
        
        index_dict = pickle.load(pkl_file)
        cat_cols   = pickle.load(cat_cols)
        num_cols   = pickle.load(num_cols)
        
        new_vector = np.zeros((len(index_dict)))
        e = []
        p = []
        s = []

        
        for col in cat_cols:
            if col in result:
                try:
                    new_vector[index_dict[col+'_'+str(result[col])]] = 1
                    app.logger.info('done successfully')
                except (KeyError, ValueError): (e.append(col+' incorrect format'), s.append('402'), app.logger.warning('ValueError'))                                                                
            else: (e.append(col+' incorrect field'), s.append('401'), app.logger.warning('incorrect field'))
        
        
        
        for col in num_cols:
            if col in result:
                try:
                    new_vector[index_dict[col]] = result[col]
                    app.logger.info('done successfully')
                except ValueError: (e.append(col+' incorrect format'), s.append('402'), app.logger.warning('ValueError'))                              
            else: (e.append(col+' incorrect field'), s.append('401'), app.logger.warning('incorrect field'))
          
        
        
        pkl_file = open('model.pkl', 'rb')
        model = pickle.load(pkl_file)
                   
        if not e:
            e.append('None')
            s.append('200')
            p = model.predict_proba([new_vector])[:,1]
        else:
            p.append('None')
            s = list(set(s))


        responce = {'s'    : s,
                    'error': e,
                    'proba': str(p[0])
                    
        }
            
        app.logger.info('End')    

        
        return str(responce)    #json.dumps(responce, indent = 3)

        

if __name__ == "__main__":
    handler = RotatingFileHandler('log.log', maxBytes=1000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()


# In[ ]:




