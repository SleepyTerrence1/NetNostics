#RUns probes, collects measurements
import subprocess as sp
Hostname = input("Enter Domain: ")

try:
    print("Please wait for results...")
    
    if result.returncode == 0:
        print(f"\n{result.stdout}")
    else:
        print(result.stderr if result.stderr else "Ping failed; Check domain and try again.")
    
except sp.TimeoutExpired:
    print("Server Timed Out")
except FileNotFoundError:
    print("Ping is not installed")
