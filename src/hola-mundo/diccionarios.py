# Diccionarios
fili = {
        "id": 1,
        "name": "Angel",
        "lastName": "Rebollo"
    }

print fili

# Base de Datos con diccionarios
DB = [
        {
            "id": 1,
            "name": "Angel",
            "lastName": "Rebollo",
            "gender": "Masculine",
            "age": 22,
        },
        {
            "id": 2,
            "name": "Francisco",
            "lastName": "Pachueco",
            "gender": "Masculine",
            "age": 22,
        },
        {
            "id": 3,
            "name": "Ricardo",
            "lastName": "Raya",
            "gender": "Masculine",
            "age": 22,
        },
        {
            "id": 4,
            "name": "Maribel",
            "lastName": "Vidal",
            "gender": "Femenine",
            "age": 22,
        }
    ]

print
for person in DB:
    print "ID: ", person['id']
    print "Name: ", person['name']
    print "Last Name:", person['lastName']
    print "Gender: ", person['gender']
    print "Age: ", person['age'], "Years Old"
    print