from sense_hat import SenseHat
from datetime import datetime

def get_readings():
    """Get the current readings from the SenseHat module and return them as a dictionary"""
    # Setup the SenseHat API and grab data
    sense = SenseHat()
    
    humidity = round(sense.get_humidity(), 2)
    temp = round((sense.get_temperature() * 1.8) + 32, 2) # SenseHat uses Celsius, so convert to Fahrenheit by doing 'multiply by 1.8, add 32'
    pressure = round(sense.get_pressure() / 33.864, 2) # Convert to inHg
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    return {'humidity': humidity, 'temp': temp, 'pressure': pressure, 'time': current_time}
