import pandas as pd
import numpy as np
import joblib
from pydantic import BaseModel
try:
  model=joblib.load("knn_model")
except Exception as e:
  print(e)
  return "Model Not Found

columns=['decimalLatitude', 'decimalLongitude', 'year', 'Arunachal Pradesh',
       'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Delhi', 'Goa',
       'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir',
       'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Madhya Pradesh',
       'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha',
       'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
       'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Gyps fulvus',
       'Gyps himalayensis', 'Gyps indicus', 'Gyps tenuirostris', 'month_sin',
       'month_cos', 'day_sin', 'day_cos']

vulture_df=pd.DataFrame(data=np.array([0]*len(columns),columns=columns)
                        
def data_preprocessor(lat,lon,year,state,species,month,day):
  try:
    vulture_df['decimalLatitude']=lat
    vulture_df['decimalLongitude']=lon
    vulture_df['year']=year
    vulture_df[state]=1
    vulture_df[species]=1
    vulture_df['month_sin']=np.sin((2*np.pi*month)/12)
    vulture_df['month_cos']=np.cos((2*np.pi*month)/12)
    vulture_df['day_sin']=np.sin((2*np.pi*day)/31)
    vulture_df['day_cos']=np.cos((2*np.pi*day)/31)
    count=model.predict(vulture_df)
    final_counts = np.round(np.expm1(count)).astype(int)
    return {"predicted_count":final_counts}
  except Exception as e:
    print(e)
    return "Software not working right now. Please try again later."

  
  
  
  
  
