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
LIBS:Device
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
P 1450 1150
F 0 "J2" H 1650 1650 50  0000 C CNN
F 1 "Judge3" H 1300 1650 50  0000 C CNN
F 2 "PiKwonDo:TH-RJ12" H 1450 1150 50  0001 C CNN
F 3 "" H 1450 1150 50  0001 C CNN
	1    1450 1150
	0    -1   1    0   
$EndComp
$Comp
L RJ12-UNSHLD J3
U 1 1 5B25A769
P 1450 2100
F 0 "J3" H 1650 2600 50  0000 C CNN
F 1 "Judge2" H 1300 2600 50  0000 C CNN
F 2 "PiKwonDo:TH-RJ12" H 1450 2100 50  0001 C CNN
F 3 "" H 1450 2100 50  0001 C CNN
	1    1450 2100
	0    -1   1    0   
$EndComp
$Comp
L RJ12-UNSHLD J4
U 1 1 5B25A78D
P 1450 3150
F 0 "J4" H 1650 3650 50  0000 C CNN
F 1 "Judge1" H 1300 3650 50  0000 C CNN
F 2 "PiKwonDo:TH-RJ12" H 1450 3150 50  0001 C CNN
F 3 "" H 1450 3150 50  0001 C CNN
	1    1450 3150
	0    -1   1    0   
$EndComp
$Comp
L RJ12-UNSHLD J5
U 1 1 5B25A7B5
P 1450 4100
F 0 "J5" H 1650 4600 50  0000 C CNN
F 1 "Controller" H 1300 4600 50  0000 C CNN
F 2 "PiKwonDo:TH-RJ12" H 1450 4100 50  0001 C CNN
F 3 "" H 1450 4100 50  0001 C CNN
	1    1450 4100
	0    -1   1    0   
$EndComp
$Comp
L PWR_FLAG #FLG01
U 1 1 5B25A8B6
P 11000 750
F 0 "#FLG01" H 11000 825 50  0001 C CNN
F 1 "PWR_FLAG" H 11000 900 50  0000 C CNN
F 2 "" H 11000 750 50  0001 C CNN
F 3 "" H 11000 750 50  0001 C CNN
	1    11000 750 
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 5B25D60F
P 11000 750
F 0 "#PWR02" H 11000 500 50  0001 C CNN
F 1 "GND" H 11000 600 50  0000 C CNN
F 2 "" H 11000 750 50  0001 C CNN
F 3 "" H 11000 750 50  0001 C CNN
	1    11000 750 
	-1   0    0    -1  
$EndComp
$Comp
L Conn_02x20_Odd_Even J1
U 1 1 5B25D769
P 10750 3950
F 0 "J1" H 10800 4950 50  0000 C CNN
F 1 "Conn_02x20_Odd_Even" H 10800 2850 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x20_Pitch2.54mm" H 10750 3950 50  0001 C CNN
F 3 "" H 10750 3950 50  0001 C CNN
	1    10750 3950
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR03
U 1 1 5B2ADD76
P 1900 1350
F 0 "#PWR03" H 1900 1100 50  0001 C CNN
F 1 "GND" H 1900 1200 50  0000 C CNN
F 2 "" H 1900 1350 50  0001 C CNN
F 3 "" H 1900 1350 50  0001 C CNN
	1    1900 1350
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR04
U 1 1 5B2ADE0B
P 1900 2300
F 0 "#PWR04" H 1900 2050 50  0001 C CNN
F 1 "GND" H 1900 2150 50  0000 C CNN
F 2 "" H 1900 2300 50  0001 C CNN
F 3 "" H 1900 2300 50  0001 C CNN
	1    1900 2300
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR05
U 1 1 5B2ADE2A
P 2050 3350
F 0 "#PWR05" H 2050 3100 50  0001 C CNN
F 1 "GND" H 2050 3200 50  0000 C CNN
F 2 "" H 2050 3350 50  0001 C CNN
F 3 "" H 2050 3350 50  0001 C CNN
	1    2050 3350
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR06
U 1 1 5B2ADE44
P 1900 4300
F 0 "#PWR06" H 1900 4050 50  0001 C CNN
F 1 "GND" H 1900 4150 50  0000 C CNN
F 2 "" H 1900 4300 50  0001 C CNN
F 3 "" H 1900 4300 50  0001 C CNN
	1    1900 4300
	-1   0    0    -1  
