M=eval(raw_input('Enter the amount of water in kilograms:'))
finalTemperature=eval(raw_input('Enter the initial temperature:'))
initiallTemperature=eval(raw_input('Enter the fanal temperature:'))
Q = M * (finalTemperature - initiallTemperature) * 4184
print('The energy needed is {}'.format(-Q))

