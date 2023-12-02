def process_informations(informations_list):

    info = []

    age = int(informations_list[0])
    
    if age < 4:
        info.extend(['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
    elif 5 <= age <= 9:
        info.extend(['0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
    elif 10 <= age <= 19:
        info.extend(['0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0'])
    elif 20 <= age <= 29:
        info.extend(['0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0'])
    elif 30 <= age <= 39:
        info.extend(['0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0'])
    elif 40 <= age <= 49:
        info.extend(['0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'])
    elif 50 <= age <= 59:
        info.extend(['1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0'])
    elif 60 <= age <= 69:
        info.extend(['0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0'])
    elif 70 <= age <= 79:
        info.extend(['0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'])
    elif 80 <= age <= 89:
        info.extend(['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0'])
    elif age >= 90:
        info.extend(['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'])

    for i in range(2, 9):
        if informations_list[i] == 'sim':
            info.extend(['1', '0'])
        else:
            info.extend(['0', '1'])

    info_csv = ",".join(info)
    
    return info_csv