$EndComp
NoConn ~ 1900 950 
NoConn ~ 1900 1450
NoConn ~ 1900 1900
NoConn ~ 1900 2400
NoConn ~ 1900 2950
NoConn ~ 1900 3450
NoConn ~ 1900 3900
NoConn ~ 1900 4400
Text Label 8450 950  2    60   ~ 0
CLK
Text Label 7950 1900 2    60   ~ 0
CLK
Text Label 5450 1150 2    60   ~ 0
J1_LOAD
Text Label 5250 2100 2    60   ~ 0
J2_LOAD
Text Label 5400 3150 2    60   ~ 0
J3_LOAD
Text Label 5350 4100 2    60   ~ 0
C_LOAD
Text Label 10150 4450 2    60   ~ 0
CLK
NoConn ~ 10950 4850
NoConn ~ 10950 4750
NoConn ~ 10950 4650
NoConn ~ 10950 4550
NoConn ~ 10950 4450
NoConn ~ 10950 4350
NoConn ~ 10950 4250
NoConn ~ 10950 4150
NoConn ~ 10950 4050
NoConn ~ 10950 3950
NoConn ~ 10950 3850
NoConn ~ 10950 3750
NoConn ~ 10950 3650
NoConn ~ 10950 3550
NoConn ~ 10950 3450
NoConn ~ 10950 3350
NoConn ~ 10950 3250
NoConn ~ 10450 3750
NoConn ~ 10450 2950
NoConn ~ 10950 3150
NoConn ~ 10450 4250
NoConn ~ 10450 4350
$Comp
L R R9
U 1 1 5B481FBA
P 3350 1050
F 0 "R9" V 3430 1050 50  0000 C CNN
F 1 "10" V 3350 1050 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3280 1050 50  0001 C CNN
F 3 "" H 3350 1050 50  0001 C CNN
	1    3350 1050
	0    -1   1    0   
$EndComp
$Comp
L R R5
U 1 1 5B48205D
P 3650 1150
F 0 "R5" V 3730 1150 50  0000 C CNN
F 1 "10" V 3650 1150 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3580 1150 50  0001 C CNN
F 3 "" H 3650 1150 50  0001 C CNN
	1    3650 1150
	0    -1   1    0   
$EndComp
$Comp
L R R1
U 1 1 5B482090
P 4000 1250
F 0 "R1" V 4080 1250 50  0000 C CNN
F 1 "470" V 4000 1250 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 3930 1250 50  0001 C CNN
F 3 "" H 4000 1250 50  0001 C CNN
	1    4000 1250
	0    -1   1    0   
$EndComp
$Comp
L R R10
U 1 1 5B4820BB
P 3400 2000
F 0 "R10" V 3480 2000 50  0000 C CNN
F 1 "10" V 3400 2000 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3330 2000 50  0001 C CNN
F 3 "" H 3400 2000 50  0001 C CNN
	1    3400 2000
	0    -1   1    0   
$EndComp
$Comp
L R R6
U 1 1 5B4820F5
P 3700 2100
F 0 "R6" V 3780 2100 50  0000 C CNN
F 1 "10" V 3700 2100 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3630 2100 50  0001 C CNN
F 3 "" H 3700 2100 50  0001 C CNN
	1    3700 2100
	0    -1   1    0   
$EndComp
$Comp
L R R2
U 1 1 5B482126
P 4000 2200
F 0 "R2" V 4080 2200 50  0000 C CNN
F 1 "470" V 4000 2200 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 3930 2200 50  0001 C CNN
F 3 "" H 4000 2200 50  0001 C CNN
	1    4000 2200
	0    -1   1    0   
$EndComp
$Comp
L D_Zener D1
U 1 1 5B4821E8
P 4900 1450
F 0 "D1" H 4900 1550 50  0000 C CNN
F 1 "D_Zener_3.3V" H 4900 1350 50  0000 C CNN
F 2 "Diodes_SMD:D_SOD-323_HandSoldering" H 4900 1450 50  0001 C CNN
F 3 "" H 4900 1450 50  0001 C CNN
	1    4900 1450
	0    -1   1    0   
$EndComp
$Comp
L D_Zener D5
U 1 1 5B482275
P 4650 1450
F 0 "D5" H 4650 1550 50  0000 C CNN
F 1 "D_Zener_3.3V" H 4650 1350 50  0000 C CNN
F 2 "Diodes_SMD:D_SOD-323_HandSoldering" H 4650 1450 50  0001 C CNN
F 3 "" H 4650 1450 50  0001 C CNN
	1    4650 1450
	0    -1   1    0   
$EndComp
$Comp
L D_Zener D9
U 1 1 5B48230A
P 11100 3150
F 0 "D9" H 11100 3250 50  0000 C CNN
F 1 "D_Zener_5V" H 11100 3050 50  0000 C CNN
F 2 "Diodes_SMD:D_SOD-323_HandSoldering" H 11100 3150 50  0001 C CNN
F 3 "" H 11100 3150 50  0001 C CNN
	1    11100 3150
	0    -1   1    0   
$EndComp
$Comp
L C C5
U 1 1 5B482357
P 3000 1450
F 0 "C5" H 3025 1550 50  0000 L CNN
F 1 "470pF" H 3025 1350 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 3038 1300 50  0001 C CNN
F 3 "" H 3000 1450 50  0001 C CNN
	1    3000 1450
	-1   0    0    -1  
