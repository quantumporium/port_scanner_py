# setup and testing of scanner.py
echo "[info] this is is used to setup and test scanner.py, it was create by 
quantumporium (quantumporium[at]email.com)."

echo "+ start a simple http server at the address 0.0.0.0 with the port 8000 open"

python3 -m http.server 8000 &> /dev/null &
pid=$!

# give server time to start up
sleep 1

echo "+ manual test scanner.py on port 8000 and on port 9000"
./scanner.py 0.0.0.0 8000
./scanner.py 0.0.0.0 9000


# kill server
kill "${pid}"
