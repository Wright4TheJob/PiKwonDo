EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L 74LS166 U?
U 1 1 5AEB82D1
P 3750 2650
F 0 "U?" H 3750 2900 50  0000 C CNN
F 1 "74LS166" H 3750 2700 50  0000 C CNN
F 2 "" H 3750 2650 50  0001 C CNN
F 3 "" H 3750 2650 50  0001 C CNN
	1    3750 2650
	1    0    0    -1  
$EndComp
$Comp
L 74LS166 U?
U 1 1 5AEB830F
P 3750 4400
F 0 "U?" H 3750 4650 50  0000 C CNN
F 1 "74LS166" H 3750 4450 50  0000 C CNN
F 2 "" H 3750 4400 50  0001 C CNN
F 3 "" H 3750 4400 50  0001 C CNN
	1    3750 4400
	1    0    0    -1  
$EndComp
Wire Wire Line
	3050 3050 2650 3050
Wire Wire Line
	2650 3050 2650 4800
Wire Wire Line
	2650 4800 3050 4800
Wire Wire Line
	3050 3300 2800 3300
Wire Wire Line
	2800 3300 2800 5050
Wire Wire Line
	2800 5050 3050 5050
$Comp
L R_Network08 RN?
U 1 1 5AEB84F7
P 2300 2200
F 0 "RN?" V 1800 2200 50  0000 C CNN
F 1 "R_Network08" V 2700 2200 50  0000 C CNN
F 2 "Resistors_THT:R_Array_SIP9" V 2775 2200 50  0001 C CNN
F 3 "" H 2300 2200 50  0001 C CNN
	1    2300 2200
	1    0    0    -1  
$EndComp
$Comp
L R_Network08 RN?
U 1 1 5AEB8531
P 1950 4250
F 0 "RN?" V 1450 4250 50  0000 C CNN
F 1 "R_Network08" V 2350 4250 50  0000 C CNN
F 2 "Resistors_THT:R_Array_SIP9" V 2425 4250 50  0001 C CNN
F 3 "" H 1950 4250 50  0001 C CNN
	1    1950 4250
	1    0    0    -1  
$EndComp
$EndSCHEMATC
