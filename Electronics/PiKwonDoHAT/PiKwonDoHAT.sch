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
LIBS:PiKwonDoHAT-cache
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
L RJ12-UNSHLD J2
U 1 1 5B25A715
P 7450 1300
F 0 "J2" H 7650 1800 50  0000 C CNN
F 1 "Judge3" H 7300 1800 50  0000 C CNN
F 2 "PiKwonDo:TH-RJ12" H 7450 1300 50  0001 C CNN
F 3 "" H 7450 1300 50  0001 C CNN
	1    7450 1300
	0    1    1    0   
$EndComp
$Comp
L RJ12-UNSHLD J3
U 1 1 5B25A769
P 7450 2100
F 0 "J3" H 7650 2600 50  0000 C CNN
F 1 "Judge2" H 7300 2600 50  0000 C CNN
F 2 "PiKwonDo:TH-RJ12" H 7450 2100 50  0001 C CNN
F 3 "" H 7450 2100 50  0001 C CNN
	1    7450 2100
	0    1    1    0   
$EndComp
$Comp
L RJ12-UNSHLD J4
U 1 1 5B25A78D
P 7450 2950
F 0 "J4" H 7650 3450 50  0000 C CNN
F 1 "Judge1" H 7300 3450 50  0000 C CNN
F 2 "PiKwonDo:TH-RJ12" H 7450 2950 50  0001 C CNN
F 3 "" H 7450 2950 50  0001 C CNN
	1    7450 2950
	0    1    1    0   
$EndComp
$Comp
L RJ12-UNSHLD J5
U 1 1 5B25A7B5
P 7450 3800
F 0 "J5" H 7650 4300 50  0000 C CNN
F 1 "Controller" H 7300 4300 50  0000 C CNN
F 2 "PiKwonDo:TH-RJ12" H 7450 3800 50  0001 C CNN
F 3 "" H 7450 3800 50  0001 C CNN
	1    7450 3800
	0    1    1    0   
$EndComp
$Comp
L PWR_FLAG #FLG01
U 1 1 5B25A8B6
P 1350 850
F 0 "#FLG01" H 1350 925 50  0001 C CNN
F 1 "PWR_FLAG" H 1350 1000 50  0000 C CNN
F 2 "" H 1350 850 50  0001 C CNN
F 3 "" H 1350 850 50  0001 C CNN
	1    1350 850 
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 5B25D60F
P 1350 850
F 0 "#PWR02" H 1350 600 50  0001 C CNN
F 1 "GND" H 1350 700 50  0000 C CNN
F 2 "" H 1350 850 50  0001 C CNN
F 3 "" H 1350 850 50  0001 C CNN
	1    1350 850 
	1    0    0    -1  
$EndComp
$Comp
L Conn_02x20_Odd_Even J1
U 1 1 5B25D769
P 5600 2600
F 0 "J1" H 5650 3600 50  0000 C CNN
F 1 "Conn_02x20_Odd_Even" H 5650 1500 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x20_Pitch2.54mm" H 5600 2600 50  0001 C CNN
F 3 "" H 5600 2600 50  0001 C CNN
	1    5600 2600
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR03
U 1 1 5B2ADD76
P 7000 1500
F 0 "#PWR03" H 7000 1250 50  0001 C CNN
F 1 "GND" H 7000 1350 50  0000 C CNN
F 2 "" H 7000 1500 50  0001 C CNN
F 3 "" H 7000 1500 50  0001 C CNN
	1    7000 1500
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR04
U 1 1 5B2ADE0B
P 7000 2300
F 0 "#PWR04" H 7000 2050 50  0001 C CNN
F 1 "GND" H 7000 2150 50  0000 C CNN
F 2 "" H 7000 2300 50  0001 C CNN
F 3 "" H 7000 2300 50  0001 C CNN
	1    7000 2300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR05
