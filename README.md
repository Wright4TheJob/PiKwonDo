# PiKwonDo
A Raspberry Pi-based system for scoring TaeKwonDo sparring matches.

# Goals
The goal of this project is to create an inexpensive system for scoring TaeKwonDo sparring. This system is intended to be small and easily modified to suit the needs of individual Dojangs. The system is currently designed for electronic scoring manually triggered by corner judges.

Phase 1 of the judging system will use judge triggers connected by wires to the central controller. Phase 2 is intended to use wireless judge trigger systems or mobile phone connectivity.

While the system is designed to mimic expensive World TaeKwonDo-approved systems, it is not certified for official tournament use.

# Status
The project is under alpha development. Software has been developed but has yet to be tested with the hardware. Electronics are designed for single-sided PCB routing and have all completed initial design but have not been tested yet. Cases are designed for 3D printing. Hardware and software folders have individual README files with more particular statuses and todo items.

All design files and software are provided "as-is." Any stable releases will be bundled for easy download, but this does not guarantee suitability for your particular setup.

Bill of Materials (BOM) table validation: [![goodtables.io](https://goodtables.io/badge/github/Wright4TheJob/PiKwonDo.svg)](https://goodtables.io/github/Wright4TheJob/PiKwonDo)

# Software
The judging software and UI is written in python and QT. A dedicated thread scans the status of judge controller buttons. Game logic and UI are run as the primary thread.
<!--Wireless versions of the software may use Twisted to create a local server.-->

# Electronics
Controllers use shift registers to store and sequentially read out the values of the buttons in each controller. Judge controllers have 10 buttons and the timer controller has 5. PCBs are designed for single-side milling, with traces no smaller than 0.4mm and trace gaps of 0.3mm. Through-hole components are used for hand soldering and occasional jumper wires are used.

# Hardware
The system is designed and tested on a Raspberry Pi 3B+. Physical wiring uses phone jacks and standard 4-conductor phone cables for data communication to judging triggers. Cases are designed for 3D printing and modeled in Solidworks.
<!--Future iterations may investigate the viability of using the Raspberry Pi Zero W.-->
