import pandas as pd
import json
import requests
from datetime import datetime
import s3fs

# get data from pinball API
res = requests.get('https://pinballmap.com/api/v1/regions.json')

if res.status_code == 200:
    data = res.json() # Parse the JSON response
    
    # Print the data (or process it as needed)
    # print(data)
else:
    print(f"Failed to retrieve data: {res.status_code}")