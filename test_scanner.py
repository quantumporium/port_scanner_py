import pytest
import scanner
import sys

# command line argument
def test_goodArg():
    if '-v' in sys.argv :
        sys.argv.remove('-v') # remove the -v of pytest from the arguement vector

    sys.argv.append('0.0.0.0')
    sys.argv.append('9000')

    assert scanner.get_command_line() == ( '0.0.0.0', 9000 )

def test_baddArg():

    sys.argv.pop()
    sys.argv.pop()
    sys.argv.append('0.0.0.0')
    sys.argv.append('abc')
    assert scanner.get_command_line() == False

# test connection 
def test_goodCon():
    address = ( '0.0.0.0', 9000 )
    assert scanner.tcp_connection( address ) == ( 0,  ('0.0.0.0', 9000 ))

def test_badCon():
    address = ( '0.0.0.0', 90 )
    assert scanner.tcp_connection( address ) != ( 0, ('0.0.0.0', 9000 ))

def test_badCon1():
    ' bad ip bug good port'
    with pytest.raises( SystemExit ) as wrapper:
        scanner.tcp_connection( ('a.a.a.a', 9000) )
    assert wrapper.type == SystemExit

def test_badCon2():
    ' bad ip and bad port '
    with pytest.raises( SystemExit ) as wrapper:
        scanner.tcp_connection( ('a.a.a.a', 900) )
    assert wrapper.type == SystemExit

# test usage
def test_usage():
    sys.argv.clear()
    sys.argv.append('-v')

    if len(sys.argv) == 2 and sys.argv[1] == '--help':
        assert usage() == 'usage_function'
 
