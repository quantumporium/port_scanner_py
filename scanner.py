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
    except:
        return False

def get_address_input():
    ip = input("Enter the ip: ")

    try:
        port = int(input("Enter the port: "))
    except:
        print("error") 
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
    
    try:
        connection = s.connect_ex( address )
        return connection
    except Exception as ex:
        print( ex )
        
if __name__ == "__main__":
    
    
    if len(sys.argv) == 2 and sys.argv[1] == '--help':
        usage()
        exit()
    
    if address := get_command_line() :
        # tcp_return 0 if the connection is possible need toswitch return in o
        #rder to use it correctly
        if not tcp_connection( address ):
            print( "Port is open")
        else:
            print( "port is closed")
    else:
        address = get_address_input()
        if not tcp_connection( address ) :
            print(" port is open" )
        else:
            print(" port is closed")
        
    
