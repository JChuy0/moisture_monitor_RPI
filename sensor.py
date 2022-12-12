from grove.adc import ADC
import logging

class Sensor():
    """Returns a value from an analog sensor."""

    try:
        def moisture(self):
            """Returns the value from the moisture sensor."""

            try:
                aio = ADC(address=0x08)
                moistvalue = aio.read(5)

                if moistvalue > 700:
                    moistvalue = 700

                return moistvalue
            except Exception as e:
                logging.error(e)
    except Exception as e:
        logging.error(e)