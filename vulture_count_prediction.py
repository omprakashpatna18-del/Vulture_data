import pandas as pd
import numpy as np
import joblib
from pydantic import BaseModel
try:
  model=joblib.load("knn_model")
except Exception as e:
  print(e)
  return "Model Not Found
class vulture:
  
