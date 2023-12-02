import os
import boto3
from utils.process_informations import process_informations
from dotenv import load_dotenv

load_dotenv()

sagemaker = boto3.client('sagemaker-runtime',
                    region_name= os.getenv('region_name'),
                    aws_access_key_id=os.getenv('aws_access_key_id'),
                    aws_secret_access_key=os.getenv('aws_secret_access_key'))
    


def get_predictions(covid_data):
    
    formatted_data = process_informations(covid_data)
    
    predict = sagemaker.invoke_endpoint(
        EndpointName=os.getenv('endpoint_name'), Body=formatted_data, ContentType="text/csv"
    )

    predict_value = int(float(predict["Body"].read().decode("utf-8")))

    return predict_value