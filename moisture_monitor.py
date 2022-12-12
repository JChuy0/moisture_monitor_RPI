from sensor import Sensor
from gpiozero import RGBLED
from time import sleep
import BlynkLib
import logging
from my_emailsender import send_my_email
import my_config as mc


try:
    # replace these with your own values from the Blynk web console
    BLYNK_TEMPLATE_ID = mc.BLYNK_ID
    BLYNK_DEVICE_NAME = mc.BLYNK_NAME
    BLYNK_AUTH_TOKEN = mc.BLYNK_TOKEN

    logging.basicConfig(filename="myapp.log", level=logging.INFO,
                        format="%(asctime)s %(levelname)s: %(message)s",
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)
    led = RGBLED(red=5, green=6, blue=13)
    led.color = (1, 1, 1)  # turns LED off
    old_moist_level = "Low"

    def update_moisture(old_level):
        """Updates the moisture level."""

        try:
            global old_moist_level
            moistvalue = 0
            moistlevel = "Low"

            mySensor = Sensor()
            moistvalue = mySensor.moisture()
            print(f"Current moisture value is: {moistvalue}")
            moistvalue = round((700 - moistvalue) / 700 * 100)

            # sets moisture level and led color
            # The color values on my LED are reversed, so I had to use 0, 1, 1 to display red.
            if moistvalue >= 66:
                moistlevel = "High"
                led.color = (1, 1, 0)  # turns LED blue
            elif moistvalue > 33 and moistvalue <= 66:
                moistlevel = "Normal"
                led.color = (1, 0, 1)  # turns LED green
            else:
                moistlevel = "Low"
                led.color = (0, 1, 1)  # turns LED red

            if old_level != moistlevel:
                logging.info("Moisture level has changed from " +
                             f"{old_moist_level.upper()} to {moistlevel.upper()}.")
                old_moist_level = moistlevel
            moiststring = str(moistvalue) + "%"

            # Writes data to blynk app
            blynk.virtual_write(1, moiststring)
            blynk.virtual_write(2, moistlevel)

            return moistvalue
        except Exception as e:
            logging.error(e)

    while True:
        try:
            sleep(1)
            moistvalue = update_moisture(old_moist_level)

            # Causes LED to flash red
            if moistvalue <= 33:
                print("An email has been sent")
                led.color = (0, 1, 1)  # turns LED red
                sleep(1)
                led.color = (1, 1, 1)  # turns LED off
                sleep(1)
                send_my_email()
        except Exception as e:
            logging.error(e)

except Exception as e:
    logging.error(e)