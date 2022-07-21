#!/usr/bin/python3

import socket
import sys

def usage():
    print("""
    scanner.py: Allow you to see if an port is open on a giving server. 
    scanner usage:
    ./scanner.py [ip] [port]
    ./scanner.py
        Enter the ip  :
        Enter the port:
    """)

    return 

def get_command_line():
    try:
        return ( sys.argv[1] , int(sys.argv[2]))
    except ValueError:
        print('[FATAL] A value you enter is invalid you can retry in the interactive mode.')
        return False

def get_address_input():
    ip = input("Enter the ip: ")
    try:
        port = int(input("Enter the port: "))
    except ValueError:
        print("[FATAL] port need to be a number")
        return False
    except: 
        print("[FATALl an fatal error occur")
    
    return (ip, port)

def tcp_connection( address ):
    """
     tcp_connection: create a tcp connection to the given address
     the address is an tuple of two item, containing the ip address
     of who you whant to connect to and the port you whant to connect
     to.It return bool TRUE if the connection is successfull and bool
     False is it is not.

    """
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    error_type = socket.gaierror()

    try:
        connection = s.connect_ex( address )
        return (connection, address)
    except KeyboardInterrupt :
        print("[FATAL] You interrupt to scanning")
    except Exception as ex:
        print("[FATAL] A fatal error occured")
        exit(0)
        
        
if __name__ == "__main__":
    
    
    if len(sys.argv) == 2 and sys.argv[1] == '--help':
        usage()
        exit()
    
    if address := get_command_line() :
        # tcp_return 0 if the connection is possible need toswitch return in o
        #rder to use it correctly
        socket_connection = tcp_connection( address )
        if not socket_connection[0] :
            print(f'[{socket_connection[1][0]}] - port {socket_connection[1][1]} is open')
        else:
            print(f'[{socket_connection[1][0]}] - port {socket_connection[1][1]} is closed')
    else:
        address = get_address_input()
        if address == False:
            exit() # if a fatal error happen

        socket_connection = tcp_connection( address )
        if not socket_connection[0] :
            print(f'[{socket_connection[1][0]}] - port {socket_connection[1][1]} is open')
        else:
            print(f'[{socket_connection[1][0]}] - port {socket_connection[1][1]} is closed')
        
    
