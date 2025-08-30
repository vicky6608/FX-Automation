import requests
import os
import time
from datetime import datetime
fx_url = "https://www.bankofcanada.ca/valet/observations/group/FX_RATES_MONTHLY/csv?start_date=2017-01-01"
folder = r"C:\Users\Raw Data"

while True :
    ts = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    folder_path = os.path.join(folder,ts)
    os.makedirs(folder_path,exist_ok = True)
    file_path = os.path.join(folder_path,"FX_Bank_of_Canada.csv")

    response = requests.get(fx_url)
    response.raise_for_status()
    
    with open(file_path, "wb") as file:
        file.write(response.content)

    print(f"Downloaded at {ts}")

    time.sleep(60)


