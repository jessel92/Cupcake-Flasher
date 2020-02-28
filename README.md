# Cupcake-Flasher
Firmware flasher for Makerbot Cupcake Electronics

v0.0.1 ALPHA (WIP)

_**Designed By The Mad Noodle Prototypes & Roboto.NYC**_

Instructions
---

#### Requirements

- USBtiny ISP AVR Programer
- avrdude CLI (included in the `Drivers` folder)


#### **Install Drivers**
1. Navigate to the install folder for Cupcake Flasher
2. In the "`Drivers`" folder install "`WinAVR-20100110-install.exe`"

###### Test
- Open CMD and type `avrdude`
- If error, try install process again


#### Flash Firmware

1. Open Cupcake Flasher
2. From drop down menu, select your desired firmware

    _Note: This includes firmware for the both the RepRap Mother Board and The Extruder Controller
    The default we use is `Motherboard Firmware v2.2`  & `Extruder Controller Firmware v3.0 (Relay)`_
 3. Connect your USBtiny ISP to the board and click **Flash**