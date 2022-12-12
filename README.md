# moisture_monitor_RPI

Written using Python. This reads data from a moisture sensor, which is then sent to a Blynk app on a smart phone. The Blynk app will display the data as a both percentage and as a moisture level (low, medium, high). There is an RGB LED, where the color changes based on the moisture level. If the moisture level reaches low, the LED will flash red and send an email telling you to water your plants. Lastly, it will log a message every time the moisture level changes.
