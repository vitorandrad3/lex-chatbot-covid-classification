import os
import boto3
import uuid
from dotenv import load_dotenv

def put_on_dynamo(informations_list):
    
    dynamodb = boto3.client('dynamodb',
                    region_name= os.getenv('region_name'),
                    aws_access_key_id=os.getenv('aws_access_key_id'),
                    aws_secret_access_key=os.getenv('aws_secret_access_key'))
    
    
    
    table_name = 'covid_dataset'

    item = {
        'id': {'S': str(uuid.uuid4())},
        'idade': {'S': informations_list[0]},
        'sexo': {'S': informations_list[1]},
        'febre': {'S': informations_list[2]},
        'dorGarganta': {'S': informations_list[3]},
        'diarreia': {'S': informations_list[4]},
        'dificuldadeRespiratoria': {'S': informations_list[5]},
        'coriza': {'S': informations_list[6]},
        'dorCabeca': {'S': informations_list[7]},
        'tosse': {'S': informations_list[8]},
        'comorbidadeObesidade': {'S': informations_list[9]},
        'comorbidadeDiabetes': {'S': informations_list[10]},
        'comorbidadeCardio': {'S': informations_list[11]},
        'comorbidadePulmao': {'S': informations_list[12]},
        'comorbidadeRenal': {'S': informations_list[13]},
        'comorbidadeTabagismo': {'S': informations_list[14]},
        'possivelInfeccao': {'N': str(informations_list[15])}

    }

    dynamodb.put_item(
        TableName=table_name,
        Item=item
    )
