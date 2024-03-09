while True:
   convert = int(input("What do you want to convert:\n\n Celsius to Fahrenheit (1)\n\n Fahrenheit to Celsius (2)\n\n Kilograms to Pounds (3)\n\n Pounds to Kilograms (4)\n\n Meters to Feet (5)\n\n Feet to Meters (6)\n\n Kilometers to miles (7)\n\n Miles to kilometers (8)\n\n Knots to m/s km/h and beaufort (9)\n\n Beaufort to m/s km/h and knots (10)\n\n Exit (11)\n\n"))

   if convert == 1:
      cels = float(input("How many Celsius: "))
      print("It is",round(9/5 * cels + 32, 2),"in fahrenheit")
      
   if convert ==2:
      fahr=float(input("How many Fahrenheit: "))
      print("Its ", round(5/9 * (fahr -32),1),"in celsius")

   if convert==3:
      kg=float(input("How many kilograms: "))
      print("It is", round(kg * 2.2, 2),"in pounds")

      
   if convert==4:
      lbs=float(input("How many pounds: "))
      print("It is", round(lbs / 2.2, 2) ,"in kilograms")

   if convert==5:
      meters=float(input("How many meters: "))
      print("It is", round(meters*3.28, 2) ,"in feet")

   if convert==6:
      feet=float(input("How many feet: "))
      print("It is", round(feet/3.28, 2) ,"in meters")

   if convert==7:
      kmh=float(input("How many km/h: "))
      print("It is", round(kmh /1.6, 2) ,"in miles")

   if convert==8:
      mph=float(input("How many mph: "))
      print("It is", round(mph * 1.6, 2) ,"in km/h")

   if convert==9:
      knots=float(input("How many knots: "))
      print("It is", round(knots/1.94, 2) ,"m/s", round(knots*1.852, 2), "km/h", "and")
      if knots < 1:
         print("It's 0 in beaufort scale and the wind is calm") 
      if knots >=1 and knots <=3:
         print("It's 1 in beaufort scale and the wind is light")
      if knots >=4 and knots <=6: 
         print("It's 2 in beaufort scale and the wind is a light breeze")
      if knots >=7 and knots <=10:
         print("It's 3 in beaufort scale and the wind is a gentle breeze")
      if knots >=11 and knots <=16:
         print("I'ts 4 in beaufort scale and the wind is a moderate breeze")
      if knots >=17 and knots <=21:
         print("It's 5 in beaufort scale and the wind is a fresh breeze")
      if knots >=22 and knots <=27:
         print("It's 6 in beaufort scale and the wind is a strong breeze")
      if knots >=28 and knots <=33:
         print("It's 7 in beaufort scale and the wind is near gale")
      if knots >=34 and knots <=40:
         print("It's 8 in beaufort scale and the wind is a gale")
      if knots >=41 and knots <=47:
         print("It's 9 in beaufort scale and the wind is a strong gale")
      if knots >=48 and knots <=55:
         print("It's 10 in beaufort scale and it's a storm")
      if knots >=56 and knots <=63:
         print("It's 11 in beaufort scale and it's a violent storm")
      if knots >=64:
         print("It's 12 in beaufort scale and its a hurricane")
      
   if convert==10:
      beaufort=float(input("How many in beaufort scale (from 0-12):  "))
      
      if beaufort==0:
         print("It's 0 - 0,2 m/s, <1 km/h and < 1 knot")
      if beaufort==1:
         print("It's 0,3 - 1,5 m/s, 1 - 5 km/h and 1-3 knot")
      if beaufort==2:
         print("It's 1,6 - 3,3 m/s, 6 - 11 km/h and 4-6 knot")
      if beaufort==3:
         print("It's 3,4 - 5,4 m/s, 12-19 km/h and 7-10 knot")
      if beaufort==4:
         print("It's 5,5 - 7,9 m/s, 20-28 km/h and 11-16 knot")
      if beaufort==5:
         print("It's 8,0 - 10,7 m/s, 29-38 km/h and 17-21 knot")
      if beaufort==6:
         print("It's 10,8 - 13,8 m/s, 39-49 km/h and 22-27 knot")
      if beaufort==7:
         print("It's 13,9 - 17,1 m/s, 50-61 km/h and 28-33 knot")
      if beaufort==8:
         print("It's 17,2 - 20,7 m/s, 62-74 km/h and 34-40 knot")
      if beaufort==9:
         print("It's 20,8 - 24,4 m/s, 75-88 km/h and 41-47 knot")
      if beaufort==10:
         print("It's 24,5 - 28,4 m/s, 89-102 km/h and 48-55 knot")
      if beaufort==11:
         print("It's 28,5 - 32,6 m/s, 103-117 km/h and 56-63 knot")
      if beaufort==12:
         print("It's >= 32,7 m/s, >= 118 km/h and >= 64 knot")

   if convert==11:
      print("You have chosen to exit")
   break