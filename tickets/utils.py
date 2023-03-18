from tort.models import Airport, Company

def decoder(code):
    company = code[0:2]

    flight_number = f"{code[0:2].strip()} {code[2:6].strip()} "


    flight_date = code[9:14].strip()

    flight_departure_time = code[36:40]
    departure_time = f"{flight_departure_time[:2]}:{flight_departure_time[2:]}"

    flight_arrival_time = code[41:45]
    arrival_time = f"{flight_arrival_time[:2]}:{flight_arrival_time[2:]}"

    flight_departure_airport_code = code[17:20]
    flight_arrival_airport_code = code[20:23]

    flight_airplane = code[48:51]#не надо по тз

    flight_plane_type = code[52]#не надо по тз

    month_names = {
        "JAN": "янв.", "FEB": "фев.", "MAR": "мар.", "APR": "апр.",
        "MAY": "мая.","JUN": "июн.", "JUL": "июл.", "AUG": "авг.", "SEP": "сен.",
        "OCT": "окт.", "NOV": "ноя.", "DEC": "дек."
    }

    flight_date = flight_date[:2] + " " + month_names[flight_date[2:5].upper()]

    weekday_names = {
        1: "пн.",
        2: "вт.",
        3: "ср.",
        4: "чт.",
        5: "пт.",
        6: "сб.",
        7: "вс.",
    }

    week_day = weekday_names.get(int(code[15]))

    cl = {
        'Y': 'Economy Class',
        'J': 'Business Class',
        'F': 'First Class'
    }
    dt = cl.get(code[7])


    departure_airport = Airport.objects.get(iata_code=flight_departure_airport_code)
    arrival_airport = Airport.objects.get(iata_code=flight_arrival_airport_code)
    your_company = Company.objects.get(iata_code=company)

    return f"""     
    Дата вылета: {flight_date}
    День недели: {week_day}
    Время вылета: {departure_time}
    Время посадки: {arrival_time}
    Место вылета: {departure_airport} Airport
    Место посадки: {arrival_airport} Airport
    Номер рейса: {flight_number}
    Авиакомпания: {your_company}
    Класс: {dt}
    """