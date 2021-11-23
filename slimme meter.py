#!/usr/bin/env python
import re
import serial

ser = serial.Serial()
ser.baudrate = 115200
ser.bytesize=serial.EIGHTBITS
ser.parity=serial.PARITY_NONE
ser.stopbits=serial.STOPBITS_ONE
ser.xonxoff=0
ser.rtscts=0
ser.timeout=20
ser.port="/dev/ttyUSB0"
ser.close()
nr=0
try:
    ser.open()
except:
    sys.exit ("Fout bij het openen van %s."  % ser.name)
    
while nr < 26:
    regel = ser.readline() 
    regel = regel.decode('ascii').strip()
    if re.match(b'(?=1-0:1.8.1)', regel):
        nachtaf = regel[10:20] 
    if re.match(b'(?=1-0:1.8.2)', regel):
        dagaf = regel[10:20]
    if re.match(b'(?=1-0:2.8.1)', regel):
        nachtterug = regel[10:20]
    if re.match(b'(?=1-0:2.8.2)', regel):
        dagterug = regel[10:20]
    if re.match(b'(?=1-0:1.7.0)', regel): 
        af = int(float(regel[10:16])*1000)
    if re.match(b'(?=1-0:2.7.0)', regel): 
        terug = int(float(regel[10:16])*1000)
    if re.match(b'(?=1-0:32.7.0)', regel):
        volt = regel[11:14] 
    if re.match(b'(?=1-0:31.7.0)', regel):
        amp = regel[11:14]
    if re.match(b'(?=0-1:24.2.1)', regel):
        gas = regel[26:35] 
    nr = nr +1 

try:
    ser.close()
except:
    sys.exit ("%s. Programma afgebroken. Kon de seriele poort niet sluiten." % ser.name )  

def printen(nachtaf, dagaf, nachtterug, dagterug, af, terug, gas, volt, amp):
        print "daldag                     ", nachtaf, " kWh"
        print "piekdag                    ", dagaf, " kWh"
        print "dalterug                   ", nachtterug, " kWh"
        print "piekterug                  ", dagterug, " kWh"
        print "Afgenomen vermogen         ", af, " W"
        print "Teruggeleverd vermogen     ", terug, " W"
        print "Voltage                    ", volt, " V"
        print "Vermogen                   ", amp, " A"
        print "Gas                        ", gas, " m3"

printen(nachtaf, dagaf, nachtterug, dagterug, af, terug, gas, volt, amp)    