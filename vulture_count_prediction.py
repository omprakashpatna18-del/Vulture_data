import pandas as pd
import numpy as np
import joblib

try:
  model=joblib.load("knn_model")
except Exception as e:
  print(e)
  model=None

columns=['decimalLatitude', 'decimalLongitude', 'year', 'Arunachal Pradesh',
       'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Delhi', 'Goa',
       'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir',
       'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Madhya Pradesh',
       'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha',
       'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
       'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Gyps fulvus',
       'Gyps himalayensis', 'Gyps indicus', 'Gyps tenuirostris', 'month_sin',
       'month_cos', 'day_sin', 'day_cos']
                        
def data_preprocessor(lat,lon,year,state,species,month,day):
  vulture_df=pd.DataFrame(data=np.zeros(1,len(columns)),columns=columns)
  if model is None:
    return {"meesage":"Software not working right now. Please try again later."}
  try:
    vulture_df['decimalLatitude']=float(lat)
    vulture_df['decimalLongitude']=float(lon)
    vulture_df['year']=year
    if state in df.columns:
       vulture_df[state]=1
    if species in df.columns:
       vulture_df[species]=1
    vulture_df['month_sin']=np.sin((2*np.pi*month)/12)
    vulture_df['month_cos']=np.cos((2*np.pi*month)/12)
    vulture_df['day_sin']=np.sin((2*np.pi*day)/31)
    vulture_df['day_cos']=np.cos((2*np.pi*day)/31)
    count=model.predict(vulture_df)
    final_counts = np.round(np.expm1(count)).astype(int)
    return {"predicted_count":final_counts[0]}
  except Exception as e:
    print(e)
    return {"message": "Software not working right now. Please try again later."}

  
  
  
  
  
