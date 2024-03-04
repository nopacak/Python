# This file executes all defined process steps 
from robocorp.tasks import task
from .task_description import *
from .pymongo_pipelines import get_offer_data
import pandas as pd
import traceback

@task   # When you decorate a function with @task, it designates that function as a task that can be run by the robocorp-tasks runner.
def insurance_calculation(offer_id):

    df = pd.DataFrame()
    start_time = time.time()
    
    try:
        stage = 1
        df, offer_data = get_offer_data(offer_id)
        
        if offer_id is None:
            df["Status"] = "Error. Offer ID is missing."
            return df

        """Login to insurance provider website and calculate the insurance premium"""
        stage = 2
        open_the_website()

        for stage, action in enumerate([
            lambda df: log_in(df),
            lambda df: navigate_website_to_data_input(df),
            lambda df: calculate_insurance_premium(df, offer_data),
            lambda df: show_premium(df, offer_data)
            ], start=3):  
            df, success = action(df)
            if success:
                return df

    except Exception as e:
        error_message = f"An error occurred: {str(e)}\n{traceback.format_exc()}"
        df['Status'] = "Error. Manual calculation required."
        df['ErrorLog'] = error_message
        df['ErrorStage'] = stage
        return df

    finally:
        close_browser()
        end_time = time.time()  # End time for this offer ID
        runtime = end_time - start_time
        df['Runtime'] = round(runtime, 2)
        return df
