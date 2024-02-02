# This file executes all defined process steps 
from robocorp.tasks import task
from task_description import *
from pymongo_pipelines import get_offer_data
import traceback


@task   # When you decorate a function with @task, it designates that function as a task that can be run by the robocorp-tasks runner.
def insurance_calculation():
    create_new_df_columns(csv_file)
    for offer_id in unique_ids:
        start_time = time.time()
        current_step = "1. Starting process"
        stage = 1
        try:
            if offer_id is None:
                print("No offer ID")
                continue

            offer_data = get_offer_data(offer_id)
            """Login to Crosig and calculate the insurance premium"""
            current_step = "2. Opening the Crosig website"
            stage = 2
            open_the_website()
            current_step = "3. Logging in"
            stage = 3
            log_in()
            current_step = "4. Navigating to data input"
            stage = 4
            if navigate_website_to_data_input(offer_id):
                continue
            current_step = "5. Calculating the insurance premium"
            stage = 5
            if calculate_insurance_premium(offer_data):
                continue
            current_step = "6. Showing the calculated premium"
            stage = 6
            show_premium(offer_id, bonus)
        except Exception as e:
            error_message = f"An error occurred: {str(e)}\n{traceback.format_exc()}"
            error_message_2  = str(e).split('\n')[0]
            log_step(error_message, log_file)

            df = pd.read_csv(csv_file)
            # Check if the 'Status' column is empty or NaN for the specific ID, then update
            condition = (df['ID'] == offer_id) & (df['Status'].isna() | (df['Status'] == ''))
            df.loc[condition, 'Status'] = f"An error occurred at step '{current_step}': {error_message_2}"
            df["Status"] = df["Status"].astype(str)
            df.loc[condition, 'ErrorStage'] = stage
            df.to_csv(csv_file, index=False)
            continue

        finally:
            close_browser()
            end_time = time.time()  # End time for this offer ID
            runtime = end_time - start_time
            df = pd.read_csv(csv_file)
            df.loc[df['ID'] == offer_id, 'Runtime'] = round(runtime, 2)
            df.to_csv(csv_file, index=False)

            
