# this next challange for this code is to sort numbers into there respective elements


import serial
# indicates if the packer needs to pack
rd_data = False
# indicator that the transmission has just ended
trans_end = False
# sample rate must be greater then the send rate
ser = serial.Serial('COM8', baudrate=9600, timeout=0.05)
# list for storing the incoming data
my_list = []
# set list size index
index = 1
# init the pk_build
pk_build = ''
# what is the size of the packet
PACKET_LENGTH = 13
# infinite loop
while 1:
    arduinoData = ser.readline().decode('ascii')
    print(index)
    # watches for state change characters
    if arduinoData == 'X':
        rd_data = True
        arduinoData = ''
        print('start transmission')

    # looks for start of trasmission indicator. When rd_data = True the array gets packed with data
    if rd_data == True:                                                              # start counting
        if arduinoData != '' and arduinoData != ',':                    # if the buffer contains new data
            print('number builder')
            pk_build = pk_build + arduinoData
        elif arduinoData == ',':
            index += 1
            my_list.append(int(pk_build))
            pk_build = ''                                               # reset packet builder

            # otherwise it waits for data
    else:
        print('waiting for data')

    # looks for the last character in the array then saves the data to the file, this is preformed once at the end of each packet
    if trans_end == True:
        print(str(my_list).strip('[]'))         # prints to console what is saved in the file
        trans_end = False                       # only occurs once
        file = open("testFile.txt", "a")        # open the file
        file.write(str(my_list).strip('[]'))                # append the data
        file.write('\n')
        file.close()                            # close the file
        index = 1                               # trans over, reset index for next iteration
        my_list[:] = []                         # clears the array

    if arduinoData == 'Z':
        print('end transmission')
        rd_data = False                         # the array is ready to store
        trans_end = True                        # indication to store the information
        if index > PACKET_LENGTH:               # check if the number of elements is as expected
            print('packet size error')