$EndComp
$Comp
L C C1
U 1 1 5B482411
P 3250 1450
F 0 "C1" H 3275 1550 50  0000 L CNN
F 1 "470pF" H 3275 1350 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 3288 1300 50  0001 C CNN
F 3 "" H 3250 1450 50  0001 C CNN
	1    3250 1450
	-1   0    0    -1  
$EndComp
Wire Wire Line
	1900 2000 3250 2000
Wire Wire Line
	1900 2100 3550 2100
Wire Wire Line
	1900 3050 3250 3050
Wire Wire Line
	1900 3150 3550 3150
Wire Wire Line
	10450 4450 10150 4450
Wire Wire Line
	2050 3350 1900 3350
Wire Wire Line
	1900 1050 3200 1050
Wire Wire Line
	3500 1050 7350 1050
Wire Wire Line
	3800 1150 5450 1150
Wire Wire Line
	1900 1150 3500 1150
Wire Wire Line
	3000 1300 3000 1050
Connection ~ 3000 1050
Wire Wire Line
	3250 1300 3250 1150
Connection ~ 3250 1150
Wire Wire Line
	4650 1300 4650 1150
Connection ~ 4650 1150
Wire Wire Line
	4900 1600 4900 1700
Wire Wire Line
	4650 1600 4650 1700
Connection ~ 4650 1700
Wire Wire Line
	1900 1250 3850 1250
Wire Wire Line
	4150 1250 5100 1250
Wire Wire Line
	4900 1300 4900 1250
Connection ~ 4900 1250
Wire Wire Line
	3250 1650 3250 1600
Wire Wire Line
	3000 1650 3250 1650
Wire Wire Line
	3000 1650 3000 1600
$Comp
L GND #PWR07
U 1 1 5B482984
P 4650 1700
F 0 "#PWR07" H 4650 1450 50  0001 C CNN
F 1 "GND" H 4650 1550 50  0000 C CNN
F 2 "" H 4650 1700 50  0001 C CNN
F 3 "" H 4650 1700 50  0001 C CNN
	1    4650 1700
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR08
U 1 1 5B4829BF
P 3100 1700
F 0 "#PWR08" H 3100 1450 50  0001 C CNN
F 1 "GND" H 3100 1550 50  0000 C CNN
F 2 "" H 3100 1700 50  0001 C CNN
F 3 "" H 3100 1700 50  0001 C CNN
	1    3100 1700
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3100 1700 3100 1650
Connection ~ 3100 1650
$Comp
L D_Zener D6
U 1 1 5B483622
P 4650 2400
F 0 "D6" H 4650 2500 50  0000 C CNN
F 1 "D_Zener_3.3V" H 4650 2300 50  0000 C CNN
F 2 "Diodes_SMD:D_SOD-323_HandSoldering" H 4650 2400 50  0001 C CNN
F 3 "" H 4650 2400 50  0001 C CNN
	1    4650 2400
	0    -1   1    0   
$EndComp
$Comp
L D_Zener D10
U 1 1 5B483628
P 4350 2400
F 0 "D10" H 4350 2500 50  0000 C CNN
F 1 "D_Zener_3.3V" H 4350 2300 50  0000 C CNN
F 2 "Diodes_SMD:D_SOD-323_HandSoldering" H 4350 2400 50  0001 C CNN
F 3 "" H 4350 2400 50  0001 C CNN
	1    4350 2400
	0    -1   1    0   
$EndComp
Wire Wire Line
	4650 2550 4650 2650
Wire Wire Line
	4350 2650 4350 2550
$Comp
L GND #PWR09
U 1 1 5B483635
P 4650 2650
F 0 "#PWR09" H 4650 2400 50  0001 C CNN
F 1 "GND" H 4650 2500 50  0000 C CNN
F 2 "" H 4650 2650 50  0001 C CNN
F 3 "" H 4650 2650 50  0001 C CNN
	1    4650 2650
	-1   0    0    -1  
$EndComp
$Comp
L D_Zener D7
U 1 1 5B483732
P 4650 3450
F 0 "D7" H 4650 3550 50  0000 C CNN
F 1 "D_Zener_3.3V" H 4650 3350 50  0000 C CNN
F 2 "Diodes_SMD:D_SOD-323_HandSoldering" H 4650 3450 50  0001 C CNN
F 3 "" H 4650 3450 50  0001 C CNN
	1    4650 3450
	0    -1   1    0   
