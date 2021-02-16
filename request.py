#!/usr/bin/env python
# coding: utf-8

# In[134]:


import requests
import json

url = 'http://localhost:5000/calc_proba'

data = {'age': 54,
        'job':'adm.',
        'marital':'divorced', 
        'education': 'high.school',
        'default':'no',
        'housing':'yes',
        'loan':'no',
        'contact':'cellular',
        'month':'may',
        'day_of_week':'fri',
        'duration':334,
        'campaign':3,
        'pdays':999,
        'previous':3,
        'poutcome':'nonexistent',
        'emp.var.rate':3.1,
        'cons.price.idx':82.893,
        'cons.conf.idx':4,
        'euribor3m':2.313,
        'nr.employed':4099.1,
        'euribor3m':2.313,
        'dsfdsf':'dfdg'
       }



r = requests.post(url,json=data)
out = r.text
#Format string
#symbols = ['[',']','{','}']
#for symbol in symbols:
out #= out.replace(symbol,'')


# In[ ]:




