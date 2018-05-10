EESchema Schematic File Version 2
LIBS:JudgeBoard-rescue
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
LIBS:Switch
LIBS:Logic_74xx
LIBS:Logic_CMOS_4000
LIBS:Logic_CMOS_IEEE
LIBS:JudgeBoard-cache
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
L GND #PWR01
U 1 1 5AEBDB86
P 650 2050
F 0 "#PWR01" H 650 1800 50  0001 C CNN
F 1 "GND" H 650 1900 50  0000 C CNN
F 2 "" H 650 2050 50  0001 C CNN
F 3 "" H 650 2050 50  0001 C CNN
	1    650  2050
	1    0    0    -1  
$EndComp
Wire Wire Line
	750  2050 650  2050
$Comp
L +3.3V #PWR02
U 1 1 5AEBE39C
P 4000 1450
F 0 "#PWR02" H 4000 1300 50  0001 C CNN
F 1 "+3.3V" H 4000 1590 50  0000 C CNN
F 2 "" H 4000 1450 50  0001 C CNN
F 3 "" H 4000 1450 50  0001 C CNN
	1    4000 1450
	1    0    0    -1  
$EndComp
Wire Wire Line
	1850 1950 6100 1950
Wire Wire Line
	4000 1950 4000 1850
Wire Wire Line
	3250 2250 5000 2250
Wire Wire Line
	4100 2250 4100 1850
Wire Wire Line
	1850 3000 5100 3000
Wire Wire Line
	4200 3000 4200 1850
Wire Wire Line
	3250 3300 5200 3300
Wire Wire Line
	1850 4000 5300 4000
Wire Wire Line
	4400 4000 4400 1850
Wire Wire Line
	3250 4300 5400 4300
Wire Wire Line
	4500 4300 4500 1850
Wire Wire Line
	1850 5050 5500 5050
Wire Wire Line
	4600 5050 4600 1850
Wire Wire Line
	3250 5350 5600 5350
Wire Wire Line
	4700 5350 4700 1850
Connection ~ 4000 1950
Wire Wire Line
	5000 2250 5000 2100
Wire Wire Line
	5000 2100 6100 2100
Connection ~ 4100 2250
Wire Wire Line
	5100 3000 5100 2250
Wire Wire Line
	5100 2250 6100 2250
Connection ~ 4200 3000
Wire Wire Line
	5200 3300 5200 2400
Wire Wire Line
	5200 2400 6100 2400
Connection ~ 4300 3300
Wire Wire Line
	5300 4000 5300 2550
Wire Wire Line
	5300 2550 6100 2550
Connection ~ 4400 4000
Wire Wire Line
	5400 4300 5400 2700
Wire Wire Line
	5400 2700 6100 2700
Connection ~ 4500 4300
Wire Wire Line
	5500 5050 5500 2850
Wire Wire Line
	5500 2850 6100 2850
Connection ~ 4600 5050
Wire Wire Line
	5600 5350 5600 3000
Wire Wire Line
	5600 3000 6100 3000
Connection ~ 4700 5350
$Comp
L 74HC165 U1
U 1 1 5AECD96E
P 6700 2450
F 0 "U1" H 6700 2800 60  0000 C CNN
F 1 "74HC165" H 6700 2450 60  0000 C CNN
F 2 "Housings_DIP:DIP-16_W7.62mm_LongPads" H 6700 2450 60  0001 C CNN
F 3 "" H 6700 2450 60  0001 C CNN
	1    6700 2450
	1    0    0    -1  
$EndComp
$Comp
L 74HC165 U2
U 1 1 5AECD9AB
P 7650 4850
F 0 "U2" H 7650 5200 60  0000 C CNN
F 1 "74HC165" H 7650 4850 60  0000 C CNN
F 2 "Housings_DIP:DIP-16_W7.62mm_LongPads" H 7650 4850 60  0001 C CNN
F 3 "" H 7650 4850 60  0001 C CNN
	1    7650 4850
	1    0    0    -1  
$EndComp
$Comp
L +3.3V #PWR03
U 1 1 5AECDC8D
P 7650 3650
F 0 "#PWR03" H 7650 3500 50  0001 C CNN
F 1 "+3.3V" H 7650 3790 50  0000 C CNN
F 2 "" H 7650 3650 50  0001 C CNN
F 3 "" H 7650 3650 50  0001 C CNN
	1    7650 3650
	1    0    0    -1  
$EndComp
$Comp
L +3.3V #PWR04
U 1 1 5AECDCC2
P 6700 1250
F 0 "#PWR04" H 6700 1100 50  0001 C CNN
F 1 "+3.3V" H 6700 1390 50  0000 C CNN
F 2 "" H 6700 1250 50  0001 C CNN
F 3 "" H 6700 1250 50  0001 C CNN
	1    6700 1250
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR05
U 1 1 5AECDCF7
P 6700 3450
F 0 "#PWR05" H 6700 3200 50  0001 C CNN
F 1 "GND" H 6700 3300 50  0000 C CNN
F 2 "" H 6700 3450 50  0001 C CNN
F 3 "" H 6700 3450 50  0001 C CNN
	1    6700 3450
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR06
U 1 1 5AECDDAA
P 7650 5850
F 0 "#PWR06" H 7650 5600 50  0001 C CNN
F 1 "GND" H 7650 5700 50  0000 C CNN
F 2 "" H 7650 5850 50  0001 C CNN
F 3 "" H 7650 5850 50  0001 C CNN
	1    7650 5850
	1    0    0    -1  
$EndComp
Wire Wire Line
	6700 3400 6100 3400
Wire Wire Line
	7050 5800 7650 5800
Wire Wire Line
	1850 6050 5800 6050
Connection ~ 7650 5800
Connection ~ 6700 3400
Wire Wire Line
	3250 6350 5950 6350
Wire Wire Line
	5950 6350 5950 4500
Wire Wire Line
	5950 4500 7050 4500
$Comp
L R_Network10 RN1
U 1 1 5AECE52B
P 4500 1650
F 0 "RN1" V 3900 1650 50  0000 C CNN
F 1 "R_Network10" V 5000 1650 50  0000 C CNN
F 2 "Resistors_THT:Resistor_Array_SIP11" V 5075 1650 50  0001 C CNN
F 3 "" H 4500 1650 50  0001 C CNN
	1    4500 1650
	1    0    0    -1  
$EndComp
Wire Wire Line
	4800 6050 4800 1850
Connection ~ 4800 6050
Wire Wire Line
	4900 1850 4900 6350
Connection ~ 4900 6350
Wire Wire Line
	4300 3300 4300 1850
Wire Wire Line
	7050 3900 6900 3900
Wire Wire Line
	6100 1500 5900 1500
$Comp
L +3.3V #PWR07
U 1 1 5AECEC2E
P 5350 1600
F 0 "#PWR07" H 5350 1450 50  0001 C CNN
F 1 "+3.3V" H 5350 1740 50  0000 C CNN
F 2 "" H 5350 1600 50  0001 C CNN
F 3 "" H 5350 1600 50  0001 C CNN
	1    5350 1600
	1    0    0    -1  
$EndComp
Wire Wire Line
	6100 1650 5350 1650
Wire Wire Line
	5350 1650 5350 1600
Wire Wire Line
	6100 1800 5900 1800
Wire Wire Line
	6650 4050 7050 4050
Wire Wire Line
	6650 3700 6650 4050
Wire Wire Line
	7050 4200 6850 4200
Connection ~ 7050 5550
Connection ~ 7050 5400
Connection ~ 7050 5100
Connection ~ 7050 4950
Connection ~ 7050 4800
Wire Wire Line
	7300 2400 7450 2400
Wire Wire Line
	7450 2400 7450 3700
Wire Wire Line
	7450 3700 6650 3700
Text Label 6900 3900 0    60   ~ 0
CLK
Text Label 6850 4200 0    60   ~ 0
LOAD
Text Label 5900 1500 0    60   ~ 0
CLK
Text Label 5900 1800 0    60   ~ 0
LOAD
$Comp
L RJ12-UNSHLD J1
U 1 1 5AED1621
P 10150 2250
F 0 "J1" H 10350 2750 50  0000 C CNN
F 1 "RJ12-UNSHLD" H 10000 2750 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x03_Pitch2.54mm" H 10150 2250 50  0001 C CNN
F 3 "" H 10150 2250 50  0001 C CNN
	1    10150 2250
	0    1    1    0   
$EndComp
$Comp
L +3.3V #PWR08
U 1 1 5AED16D2
P 9700 2050
F 0 "#PWR08" H 9700 1900 50  0001 C CNN
F 1 "+3.3V" H 9700 2190 50  0000 C CNN
F 2 "" H 9700 2050 50  0001 C CNN
F 3 "" H 9700 2050 50  0001 C CNN
	1    9700 2050
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR09
U 1 1 5AED1707
P 9700 2550
F 0 "#PWR09" H 9700 2300 50  0001 C CNN
F 1 "GND" H 9700 2400 50  0000 C CNN
F 2 "" H 9700 2550 50  0001 C CNN
F 3 "" H 9700 2550 50  0001 C CNN
	1    9700 2550
	1    0    0    -1  
$EndComp
Wire Wire Line
	9700 2150 9450 2150
Wire Wire Line
	9700 2250 9450 2250
Wire Wire Line
	8250 4800 8900 4800
Wire Wire Line
	8900 4800 8900 2350
Wire Wire Line
	8900 2350 9700 2350
Text Label 9450 2150 0    60   ~ 0
CLK
Text Label 9450 2250 0    60   ~ 0
LOAD
$Comp
L +3.3V #PWR010
U 1 1 5AED1A4E
P 750 750
F 0 "#PWR010" H 750 600 50  0001 C CNN
F 1 "+3.3V" H 750 890 50  0000 C CNN
F 2 "" H 750 750 50  0001 C CNN
F 3 "" H 750 750 50  0001 C CNN
	1    750  750 
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR011
U 1 1 5AED1A83
P 1050 900
F 0 "#PWR011" H 1050 650 50  0001 C CNN
F 1 "GND" H 1050 750 50  0000 C CNN
F 2 "" H 1050 900 50  0001 C CNN
F 3 "" H 1050 900 50  0001 C CNN
	1    1050 900 
	1    0    0    -1  
$EndComp
$Comp
L PWR_FLAG #FLG012
U 1 1 5AED1AC8
P 1050 900
F 0 "#FLG012" H 1050 975 50  0001 C CNN
F 1 "PWR_FLAG" H 1050 1050 50  0000 C CNN
F 2 "" H 1050 900 50  0001 C CNN
F 3 "" H 1050 900 50  0001 C CNN
	1    1050 900 
	1    0    0    -1  
$EndComp
$Comp
L PWR_FLAG #FLG013
U 1 1 5AED1B04
P 750 750
F 0 "#FLG013" H 750 825 50  0001 C CNN
F 1 "PWR_FLAG" H 750 900 50  0000 C CNN
F 2 "" H 750 750 50  0001 C CNN
F 3 "" H 750 750 50  0001 C CNN
	1    750  750 
	-1   0    0    1   
$EndComp
NoConn ~ 7300 2550
NoConn ~ 8250 4950
NoConn ~ 9700 2450
Wire Wire Line
	6100 3400 6100 3150
Wire Wire Line
	7050 4650 7050 5800
Connection ~ 7050 5250
Wire Wire Line
	6700 3450 6700 3400
Wire Wire Line
	7650 5800 7650 5850
$Comp
L C C1
U 1 1 5AECE346
P 7300 1400
F 0 "C1" H 7325 1500 50  0000 L CNN
F 1 "C" H 7325 1300 50  0000 L CNN
F 2 "Capacitors_THT:C_Disc_D3.4mm_W2.1mm_P2.50mm" H 7338 1250 50  0001 C CNN
F 3 "" H 7300 1400 50  0001 C CNN
	1    7300 1400
	1    0    0    -1  
