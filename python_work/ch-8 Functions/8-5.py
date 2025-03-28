def describe_city(name, country = "India"):
    print(name.title(), 'is in', country.title() + '.')

describe_city('Delhi')
describe_city('Mumbai')
describe_city('London', country='UK')