$EndComp
$Comp
L D_Zener D11
U 1 1 5B483738
P 4400 3450
F 0 "D11" H 4400 3550 50  0000 C CNN
F 1 "D_Zener_3.3V" H 4400 3350 50  0000 C CNN
F 2 "Diodes_SMD:D_SOD-323_HandSoldering" H 4400 3450 50  0001 C CNN
F 3 "" H 4400 3450 50  0001 C CNN
	1    4400 3450
	0    -1   1    0   
$EndComp
Wire Wire Line
	4400 3700 4650 3700
Wire Wire Line
	4650 3700 4650 3600
Connection ~ 4650 3700
Wire Wire Line
	4400 3700 4400 3600
$Comp
L GND #PWR010
U 1 1 5B483745
P 4650 3700
F 0 "#PWR010" H 4650 3450 50  0001 C CNN
F 1 "GND" H 4650 3550 50  0000 C CNN
F 2 "" H 4650 3700 50  0001 C CNN
F 3 "" H 4650 3700 50  0001 C CNN
	1    4650 3700
	-1   0    0    -1  
$EndComp
$Comp
L D_Zener D8
U 1 1 5B4837F0
P 4650 4400
F 0 "D8" H 4650 4500 50  0000 C CNN
F 1 "D_Zener_3.3V" H 4650 4300 50  0000 C CNN
F 2 "Diodes_SMD:D_SOD-323_HandSoldering" H 4650 4400 50  0001 C CNN
F 3 "" H 4650 4400 50  0001 C CNN
	1    4650 4400
	0    -1   1    0   
$EndComp
$Comp
L D_Zener D12
U 1 1 5B4837F6
P 4400 4400
F 0 "D12" H 4400 4500 50  0000 C CNN
F 1 "D_Zener_3.3V" H 4400 4300 50  0000 C CNN
F 2 "Diodes_SMD:D_SOD-323_HandSoldering" H 4400 4400 50  0001 C CNN
F 3 "" H 4400 4400 50  0001 C CNN
	1    4400 4400
	0    -1   1    0   
$EndComp
Wire Wire Line
	4400 4650 4650 4650
Wire Wire Line
	4650 4550 4650 4700
Connection ~ 4650 4650
Wire Wire Line
	4400 4650 4400 4550
$Comp
L GND #PWR011
U 1 1 5B483803
P 4650 4700
F 0 "#PWR011" H 4650 4450 50  0001 C CNN
F 1 "GND" H 4650 4550 50  0000 C CNN
F 2 "" H 4650 4700 50  0001 C CNN
F 3 "" H 4650 4700 50  0001 C CNN
	1    4650 4700
	-1   0    0    -1  
$EndComp
$Comp
L C C6
U 1 1 5B483DC0
P 3000 2400
F 0 "C6" H 3025 2500 50  0000 L CNN
F 1 "470pF" H 3025 2300 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 3038 2250 50  0001 C CNN
F 3 "" H 3000 2400 50  0001 C CNN
	1    3000 2400
	-1   0    0    -1  
$EndComp
$Comp
L C C2
U 1 1 5B483DC6
P 3250 2400
F 0 "C2" H 3275 2500 50  0000 L CNN
F 1 "470pF" H 3275 2300 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 3288 2250 50  0001 C CNN
F 3 "" H 3250 2400 50  0001 C CNN
	1    3250 2400
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3000 2250 3000 2000
Wire Wire Line
	3250 2100 3250 2250
Wire Wire Line
	3250 2600 3250 2550
Wire Wire Line
	3000 2600 3250 2600
Wire Wire Line
	3000 2600 3000 2550
$Comp
L GND #PWR012
U 1 1 5B483DD2
P 3100 2650
F 0 "#PWR012" H 3100 2400 50  0001 C CNN
F 1 "GND" H 3100 2500 50  0000 C CNN
F 2 "" H 3100 2650 50  0001 C CNN
F 3 "" H 3100 2650 50  0001 C CNN
	1    3100 2650
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3100 2650 3100 2600
Connection ~ 3100 2600
$Comp
L C C7
U 1 1 5B4840B1
P 3000 3450
F 0 "C7" H 3025 3550 50  0000 L CNN
F 1 "470pF" H 3025 3350 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 3038 3300 50  0001 C CNN
F 3 "" H 3000 3450 50  0001 C CNN
	1    3000 3450
	-1   0    0    -1  
$EndComp
$Comp
L C C3
U 1 1 5B4840B7
P 3250 3450
F 0 "C3" H 3275 3550 50  0000 L CNN
F 1 "470pF" H 3275 3350 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 3288 3300 50  0001 C CNN
F 3 "" H 3250 3450 50  0001 C CNN
	1    3250 3450
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3000 3300 3000 3050
Wire Wire Line
	3250 3150 3250 3300
Wire Wire Line
	3250 3650 3250 3600
Wire Wire Line
	3000 3650 3250 3650
Wire Wire Line
	3000 3650 3000 3600