$EndComp
$Comp
L C C2
U 1 1 5AECE390
P 8250 3800
F 0 "C2" H 8275 3900 50  0000 L CNN
F 1 "C" H 8275 3700 50  0000 L CNN
F 2 "Capacitors_THT:C_Disc_D3.4mm_W2.1mm_P2.50mm" H 8288 3650 50  0001 C CNN
F 3 "" H 8250 3800 50  0001 C CNN
	1    8250 3800
	1    0    0    -1  
$EndComp
Wire Wire Line
	6700 1250 7300 1250
$Comp
L GND #PWR014
U 1 1 5AECE986
P 7300 1550
F 0 "#PWR014" H 7300 1300 50  0001 C CNN
F 1 "GND" H 7300 1400 50  0000 C CNN
F 2 "" H 7300 1550 50  0001 C CNN
F 3 "" H 7300 1550 50  0001 C CNN
	1    7300 1550
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR015
U 1 1 5AECEA91
P 8250 3950
F 0 "#PWR015" H 8250 3700 50  0001 C CNN
F 1 "GND" H 8250 3800 50  0000 C CNN
F 2 "" H 8250 3950 50  0001 C CNN
F 3 "" H 8250 3950 50  0001 C CNN
	1    8250 3950
	1    0    0    -1  
$EndComp
Wire Wire Line
	7650 3650 8250 3650
Wire Wire Line
	9700 2050 8700 2050
Wire Wire Line
	8700 2050 8700 2250
$Comp
L CP1 C3
U 1 1 5AECEE1D
P 8700 2400
F 0 "C3" H 8725 2500 50  0000 L CNN
F 1 "CP1" H 8725 2300 50  0000 L CNN
F 2 "Capacitors_THT:CP_Axial_L11.0mm_D5.0mm_P18.00mm_Horizontal" H 8700 2400 50  0001 C CNN
F 3 "" H 8700 2400 50  0001 C CNN
	1    8700 2400
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR016
U 1 1 5AECEE74
P 8700 2550
F 0 "#PWR016" H 8700 2300 50  0001 C CNN
F 1 "GND" H 8700 2400 50  0000 C CNN
F 2 "" H 8700 2550 50  0001 C CNN
F 3 "" H 8700 2550 50  0001 C CNN
	1    8700 2550
	1    0    0    -1  
$EndComp
$Comp
L DPDT-Button S1
U 1 1 5AF3A7BC
P 1300 2200
F 0 "S1" H 1300 2650 60  0000 C CNN
F 1 "DPDT-Button" H 1300 2200 60  0000 C CNN
F 2 "Buttons_Switches_THT:MHPS2285V" H 1300 2200 60  0001 C CNN
F 3 "" H 1300 2200 60  0001 C CNN
	1    1300 2200
	1    0    0    -1  
$EndComp
$Comp
L DPDT-Button S6
U 1 1 5AF3AAFB
P 2700 2500
F 0 "S6" H 2700 2950 60  0000 C CNN
F 1 "DPDT-Button" H 2700 2500 60  0000 C CNN
F 2 "Buttons_Switches_THT:MHPS2285V" H 2700 2500 60  0001 C CNN
F 3 "" H 2700 2500 60  0001 C CNN
	1    2700 2500
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR017
U 1 1 5AF3AF90
P 2000 2350
F 0 "#PWR017" H 2000 2100 50  0001 C CNN
F 1 "GND" H 2000 2200 50  0000 C CNN
F 2 "" H 2000 2350 50  0001 C CNN
F 3 "" H 2000 2350 50  0001 C CNN
	1    2000 2350
	1    0    0    -1  
$EndComp
Wire Wire Line
	2000 2350 2150 2350
$Comp
L DPDT-Button S2
U 1 1 5AF3B1C2
P 1300 3250
F 0 "S2" H 1300 3700 60  0000 C CNN
F 1 "DPDT-Button" H 1300 3250 60  0000 C CNN
F 2 "Buttons_Switches_THT:MHPS2285V" H 1300 3250 60  0001 C CNN
F 3 "" H 1300 3250 60  0001 C CNN
	1    1300 3250
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR018
U 1 1 5AF3B202
P 600 3100
F 0 "#PWR018" H 600 2850 50  0001 C CNN
F 1 "GND" H 600 2950 50  0000 C CNN
F 2 "" H 600 3100 50  0001 C CNN
F 3 "" H 600 3100 50  0001 C CNN
	1    600  3100
	1    0    0    -1  
