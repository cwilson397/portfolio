##################################################################
# Programmer: Colby Wilson
# Date: 7/15/2024
# Description: a menu that also calculates wind chill,
# and converts temps from celsius to farenheit, and vice versa
# it will also allow for outputting a wind chill warning if the
# wind chill drops below a certain level, and also has support for
# kph as well as mph
###################################################################


# function to calculate windchill for wind in farenheit
def calculate_wind_chillf(temp_f, wind_mph):
    wind_chill = 35.74 + 0.6215*temp_f - 35.75*(wind_mph**0.16) + 0.4275*temp_f*(wind_mph**0.16)
    return wind_chill

# function for windchill in celsius
def calculate_wind_chillc(temp_c, wind_kph):
    wind_chill = 13.12 + 0.6215*temp_c - 11.37*(wind_kph**0.16) + 0.3965*temp_c*(wind_kph**0.16)
    return wind_chill

# celsius to farenheit
def celsius_farenheit(temp_c):
    return (temp_c * 9/5) + 32

# farenheit to celsius
def farenheit_celsius(temp_f):
    return (temp_f - 32) * 5/9

# function for converting mph to kph
def mph_to_kph(mph):
    return mph * 1.60934

# kph to mph
def kph_to_mph(kph):
    return kph / 1.60934

# calculating wind chill for specific temp and speed
def calculate_specific_wind():
    try:
        temp = float(input("What is the temperature? "))
        temp_unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()
        wind_speed = float(input("Enter wind speed: "))
        wind_speed_unit = input("Wind speed unit (MPH/KPH)? ").strip().upper()

        if temp_unit not in ['F', 'C']:
            print("Invalid temperature unit. Please enter F or C.")
            return

        if wind_speed_unit not in ['MPH', 'KPH']:
            print("Invalid wind speed unit. Please enter MPH or KPH.")
            return

        if temp_unit == 'C' and wind_speed_unit == 'KPH':
            wind_chill = calculate_wind_chillc(temp, wind_speed)
        elif temp_unit == 'C' and wind_speed_unit == 'MPH':
            wind_speed_kph = mph_to_kph(wind_speed)
            wind_chill = calculate_wind_chillc(temp, wind_speed_kph)
        elif temp_unit == 'F' and wind_speed_unit == 'MPH':
            wind_chill = calculate_wind_chillf(temp, wind_speed)
        elif temp_unit == 'F' and wind_speed_unit == 'KPH':
            wind_speed_mph = kph_to_mph(wind_speed)
            wind_chill = calculate_wind_chillf(temp, wind_speed_mph)

        print(f"At temperature {temp:.2f}{temp_unit} and wind speed {wind_speed:.2f} {wind_speed_unit}, the wind chill is: {wind_chill:.2f}{temp_unit}")
        if wind_chill < -40:
            print("  Warning: Extreme wind chill! Risk of frostbite in minutes.")
    except ValueError:
        print("Invalid input. Please enter numeric values for temperature and wind speed.")

# displaying wind chill values
def display_wind_chill(temp, unit, wind_unit):

   temp_display = f"{temp}{unit}"
   
   # display setup
   if unit == 'C':
    if wind_unit == 'KPH':
          wind_speeds = range(5, 65, 5)
          speed_display = 'kph'
    else:
          wind_speeds = [mph_to_kph(wind_speeds) for wind_speeds in range(5, 65, 5)]
          speed_display = 'kph'
   else:
       if wind_unit == "MPH":
           wind_speeds = range(5, 65, 5)
           speed_display = 'mph'
       else:
           wind_speeds = [kph_to_mph(wind_speeds) for wind_speeds in range(5, 65, 5)]
           speed_display = 'mph'

# display values
   print(f"\nAt temperature {temp_display}:")
   for wind_speed in wind_speeds:
       if unit == 'C' and wind_unit == 'KPH':
           wind_chill = calculate_wind_chillc(temp, wind_speed)
       elif unit == 'C' and wind_unit == 'MPH':
           wind_speed_kph = mph_to_kph(wind_speed)
           wind_chill = calculate_wind_chillc(temp, wind_speed_kph)
       elif unit == 'F' and wind_unit == 'MPH':
           wind_chill = calculate_wind_chillf(temp, wind_speed)
       elif unit == 'F' and wind_unit == 'KPH':
           wind_speed_mph = kph_to_mph(wind_speed)
           wind_chill = calculate_wind_chillf(temp, wind_speed_mph)

       print(f" and wind speed {wind_speed:.2f} {speed_display}, the wind chill is: {wind_chill:.2f}{unit}")
       if wind_chill < -40:
           print(f" Warning: Exteme wind chill! Risk of frostbite in minutes.")


def main():
    # while loop
    while True:

        # menu
        print("\nMenu:")
        print("1. Calculate Wind Chill range")
        print("2. Calcualte Wind Chill specifics")
        print("3. Convert Celsius to Farenheit")
        print("4. Convert Farenheit to Celsius")
        print("5. Convert MPH to KPH")
        print("6. Convert KPH to MPH")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        # choice tree
        if choice == '1':
            try:
                temp = float(input("What is the temperature? "))
                temp_unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()
                wind_speed_unit = input("Wind speed unit (MPH/KPH)? ").strip().upper()
                
                if temp_unit not in ['F', 'C']:
                    print("Invalid temperature unit. Please enter F or C.")
                    continue

                if wind_speed_unit not in ['MPH', 'KPH']:
                    print("Invalid wind speed unit. Please enter MPH or KPH.")
                    continue

                display_wind_chill(temp, temp_unit, wind_speed_unit)

            except ValueError:
                print("Invalid input. Please enter a numeric value for temperature.")

        elif choice == '2':
            calculate_specific_wind()

        elif choice == '3':
            try:
                temp_c = float(input("Enter temperature in Celsius: "))
                temp_f = celsius_farenheit(temp_c)
                print(f"{temp_c:.2f}C is {temp_f:.2f}F")
            except ValueError:
                print("Invalid input. Please enter a numeric value for temperature.")

        elif choice == '4':
            try:
                temp_f = float(input("Enter temperature in Fahrenheit: "))
                temp_c = farenheit_celsius(temp_f)
                print(f"{temp_f:.2f}F is {temp_c:.2f}C")
            except ValueError:
                print("Invalid input. Please enter a numeric value for temperature.")
        elif choice == '5':
            try:
                mph = float(input("Enter speed in MPH: "))
                kph = mph_to_kph(mph)
                print(f"{mph:.2f} MPH is {kph:.2f} KPH")
            except ValueError:
                print("Invalid input. Please enter a numeric value for speed.")

        elif choice == '6':
            try:
                kph = float(input("Enter speed in KPH: "))
                mph = kph_to_mph(kph)
                print(f"{kph:.2f} KPH is {mph:.2f} MPH")
            except ValueError:
                print("Invalid input. Please enter a numeric value for speed.")
        
        elif choice == '7':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


main()


    