$Comp
L GND #PWR013
U 1 1 5B4840C3
P 3100 3700
F 0 "#PWR013" H 3100 3450 50  0001 C CNN
F 1 "GND" H 3100 3550 50  0000 C CNN
F 2 "" H 3100 3700 50  0001 C CNN
F 3 "" H 3100 3700 50  0001 C CNN
	1    3100 3700
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3100 3700 3100 3650
Connection ~ 3100 3650
$Comp
L C C8
U 1 1 5B484431
P 3000 4400
F 0 "C8" H 3025 4500 50  0000 L CNN
F 1 "470pF" H 3025 4300 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 3038 4250 50  0001 C CNN
F 3 "" H 3000 4400 50  0001 C CNN
	1    3000 4400
	-1   0    0    -1  
$EndComp
$Comp
L C C4
U 1 1 5B484437
P 3250 4400
F 0 "C4" H 3275 4500 50  0000 L CNN
F 1 "470pF" H 3275 4300 50  0000 L CNN
F 2 "Capacitors_SMD:C_0805_HandSoldering" H 3288 4250 50  0001 C CNN
F 3 "" H 3250 4400 50  0001 C CNN
	1    3250 4400
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3250 4600 3250 4550
Wire Wire Line
	3000 4600 3250 4600
Wire Wire Line
	3000 4600 3000 4550
$Comp
L GND #PWR014
U 1 1 5B484441
P 3100 4650
F 0 "#PWR014" H 3100 4400 50  0001 C CNN
F 1 "GND" H 3100 4500 50  0000 C CNN
F 2 "" H 3100 4650 50  0001 C CNN
F 3 "" H 3100 4650 50  0001 C CNN
	1    3100 4650
	-1   0    0    -1  
$EndComp
Wire Wire Line
	3100 4650 3100 4600
Connection ~ 3100 4600
Connection ~ 3000 2000
Wire Wire Line
	3550 2000 6800 2000
Wire Wire Line
	3850 2100 5250 2100
Wire Wire Line
	3850 2200 1900 2200
Connection ~ 3250 2100
Wire Wire Line
	4650 2250 4650 2100
Connection ~ 4650 2100
$Comp
L R R11
U 1 1 5B485092
P 3400 3050
F 0 "R11" V 3480 3050 50  0000 C CNN
F 1 "10" V 3400 3050 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3330 3050 50  0001 C CNN
F 3 "" H 3400 3050 50  0001 C CNN
	1    3400 3050
	0    -1   1    0   
$EndComp
$Comp
L R R7
U 1 1 5B485098
P 3700 3150
F 0 "R7" V 3780 3150 50  0000 C CNN
F 1 "10" V 3700 3150 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3630 3150 50  0001 C CNN
F 3 "" H 3700 3150 50  0001 C CNN
	1    3700 3150
	0    -1   1    0   
$EndComp
$Comp
L R R3
U 1 1 5B48509E
P 4000 3250
F 0 "R3" V 4080 3250 50  0000 C CNN
F 1 "470" V 4000 3250 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 3930 3250 50  0001 C CNN
F 3 "" H 4000 3250 50  0001 C CNN
	1    4000 3250
	0    -1   1    0   
$EndComp
Wire Wire Line
	3550 3050 6400 3050
Wire Wire Line
	3850 3150 5400 3150
$Comp
L R R12
U 1 1 5B48515F
P 3400 4000
F 0 "R12" V 3480 4000 50  0000 C CNN
F 1 "10" V 3400 4000 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3330 4000 50  0001 C CNN
F 3 "" H 3400 4000 50  0001 C CNN
	1    3400 4000
	0    -1   1    0   
$EndComp
$Comp
L R R8
U 1 1 5B485165
P 3700 4100
F 0 "R8" V 3780 4100 50  0000 C CNN
F 1 "10" V 3700 4100 50  0000 C CNN
F 2 "Resistors_SMD:R_0805_HandSoldering" V 3630 4100 50  0001 C CNN
F 3 "" H 3700 4100 50  0001 C CNN
	1    3700 4100
	0    -1   1    0   
$EndComp
$Comp
L R R4
U 1 1 5B48516B
P 4000 4200
F 0 "R4" V 4080 4200 50  0000 C CNN
F 1 "470" V 4000 4200 50  0000 C CNN
F 2 "Resistors_SMD:R_1206_HandSoldering" V 3930 4200 50  0001 C CNN
F 3 "" H 4000 4200 50  0001 C CNN
	1    4000 4200
	0    -1   1    0   
$EndComp
Wire Wire Line
	1900 4100 3550 4100
Wire Wire Line
	3550 4000 5950 4000
Wire Wire Line
	3850 4100 5350 4100
Connection ~ 3000 3050
Wire Wire Line
	1900 3250 3850 3250
Wire Wire Line
	4150 3250 5050 3250
Wire Wire Line
	4650 3300 4650 3150
