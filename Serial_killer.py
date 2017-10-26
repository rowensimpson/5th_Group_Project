import serial

ser = serial.Serial('COM6',baudrate=9600, timeout=0.25)



while 1:
    file = open("testFile.txt", "a")
    arduinoData = ser.readline().decode('ascii')
    print(arduinoData)
    file.write(arduinoData)
    file.close()

