#from sense_hat import SenseHat
from datetime import datetime

def get_readings():
    """Get the current readings from the SenseHat module and return them as a dictionary"""
    # Setup the SenseHat API and grab data
    #sense = SenseHat()
    
    #humidity = sense.get_humidity()
    #temp = (sense.get_temperature() * 1.8) + 32 # SenseHat uses Celsius, so convert to Fahrenheit by doing 'multiply by 1.8, add 32'
    #pressure = sense.get_pressure()
    humidity = 20.0
    temp = 80.0
    pressure = 10.0
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    return {'humidity': humidity, 'temp': temp, 'pressure': pressure, 'time': current_time}
