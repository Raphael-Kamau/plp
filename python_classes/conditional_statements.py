# Boolean values and if condition
def check_weather():
    weather = input("Is it hot or cold? ")

    if  weather == "hot":
        print('''
        It's a hot day.
        ☀☀☀
        Drink a lot of water
              ''')
    elif weather == "cold":
        print('''
        It's a cold day.
        🌧🌧🌧 
        Wear warm clothes.
              ''')
    else:
        print('''
        It's a lovely day.
        Enjoy your day.
              ''')

check_weather()