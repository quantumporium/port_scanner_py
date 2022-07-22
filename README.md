# Port Scanner (made with python)
Port-scanner.py is a terminal based utiliti. That allow you to see if a port 
on a given host is open or closed.You can either use in an interactive mode or
with command line argument.


## Content table
- Requirement
- Testing
- Usage
- License

## Requirement
You need to have or install pytest, because it is necessary for the unit test to work correctly.

If you don't have it can install it with pip by using the expression below.d3'
```py
pip install pytest
```

## Testing
If you are in linux (or any unix based system) start the bash file `` test-scanner.sh ``.
Or if you are in window you can do it with the command: `` python3 -m pytest ``. But you first need to
create an http server with the port 9000 open in another terminal. Used to command `` python3 http.server 9000`` to do so.
All the tests files are in the test folder.

## Usage
You have to choice of usage for this utilite. You can either give the host and
the port via the command line as argument to the script. Or you can give the in a interactive 
way via prompt that will apear on the terminal.

```bash
usage 1:
./port-scanner.py [ip] [port]
[ip] The port (port) is open

usage 2:
./port-scanner
Enter the ip: 0.0.0.0
Enter the port: 8000
[0.0.0.0] The port ( 8000 ) is open

```
## License
This utilitie use the gpl version 2 license. You can learn more about the licence [here](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html).