Connection ~ 4650 3150
Connection ~ 3250 3150
Wire Wire Line
	1900 4000 3250 4000
Wire Wire Line
	1900 4200 3850 4200
Wire Wire Line
	3000 4250 3000 4000
Connection ~ 3000 4000
Wire Wire Line
	3250 4250 3250 4100
Connection ~ 3250 4100
Wire Wire Line
	4150 4200 5050 4200
Wire Wire Line
	4650 4250 4650 4100
Connection ~ 4650 4100
$Comp
L GND #PWR015
U 1 1 5B4F3E4D
P 10050 3350
F 0 "#PWR015" H 10050 3100 50  0001 C CNN
F 1 "GND" H 10050 3200 50  0000 C CNN
F 2 "" H 10050 3350 50  0001 C CNN
F 3 "" H 10050 3350 50  0001 C CNN
	1    10050 3350
	-1   0    0    -1  
$EndComp
NoConn ~ 10450 4550
$Comp
L C C10
U 1 1 5B5A4A2E
P 8650 800
F 0 "C10" H 8675 900 50  0000 L CNN
F 1 "10nF" H 8675 700 50  0000 L CNN
F 2 "Capacitors_SMD:C_1206_HandSoldering" H 8688 650 50  0001 C CNN
F 3 "" H 8650 800 50  0001 C CNN
	1    8650 800 
	-1   0    0    -1  
$EndComp
$Comp
L 74LV1T34 U1
U 1 1 5B5B2161
P 7750 1050
F 0 "U1" H 7450 1400 60  0000 C CNN
F 1 "74LV1T34" H 7850 1350 60  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-23-5_HandSoldering" H 7750 1050 60  0001 C CNN
F 3 "" H 7750 1050 60  0001 C CNN
	1    7750 1050
	-1   0    0    -1  
$EndComp
Wire Wire Line
	10050 3350 10450 3350
$Comp
L GND #PWR016
U 1 1 5B5B2FBE
P 7900 1350
F 0 "#PWR016" H 7900 1100 50  0001 C CNN
F 1 "GND" H 7900 1200 50  0000 C CNN
F 2 "" H 7900 1350 50  0001 C CNN
F 3 "" H 7900 1350 50  0001 C CNN
	1    7900 1350
	-1   0    0    -1  
$EndComp
Connection ~ 11100 2950
Wire Wire Line
	8450 950  8300 950 
Wire Wire Line
	7900 650  8650 650 
$Comp
L 74LV1T34 U4
U 1 1 5B5B4D01
P 7200 2000
F 0 "U4" H 6900 2350 60  0000 C CNN
F 1 "74LV1T34" H 7300 2300 60  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-23-5_HandSoldering" H 7200 2000 60  0001 C CNN
F 3 "" H 7200 2000 60  0001 C CNN
	1    7200 2000
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR017
U 1 1 5B5B504D
P 7700 2950
F 0 "#PWR017" H 7700 2700 50  0001 C CNN
F 1 "GND" H 7700 2800 50  0000 C CNN
F 2 "" H 7700 2950 50  0001 C CNN
F 3 "" H 7700 2950 50  0001 C CNN
	1    7700 2950
	-1   0    0    -1  
$EndComp
Wire Wire Line
	7950 1900 7750 1900
Wire Wire Line
	7350 1600 8200 1600
$Comp
L 74LV1T34 U3
U 1 1 5B5B58F6
P 6800 3050
F 0 "U3" H 6500 3400 60  0000 C CNN
F 1 "74LV1T34" H 6900 3350 60  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-23-5_HandSoldering" H 6800 3050 60  0001 C CNN
F 3 "" H 6800 3050 60  0001 C CNN
	1    6800 3050
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR018
U 1 1 5B5B5C56
P 6950 3350
F 0 "#PWR018" H 6950 3100 50  0001 C CNN
F 1 "GND" H 6950 3200 50  0000 C CNN
F 2 "" H 6950 3350 50  0001 C CNN
F 3 "" H 6950 3350 50  0001 C CNN
	1    6950 3350
	-1   0    0    -1  
$EndComp
Text Label 7450 2950 2    60   ~ 0
CLK
Wire Wire Line
	7450 2950 7350 2950
$Comp
L 74LV1T34 U2
U 1 1 5B5B67A4
P 6350 4000
F 0 "U2" H 6050 4350 60  0000 C CNN
F 1 "74LV1T34" H 6450 4300 60  0000 C CNN
F 2 "TO_SOT_Packages_SMD:SOT-23-5_HandSoldering" H 6350 4000 60  0001 C CNN
F 3 "" H 6350 4000 60  0001 C CNN
	1    6350 4000
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR019
U 1 1 5B5B6841
P 6500 4300
F 0 "#PWR019" H 6500 4050 50  0001 C CNN
F 1 "GND" H 6500 4150 50  0000 C CNN
F 2 "" H 6500 4300 50  0001 C CNN
F 3 "" H 6500 4300 50  0001 C CNN
	1    6500 4300
	-1   0    0    -1  
