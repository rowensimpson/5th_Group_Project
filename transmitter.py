import serial
import queue


def packet_builder(packet):

    a = len(packet)*2
    packet2 = [','] * a
    for index in range(len(packet)):
        packet2[index*2] = packet[index]
    packet2[-1] = '\n\r'
    return packet2


def packet_sorter(standardPacket):
    print(standardPacket)

    if standardPacket.count(',')+1 == 16:
        e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16 = standardPacket.split(',')

        UnitDataPck = [e1, ',', e2, ',', e3, ',', e4, ',', e5, ',', e6, ',', e7, ',', e8, ',', e9, ',', e10, ',', e11,
                       ',', e12, ',', e13, '\n']
        StateDataPck = [e14, ',', e15, ',', e16]

        unitdatafile = open("UnitData.txt", "a")
        for elements in UnitDataPck:
            unitdatafile.write(elements)


        open('state.txt', 'w').close()  # wipe last state results
        statefile = open("state.txt", "a")  # open file form ammending
        for elements in StateDataPck:
            statefile.write(elements)
        statefile.close()
    else:
        print('packet error')




# prepares both data files for use
def reset_UD_SD_file():
    open('UnitData.txt', 'w').close()  # purge the file and prep for new data
    afile = open("UnitData.txt", "a")
    afile.write('1,0,0,0,0,0,0,0,0,0,0,0,0\n') # init so graphs dont break
    afile.close()

    open('state.txt', 'w').close()
    statefile = open("state.txt", "a")
    statefile.write('XXX,YYY,ZZZ') # init so graphs dont break
    statefile.close()

# transmits data to the Hub
def transceiver(receive):
    print('transceiver starting')
    ser = serial.Serial('COM8', baudrate=9600, timeout=1)
    ser.write(bytes('ON\n\r', 'utf-8'))         # GUI connection marker

    reset_UD_SD_file() # reset the data in the unit data file

    while True:                                     # infinite loop

        incomingPacket = ser.readline().decode('ascii')  # read data out of serial buffer as ascii

        if incomingPacket is not '':                       # if the is data there other than free space save to file
            packet_sorter(incomingPacket)                   # function to sort and save incoming data

        try:
            dataout = receive.get(False)               # look for data from GUI
            if dataout is None:                        # test for poison pill
                break
            else:                                   # send state commands
                dataout = packet_builder(dataout)
                for elements in dataout:
                    ser.write(bytes(elements, 'utf-8'))


        except queue.Empty:                         # no data in buffer exception, so look for data coming in
            dataout = None


    ser.write(bytes('OFF\n\r', 'utf-8'))      # GUI disconnection marker
    print('transceiver stopping')

    # UD = []
    # SD = []

    # try:    # sort the standard packet into relevant lists. if successful save to files
    #     = standardPacket.split(',')

    # UD[:] = standardPacket[0:26]                # Unit data sorter
    # UD[-1] = '\n'
    # print(UD)
    # unitdatafile = open("UnitData.txt", "a")
    # for elements in UD:
    #     unitdatafile.write(elements)
    # unitdatafile.close()
    #
    # SD[:] = standardPacket[26:32]               # State data sorter
    # SD = SD[:-1]
    # print('SD: ', SD)
    # open('state.txt', 'w').close()              # wipe last result
    # statefile = open("state.txt", "a")       # open file form ammending
    # for elements in SD:
    #     print(elements)
    #     statefile.write(elements)
    # statefile.close()

    # open('state.txt', 'w').close()              # wipe last state results
    # statefile = open("state.txt", "a")       # open file form ammending
    # for elements in SD:
    #     print(elements)
    #     statefile.write(elements)
    # statefile.close()


    #
    # except:     # if errors occur during sorting abandon packet
    #     print('incoming packet error')