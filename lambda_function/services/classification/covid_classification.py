from utils.process_informations import process_informations


def predict_covid(user_informations):

    array = process_informations(user_informations)

    classification_model = load_model()
    result = classification_model.predict(array)

    return result