$EndComp
Wire Wire Line
	600  3100 750  3100
$Comp
L DPDT-Button S7
U 1 1 5AF3B375
P 2700 3550
F 0 "S7" H 2700 4000 60  0000 C CNN
F 1 "DPDT-Button" H 2700 3550 60  0000 C CNN
F 2 "Buttons_Switches_THT:MHPS2285V" H 2700 3550 60  0001 C CNN
F 3 "" H 2700 3550 60  0001 C CNN
	1    2700 3550
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR019
U 1 1 5AF3B3C9
P 2050 3400
F 0 "#PWR019" H 2050 3150 50  0001 C CNN
F 1 "GND" H 2050 3250 50  0000 C CNN
F 2 "" H 2050 3400 50  0001 C CNN
F 3 "" H 2050 3400 50  0001 C CNN
	1    2050 3400
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 3400 2150 3400
$Comp
L GND #PWR020
U 1 1 5AF3B694
P 650 4100
F 0 "#PWR020" H 650 3850 50  0001 C CNN
F 1 "GND" H 650 3950 50  0000 C CNN
F 2 "" H 650 4100 50  0001 C CNN
F 3 "" H 650 4100 50  0001 C CNN
	1    650  4100
	1    0    0    -1  
$EndComp
Wire Wire Line
	750  4100 650  4100
$Comp
L DPDT-Button S3
U 1 1 5AF3B69E
P 1300 4250
F 0 "S3" H 1300 4700 60  0000 C CNN
F 1 "DPDT-Button" H 1300 4250 60  0000 C CNN
F 2 "Buttons_Switches_THT:MHPS2285V" H 1300 4250 60  0001 C CNN
F 3 "" H 1300 4250 60  0001 C CNN
	1    1300 4250
	1    0    0    -1  
$EndComp
$Comp
L DPDT-Button S8
U 1 1 5AF3B6A4
P 2700 4550
F 0 "S8" H 2700 5000 60  0000 C CNN
F 1 "DPDT-Button" H 2700 4550 60  0000 C CNN
F 2 "Buttons_Switches_THT:MHPS2285V" H 2700 4550 60  0001 C CNN
F 3 "" H 2700 4550 60  0001 C CNN
	1    2700 4550
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR021
U 1 1 5AF3B6AA
P 2000 4400
F 0 "#PWR021" H 2000 4150 50  0001 C CNN
F 1 "GND" H 2000 4250 50  0000 C CNN
F 2 "" H 2000 4400 50  0001 C CNN
F 3 "" H 2000 4400 50  0001 C CNN
	1    2000 4400
	1    0    0    -1  
$EndComp
Wire Wire Line
	2000 4400 2150 4400
$Comp
L DPDT-Button S4
U 1 1 5AF3B6B1
P 1300 5300
F 0 "S4" H 1300 5750 60  0000 C CNN
F 1 "DPDT-Button" H 1300 5300 60  0000 C CNN
F 2 "Buttons_Switches_THT:MHPS2285V" H 1300 5300 60  0001 C CNN
F 3 "" H 1300 5300 60  0001 C CNN
	1    1300 5300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR022
U 1 1 5AF3B6B7
P 600 5150
F 0 "#PWR022" H 600 4900 50  0001 C CNN
F 1 "GND" H 600 5000 50  0000 C CNN
F 2 "" H 600 5150 50  0001 C CNN
F 3 "" H 600 5150 50  0001 C CNN
	1    600  5150
	1    0    0    -1  
$EndComp
Wire Wire Line
	600  5150 750  5150
