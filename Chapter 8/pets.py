def describe_pet(pet_name,animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hmster', pet_name='harry')
describe_pet(animal_type='dog', pet_name='willie')

describe_pet(pet_name='Baby Drogon')