U 1 1 5B2ADE2A
P 6600 3150
F 0 "#PWR05" H 6600 2900 50  0001 C CNN
F 1 "GND" H 6600 3000 50  0000 C CNN
F 2 "" H 6600 3150 50  0001 C CNN
F 3 "" H 6600 3150 50  0001 C CNN
	1    6600 3150
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR06
U 1 1 5B2ADE44
P 7000 4000
F 0 "#PWR06" H 7000 3750 50  0001 C CNN
F 1 "GND" H 7000 3850 50  0000 C CNN
F 2 "" H 7000 4000 50  0001 C CNN
F 3 "" H 7000 4000 50  0001 C CNN
	1    7000 4000
	1    0    0    -1  
$EndComp
NoConn ~ 7000 1100
NoConn ~ 7000 1600
NoConn ~ 7000 1900
NoConn ~ 7000 2400
NoConn ~ 7000 2750
NoConn ~ 7000 3250
NoConn ~ 7000 3600
NoConn ~ 7000 4100
Wire Wire Line
	7000 1200 6450 1200
Wire Wire Line
	7000 1300 6450 1300
Wire Wire Line
	7000 2000 6450 2000
Wire Wire Line
	7000 2100 6450 2100
Wire Wire Line
	7000 2850 6450 2850
Wire Wire Line
	7000 2950 6450 2950
Wire Wire Line
	7000 3700 6450 3700
Wire Wire Line
	7000 3800 6450 3800
Text Label 6450 1200 0    60   ~ 0
CLK
Text Label 6450 2000 0    60   ~ 0
CLK
Text Label 6450 2850 0    60   ~ 0
CLK
Text Label 6450 3700 0    60   ~ 0
CLK
Text Label 6450 1300 0    60   ~ 0
LOAD
Text Label 6450 2100 0    60   ~ 0
LOAD
Text Label 6450 2950 0    60   ~ 0
LOAD
Text Label 6450 3800 0    60   ~ 0
LOAD
Wire Wire Line
	5800 3400 5850 3400
Wire Wire Line
	5800 3300 5850 3300
Text Label 5850 3400 0    60   ~ 0
CLK
Text Label 5850 3300 0    60   ~ 0
LOAD
Wire Wire Line
	7000 3900 6250 3900
Wire Wire Line
	6250 3900 6250 3200
Wire Wire Line
	6250 3200 5800 3200
Wire Wire Line
	7000 3050 6150 3050
Wire Wire Line
	6150 3050 6150 3000
Wire Wire Line
	6150 3000 5800 3000
Wire Wire Line
	7000 2200 6150 2200
Wire Wire Line
	6150 2200 6150 2900
Wire Wire Line
	6150 2900 5800 2900
Wire Wire Line
	7000 1400 6000 1400
Wire Wire Line
	6000 1400 6000 2800
Wire Wire Line
	6000 2800 5800 2800
Wire Wire Line
	5800 3150 5800 3100
Wire Wire Line
	5800 3150 7000 3150
Connection ~ 6600 3150
NoConn ~ 5300 3500
NoConn ~ 5300 3400
NoConn ~ 5300 3300
NoConn ~ 5300 3200
NoConn ~ 5300 3100
NoConn ~ 5300 3000
NoConn ~ 5300 2900
NoConn ~ 5300 2800
NoConn ~ 5300 2700
NoConn ~ 5300 2600
NoConn ~ 5300 2500
NoConn ~ 5300 2400
NoConn ~ 5300 2300
NoConn ~ 5300 2200
NoConn ~ 5300 2100
NoConn ~ 5300 2000
NoConn ~ 5300 1900
NoConn ~ 5300 1800
NoConn ~ 5300 1700
NoConn ~ 5300 1600
NoConn ~ 5800 3500
NoConn ~ 5800 2700
NoConn ~ 5800 2600
NoConn ~ 5800 2500
NoConn ~ 5800 2400
NoConn ~ 5800 2300
NoConn ~ 5800 2200
NoConn ~ 5800 2100
NoConn ~ 5800 2000
NoConn ~ 5800 1900
NoConn ~ 5800 1800
NoConn ~ 5800 1700
NoConn ~ 5800 1600
$EndSCHEMATC
