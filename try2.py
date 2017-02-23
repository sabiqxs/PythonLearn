contacts = [
    {
        'name': 'Bob',
        'age': 23,
        'married': False,
        'height': 1.8,  # meters
        'languages': ['English', 'Spanish'],
        'address': '123 Maple St.',
        'phone': '(555) 555-5555'
    },

    {'name': 'Sally',
     'age': 26,
     'married': True,
     'height': 1.5,  # meters
     'languages': ['English'],
     'address': '456 Elm St.',
     'phone': '(555) 555-1234'
     }
]

for contact in contacts:
    print("Name:", contact['name'])
    print("Married:", contact['married'])