$EndComp
Text Label 7050 3900 2    60   ~ 0
CLK
Wire Wire Line
	7050 3900 6900 3900
$Comp
L +5V #PWR020
U 1 1 5B5B7071
P 10600 700
F 0 "#PWR020" H 10600 550 50  0001 C CNN
F 1 "+5V" H 10600 840 50  0000 C CNN
F 2 "" H 10600 700 50  0001 C CNN
F 3 "" H 10600 700 50  0001 C CNN
	1    10600 700 
	-1   0    0    -1  
$EndComp
$Comp
L PWR_FLAG #FLG021
U 1 1 5B5B7245
P 10600 700
F 0 "#FLG021" H 10600 775 50  0001 C CNN
F 1 "PWR_FLAG" H 10600 850 50  0000 C CNN
F 2 "" H 10600 700 50  0001 C CNN
F 3 "" H 10600 700 50  0001 C CNN
	1    10600 700 
	1    0    0    1   
$EndComp
$Comp
L +5V #PWR022
U 1 1 5B5B749D
P 11100 2950
F 0 "#PWR022" H 11100 2800 50  0001 C CNN
F 1 "+5V" H 11100 3090 50  0000 C CNN
F 2 "" H 11100 2950 50  0001 C CNN
F 3 "" H 11100 2950 50  0001 C CNN
	1    11100 2950
	-1   0    0    -1  
$EndComp
$Comp
L +5V #PWR023
U 1 1 5B5B7589
P 7900 650
F 0 "#PWR023" H 7900 500 50  0001 C CNN
F 1 "+5V" H 7900 790 50  0000 C CNN
F 2 "" H 7900 650 50  0001 C CNN
F 3 "" H 7900 650 50  0001 C CNN
	1    7900 650 
	-1   0    0    -1  
$EndComp
$Comp
L +5V #PWR024
U 1 1 5B5B7675
P 7350 1600
F 0 "#PWR024" H 7350 1450 50  0001 C CNN
F 1 "+5V" H 7350 1740 50  0000 C CNN
F 2 "" H 7350 1600 50  0001 C CNN
F 3 "" H 7350 1600 50  0001 C CNN
	1    7350 1600
	-1   0    0    -1  
$EndComp
$Comp
L +5V #PWR025
U 1 1 5B5B7A06
P 6950 2650
F 0 "#PWR025" H 6950 2500 50  0001 C CNN
F 1 "+5V" H 6950 2790 50  0000 C CNN
F 2 "" H 6950 2650 50  0001 C CNN
F 3 "" H 6950 2650 50  0001 C CNN
	1    6950 2650
	-1   0    0    -1  
$EndComp
$Comp
L +5V #PWR026
U 1 1 5B5B7C04
P 6500 3600
F 0 "#PWR026" H 6500 3450 50  0001 C CNN
F 1 "+5V" H 6500 3740 50  0000 C CNN
F 2 "" H 6500 3600 50  0001 C CNN
F 3 "" H 6500 3600 50  0001 C CNN
	1    6500 3600
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR027
U 1 1 5B5B470D
P 8650 950
F 0 "#PWR027" H 8650 700 50  0001 C CNN
F 1 "GND" H 8650 800 50  0000 C CNN
F 2 "" H 8650 950 50  0001 C CNN
F 3 "" H 8650 950 50  0001 C CNN
	1    8650 950 
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR028
U 1 1 5B5B48CC
P 11100 3400
F 0 "#PWR028" H 11100 3150 50  0001 C CNN
F 1 "GND" H 11100 3250 50  0000 C CNN
F 2 "" H 11100 3400 50  0001 C CNN
F 3 "" H 11100 3400 50  0001 C CNN
	1    11100 3400
	-1   0    0    -1  
$EndComp
Wire Wire Line
	10950 2950 11100 2950
Wire Wire Line
	4650 1700 4900 1700
Wire Wire Line
	11100 3400 11100 3300
Wire Wire Line
	11100 2950 11100 3000
Wire Wire Line
	10950 3050 10950 2950
Text Label 5100 1250 0    60   ~ 0
J1_Data
Wire Wire Line
	10450 3050 10200 3050
Wire Wire Line
	10450 3150 10050 3150
