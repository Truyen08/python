## tinh' chi? so' gio' lanh.
T = float(input("Enter air temperature (°C): "))
V = float(input("Enter wind speed (km/h): "))

WCI = 13.12 + 0.6215*T - 11.37*(V**0.16) + 0.3965*T*(V**0.16)
print("Wind Chill Index =", round(WCI))
