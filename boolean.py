# BOOLEAN - true or false
# IF THEN ELSE- conditional test
# comparison operators; ==,>,<, >=,<=

# weather app
# weather = input("How is the weather? ")
#
# if weather == 'rain':
#     print('umbrella')
# elif weather == 'cloudy':
#     print('Hoodie')
# elif weather == 'thunderstorm':
#     print('Stay indoors')
# else:
#     print('sun glasses')


# check grades
# >90 A
# >80 B
# >70 c
# >60 D
# < 60 F


score = int(input("Enter your score: "))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
elif score < 60:
    print('F')
else:
    print('Invalid Inputs')