$Comp
L DPDT-Button S9
U 1 1 5AF3B6C0
P 2700 5600
F 0 "S9" H 2700 6050 60  0000 C CNN
F 1 "DPDT-Button" H 2700 5600 60  0000 C CNN
F 2 "Buttons_Switches_THT:MHPS2285V" H 2700 5600 60  0001 C CNN
F 3 "" H 2700 5600 60  0001 C CNN
	1    2700 5600
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR023
U 1 1 5AF3B6C6
P 2050 5450
F 0 "#PWR023" H 2050 5200 50  0001 C CNN
F 1 "GND" H 2050 5300 50  0000 C CNN
F 2 "" H 2050 5450 50  0001 C CNN
F 3 "" H 2050 5450 50  0001 C CNN
	1    2050 5450
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 5450 2150 5450
Wire Wire Line
	3600 3300 3600 3300
Wire Wire Line
	3650 4000 3650 4000
Wire Wire Line
	3750 4300 3750 4300
Wire Wire Line
	3900 5350 3900 5350
$Comp
L DPDT-Button S5
U 1 1 5AF3BB10
P 1300 6300
F 0 "S5" H 1300 6750 60  0000 C CNN
F 1 "DPDT-Button" H 1300 6300 60  0000 C CNN
F 2 "Buttons_Switches_THT:MHPS2285V" H 1300 6300 60  0001 C CNN
F 3 "" H 1300 6300 60  0001 C CNN
	1    1300 6300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR024
U 1 1 5AF3BB16
P 600 6150
F 0 "#PWR024" H 600 5900 50  0001 C CNN
F 1 "GND" H 600 6000 50  0000 C CNN
F 2 "" H 600 6150 50  0001 C CNN
F 3 "" H 600 6150 50  0001 C CNN
	1    600  6150
	1    0    0    -1  
$EndComp
Wire Wire Line
	600  6150 750  6150
$Comp
L DPDT-Button S10
U 1 1 5AF3BB1F
P 2700 6600
F 0 "S10" H 2700 7050 60  0000 C CNN
F 1 "DPDT-Button" H 2700 6600 60  0000 C CNN
F 2 "Buttons_Switches_THT:MHPS2285V" H 2700 6600 60  0001 C CNN
F 3 "" H 2700 6600 60  0001 C CNN
	1    2700 6600
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR025
U 1 1 5AF3BB25
P 2050 6450
F 0 "#PWR025" H 2050 6200 50  0001 C CNN
F 1 "GND" H 2050 6300 50  0000 C CNN
F 2 "" H 2050 6450 50  0001 C CNN
F 3 "" H 2050 6450 50  0001 C CNN
	1    2050 6450
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 6450 2150 6450
Wire Wire Line
	4100 6050 4100 6050
Wire Wire Line
	4250 6350 4250 6350
Wire Wire Line
	5800 6050 5800 4350
Wire Wire Line
	5800 4350 7050 4350
NoConn ~ 750  1850
NoConn ~ 750  2300
NoConn ~ 750  2500
NoConn ~ 1850 2400
NoConn ~ 2150 2150
NoConn ~ 2150 2600
NoConn ~ 2150 2800
NoConn ~ 3250 2700
NoConn ~ 750  2900
NoConn ~ 750  3350
NoConn ~ 750  3550
NoConn ~ 1850 3450
NoConn ~ 2150 3200
NoConn ~ 2150 3650
NoConn ~ 2150 3850
NoConn ~ 3250 3750
NoConn ~ 750  3900
NoConn ~ 750  4350
NoConn ~ 750  4550
NoConn ~ 1850 4450
NoConn ~ 2150 4200
NoConn ~ 2150 4650
NoConn ~ 2150 4850
NoConn ~ 3250 4750
NoConn ~ 750  4950
NoConn ~ 750  5400
NoConn ~ 750  5600
NoConn ~ 1850 5500
NoConn ~ 2150 5250
NoConn ~ 2150 5700
NoConn ~ 2150 5900
NoConn ~ 3250 5800
NoConn ~ 750  5950
NoConn ~ 750  6400
NoConn ~ 750  6600
NoConn ~ 1850 6500
NoConn ~ 2150 6250
NoConn ~ 2150 6700
NoConn ~ 2150 6900
NoConn ~ 3250 6800
$EndSCHEMATC
