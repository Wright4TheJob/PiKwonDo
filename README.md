# PiKwonDo
A Raspberry Pi-based system for scoring TaeKwonDo sparring matches.

# Goals
The goal of this project is to create an inexpensive system for scoring TaeKwonDo sparring. This system is intended to be small and easily modified to suit the needs of individual Dojangs. The system is currently designed for electronic scoring manually triggered by corner judges.

Phase 1 of the judging system will use judge triggers connected by wires to the central controller. Phase 2 is intended to use wireless judge trigger systems or mobile phone connectivity.

While the system is designed to mimic expensive World TaeKwonDo-approved systems, it is not currently recommended for official tournament use.

# Status
The project is under early development. No function prototype is ready at this time. Hardware and software folders have individual README files with more particular statuses and todo items.

All design files and software are provided "as-is." Any stable releases will be bundled for easy download, but this does not guarentee suitability for your particular setup.

# Software
The judging software and UI is written in python and QT.
<!--Wireless versions of the software may use Twisted to create a local server.-->

# Hardware

The system is designed and tested on a Raspberry Pi 3. Physical wiring uses phone jacks and lines for data communication to judging triggers. Cases are designed for 3D printing and modeled in Solidworks.
<!--Future iterations may investigate the viability of using the Raspberry Pi Zero W.-->
