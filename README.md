# NextWatch
HytelX NextWatch Project

Function: [PreChecks, PostChecks]

How to run?
Prechecks: 
    # <python> <file> <Function> <device type> <ip> <user> <password>
    python app.py PreChecks Router 192.168.1.1 admin password

Postchecks:
    # <python> <file> <Function> <device type> <ip> <user> <password>
    python app.py PostChecks Router 192.168.1.1 admin password

Make it windows installable
@echo off
python path\to\nextwatch.py %*

# Run as
NextWatch PreChecks Router 192.168.1.1 admin password
