# Helen Court Sensor

Simple Python Flask program that makes use of the Raspberry Pi SenseHat to take measurements of the room temperature, humidity, and pressure. If temperature or humidity over acceptable levels, send a text message using Twilio.

Temperature is converted from Celsius to Fahrenheit, and pressure if converted from millibars to inches of mercury (inHg).
