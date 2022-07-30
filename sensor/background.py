from .sensor import get_db, app
from time import sleep
from twilio.rest import Client
from .readings import get_readings

def scheduler():
    countdown = 1
    while True:
        current = get_readings()
        standard_check(current)
        countdown = countdown - 1

        if countdown == 0:
            hourly(current)
            countdown = 60

        sleep(60)

def standard_check(current):
    if current['temp'] > app.config.get("ALERT_TEMP") or current['humidity'] > app.config.get("ALERT_HUMIDITY"):
        alert(current['temp'], current['humidity'])

def hourly(current):
    with app.app_context():
        db = get_db()
        try:
            db.execute(
                "INSERT INTO readings (temperature, humidity, pressure) VALUES (?, ?, ?)",
                (current['temp'], current['humidity'], current['pressure']),
                )
            db.commit()
        except db.IntegrityError:
            error = "Error adding to database"

def alert(temp, humidity):
    account_sid = app.config.get("TWILIO_SID")
    auth_token = app.config.get("TWILIO_AUTH")
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        messaging_service_sid=app.config.get("TWILIO_MESSAGING_ID"),
        body='Temperature or humidity out of acceptable range, current temp is ' + str(temp) + ' degrees F and humidity is '+ str(humidity) + '%.',
        to=app.config.get("TWILIO_CONTACT_NUM")
        )
    print(account_sid)