Text Label 10050 3250 0    60   ~ 0
J1_Data
Text Label 10050 3150 0    60   ~ 0
J1_LOAD
Text Label 4900 2200 0    60   ~ 0
J2_Data
$Comp
L C C12
U 1 1 5B5BC07F
P 8200 1750
F 0 "C12" H 8225 1850 50  0000 L CNN
F 1 "10nF" H 8225 1650 50  0000 L CNN
F 2 "Capacitors_SMD:C_1206_HandSoldering" H 8238 1600 50  0001 C CNN
F 3 "" H 8200 1750 50  0001 C CNN
	1    8200 1750
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR029
U 1 1 5B5BC142
P 8200 1900
F 0 "#PWR029" H 8200 1650 50  0001 C CNN
F 1 "GND" H 8200 1750 50  0000 C CNN
F 2 "" H 8200 1900 50  0001 C CNN
F 3 "" H 8200 1900 50  0001 C CNN
	1    8200 1900
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR030
U 1 1 5B5BC487
P 7350 2300
F 0 "#PWR030" H 7350 2050 50  0001 C CNN
F 1 "GND" H 7350 2150 50  0000 C CNN
F 2 "" H 7350 2300 50  0001 C CNN
F 3 "" H 7350 2300 50  0001 C CNN
	1    7350 2300
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4150 2200 4900 2200
Wire Wire Line
	4650 2650 4350 2650
$Comp
L C C11
U 1 1 5B5BD26E
P 7700 2800
F 0 "C11" H 7725 2900 50  0000 L CNN
F 1 "10nF" H 7725 2700 50  0000 L CNN
F 2 "Capacitors_SMD:C_1206_HandSoldering" H 7738 2650 50  0001 C CNN
F 3 "" H 7700 2800 50  0001 C CNN
	1    7700 2800
	-1   0    0    -1  
$EndComp
Wire Wire Line
	6950 2650 7700 2650
Text Label 5050 3250 0    60   ~ 0
J3_Data
$Comp
L C C9
U 1 1 5B5BE924
P 7300 3750
F 0 "C9" H 7325 3850 50  0000 L CNN
F 1 "10nF" H 7325 3650 50  0000 L CNN
F 2 "Capacitors_SMD:C_1206_HandSoldering" H 7338 3600 50  0001 C CNN
F 3 "" H 7300 3750 50  0001 C CNN
	1    7300 3750
	-1   0    0    -1  
$EndComp
$Comp
L GND #PWR031
U 1 1 5B5BEABF
P 7300 3900
F 0 "#PWR031" H 7300 3650 50  0001 C CNN
F 1 "GND" H 7300 3750 50  0000 C CNN
F 2 "" H 7300 3900 50  0001 C CNN
F 3 "" H 7300 3900 50  0001 C CNN
	1    7300 3900
	-1   0    0    -1  
$EndComp
Wire Wire Line
	6500 3600 7300 3600
Text Label 5050 4200 0    60   ~ 0
C_Data
Wire Wire Line
	10450 3450 10300 3450
Wire Wire Line
	10450 3550 10100 3550
Text Label 10100 3650 0    60   ~ 0
J2_Data
Text Label 10100 3550 0    60   ~ 0
J2_LOAD
Wire Wire Line
	10450 3850 9950 3850
Wire Wire Line
	10450 3950 9950 3950
Text Label 9950 4050 0    60   ~ 0
J3_Data
Text Label 9950 3950 0    60   ~ 0
J3_LOAD
Wire Wire Line
	10450 4750 10000 4750
Wire Wire Line
	10450 4650 10000 4650
Text Label 10000 4750 0    60   ~ 0
C_Data
Text Label 10000 4650 0    60   ~ 0
C_LOAD
$Comp
L GND #PWR032
U 1 1 5B5C0EF8
P 10450 4850
F 0 "#PWR032" H 10450 4600 50  0001 C CNN
F 1 "GND" H 10450 4700 50  0000 C CNN
F 2 "" H 10450 4850 50  0001 C CNN
F 3 "" H 10450 4850 50  0001 C CNN
	1    10450 4850
	-1   0    0    -1  
$EndComp
Wire Wire Line
	10450 3250 10050 3250
Text Label 10200 3050 2    60   ~ 0
CLK
Wire Wire Line
	10450 3650 10100 3650
Text Label 10300 3450 2    60   ~ 0
CLK
Text Label 9950 3850 2    60   ~ 0
CLK
Wire Wire Line
	10450 4050 9950 4050
Wire Wire Line
	4350 2250 4350 2200
Connection ~ 4350 2200
Wire Wire Line
	4400 3300 4400 3250
Connection ~ 4400 3250
Wire Wire Line
	4400 4250 4400 4200
Connection ~ 4400 4200
$Comp
L GND #PWR033
U 1 1 5B5B9833
P 10450 4150
F 0 "#PWR033" H 10450 3900 50  0001 C CNN
F 1 "GND" H 10450 4000 50  0000 C CNN
F 2 "" H 10450 4150 50  0001 C CNN
F 3 "" H 10450 4150 50  0001 C CNN
	1    10450 4150
	-1   0    0    -1  
$EndComp
$EndSCHEMATC
