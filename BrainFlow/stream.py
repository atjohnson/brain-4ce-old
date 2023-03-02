import argparse
import logging
import PyQt5
import sys
import numpy as np
import time
import pyqtgraph as pg
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes, DetrendOperations
from PyQt5 import QtWidgets
from pyqtgraph.Qt import QtGui, QtCore


#board_shim.stop_stream() to stop streaming
#get_current_board_data() - returns array of latest data stored in ringbuffer, does not clear ring buffer.
#get_board_data(int count) - gets num of elements in ring buffer
#insert_marker() - inserts marker to data stream
#get_board_data() gets all data and removes from ringbuffer

def begin_stream(board_shim):

    try:
        board_shim.prepare_session() #need this to prepare streaming session
        board_shim.start_stream(45000) #begins data stream stores data in ringbuffer, first  arg is buffer size 
    except BaseException:
        logging.warning('Exception', exc_info=True)
    finally:
        logging.info('End')
        if board_shim.is_prepared():
            logging.info('Releasing session')
            board_shim.release_session() #end session 
    return board_shim

def end_stream(board_shim):
    data = board_shim.get_board_data()
    board_shim.stop_stream()
    board_shim.release_session()
    return data            


def main():
    BoardShim.enable_dev_board_logger()
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser()
    # use docs to check which parameters are required for specific board, e.g. for Cyton - set serial port
    parser.add_argument('--timeout', type=int, help='timeout for device discovery or connection', required=False,
                        default=0)
    parser.add_argument('--ip-port', type=int, help='ip port', required=False, default=0)
    parser.add_argument('--ip-protocol', type=int, help='ip protocol, check IpProtocolType enum', required=False,
                        default=0)
    parser.add_argument('--ip-address', type=str, help='ip address', required=False, default='')
    parser.add_argument('--serial-port', type=str, help='serial port', required=False, default='')
    parser.add_argument('--mac-address', type=str, help='mac address', required=False, default='')
    parser.add_argument('--other-info', type=str, help='other info', required=False, default='')
    parser.add_argument('--streamer-params', type=str, help='streamer params', required=False, default='')
    parser.add_argument('--serial-number', type=str, help='serial number', required=False, default='')
    parser.add_argument('--board-id', type=int, help='board id, check docs to get a list of supported boards',
                        required=False, default=BoardIds.SYNTHETIC_BOARD) #BOARD ID HERE - CHANGE FOR CYTON
    parser.add_argument('--file', type=str, help='file', required=False, default='')
    parser.add_argument('--master-board', type=int, help='master board id for streaming and playback boards',
                        required=False, default=BoardIds.NO_BOARD)
    args = parser.parse_args()

    params = BrainFlowInputParams()
    params.ip_port = args.ip_port
    params.serial_port = args.serial_port
    params.mac_address = args.mac_address
    params.other_info = args.other_info
    params.serial_number = args.serial_number
    params.ip_address = args.ip_address
    params.ip_protocol = args.ip_protocol
    params.timeout = args.timeout
    params.file = args.file
    params.master_board = args.master_board

    board_shim = BoardShim(args.board_id, params) #initiate board with params and ID
    board_shim.prepare_session() #need this to prepare streaming session

    end = False
    data = [];

    while (end == False):
        in1 = input("Type 'start' to begin data stream, 'stop' to end:\n")
        if (in1 == 'start'):
            board_shim.start_stream(45000)
        if(in1 == 'stop'):
            board_shim.stop_stream()
            data = board_shim.get_board_data()
            end = True
        if(in1[0:6] == "start "):
            board_shim.start_stream(45000)           
            time.sleep(int(in1[6]))
            board_shim.stop_stream()
            data = board_shim.get_board_data()
            end = True
    # Data output is size 32x(250*s)
    print(len(data[0]))

    np.savetxt("out.csv", data, delimiter=", ", fmt='%.3f')

    
if __name__ == '__main__':
    main()