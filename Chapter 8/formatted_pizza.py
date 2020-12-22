def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name

musican = get_formatted_name('jimmi', 'hendrix')
print(musican)

musican = get_formatted_name('jimmi', 'hendrix', 'dree')
print(musican)
