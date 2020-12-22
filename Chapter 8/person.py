def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person (un pinshy direccionario) """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musican = build_person('jimmi drogas', 'hendrix')
print(musican)

musican = build_person('jimmi drogas', 'hendrix', 27)
print(musican)
