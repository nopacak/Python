import base64
from pymongo_pipelines import get_price_data
import datetime
import pandas as pd

date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_file = f"logs/robot_{date}.log"

# Decode login credentials from base64
user = base64.b64decode("*********").decode('utf-8')
secret = base64.b64decode("*********").decode('utf-8')

# Get the offer IDs from the database
offer_ids, csv_file = get_price_data()
unique_ids = pd.read_csv(csv_file).drop_duplicates(subset='Column Name')["ID"].tolist()

def log_step(message, log_file):
    """Function to log each step of the process to a file with a timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"{timestamp} - {message}\n"
    with open(log_file, "a") as file:
        file.write(full_message)
    #print(full_message)  # Print to standard output as well
        
def create_new_df_columns(csv_file):
    """Function to create new columns in the csv file."""
    df = pd.read_csv(csv_file)
    df["Column1"] = ""
    df["Column2"] = ""
    df["Column3"] = ""
    df["Status"] = ""
    df["ErrorStage"] = pd.NA
    df["Runtime"] = pd.NA
    df.to_csv(csv_file, index=False)

def set_status_column(offer_id, status):
    """Function to update the status column in the csv file."""
    df = pd.read_csv(csv_file)
    df.loc[df['ID'] == offer_id, 'Status'] = status
    df["Status"] = df["Status"].astype(str)
    grouped = df.groupby('Base Price')
    df['Status'] = grouped['Status'].transform(lambda x: x.ffill().bfill())
    df.to_csv(csv_file, index=False)
