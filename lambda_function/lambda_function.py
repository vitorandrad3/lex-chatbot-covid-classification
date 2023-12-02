from utils.get_slot import get_slot
from services.dynamo.put_on_dynamo import put_on_dynamo
from services.classification.covid_classification import predict_covid
from services.sagemaker.get_predictions import get_predictions


def lambda_handler(event, context):
    informations_list = []
    informations_list.extend([get_slot(event, 'idade'),get_slot(event, 'sexo'), get_slot(event, 'febre'), get_slot(event, 'dificuldadeRespiratoria'),   get_slot(event, 'tosse'),get_slot(event, 'coriza'), get_slot(event, 'dorGarganta'), get_slot(event, 'diarreia'),  get_slot(event, 'dorCabeca'),get_slot(event, 'comorbidadeObesidade'), get_slot(event, 'comorbidadeDiabetes'), get_slot(event, 'comorbidadeCardio'), get_slot(event, 'comorbidadePulmao'), get_slot(event, 'comorbidadeRenal'), get_slot(event, 'comorbidadeTabagismo')])

    
    result_pred = get_predictions(informations_list)
    
    informations_list.append(result_pred)
    
    put_on_dynamo(informations_list) 
    
    if result_pred == 0:
        
        message = "Com base nas informações apresentadas, é pouco provável que esteja infectado pelo COVID-19. No entanto, é importante manter as práticas de prevenção, para continuar protegendo a si mesmo e os outros. Embora as chances sejam baixas, a COVID-19 pode se espalhar de forma assintomática em alguns casos, então a precaução é essencial."
        
    else:
        
        message = "É possível que você esteja infectado pelo vírus do COVID-19. Recomendo que você entre em contato com um profissional de saúde para obter orientações específicas. É essencial fazer o teste de COVID-19 e seguir as medidas de isolamento, caso seja recomendado."
        
    
    intent_response = {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                "confirmationState": "Confirmed",
                "name": "collect-informations",
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": message
            }
        ]
    }

    return intent_response