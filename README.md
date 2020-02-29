# Cupcake-Flasher
Firmware flasher for Makerbot Cupcake Electronics

v0.0.1 ALPHA (WIP)

_**Designed By The Mad Noodle Prototypes & Roboto.NYC**_

![Cupcake Flasher Screen Shot](https://static.wixstatic.com/media/59d0ff_f8962ed15639492c8ae3b08d66449426~mv2.jpg)

Instructions
---

#### Requirements

- USBtiny ISP AVR Programer
- avrdude CLI (included in the `Drivers` folder or automaticaly installed if useing `Cupcake Flasher Setup.exe`)


#### **Install**
- Launch `Cupcake Flasher Setup.exe`
- Installer will lauch `WinAVR` installer automatically
- Allow `WinAVR` and `AVRdude` to insall
- While those are installing `WinAVR` ensure thate you leave ALL deault options checked
- Once complete, Launch `Cupcake Flasher` from either your _**Desktop shortcut**_ or from your _**Start menu**_.


###### Test
- Open CMD and type `avrdude`
- If error, try install process again


#### Flash Firmware

1. Open Cupcake Flasher
2. From drop down menu, select your desired firmware

    >_Note: This includes firmware for the both the RepRap Mother Board and The Extruder Controller
    The default we use is `Motherboard Firmware v2.2`  & `Extruder Controller Firmware v3.0 (Relay)`_
 3. Connect your USBtiny ISP to the board and click **Flash**
