#RUns probes, collects measurements
import subprocess as sp

def NetworkProbeLauncher():

    Hostname = input("Enter Domain: ")
    while True:
        try:
            Probe_Amount = int(input('How many probes: '))
            if Probe_Amount >= 1:
                break
            else:
                print("\nPlease enter a number 1 or greater")
        except ValueError:
            print("\nNot vaild integer")

    Extracted_Time = []
    try:
        print("Please wait for results...")
     
        for i in range(Probe_Amount):

            try:
                result = sp.run(["ping", "-c", "1", Hostname], capture_output = True, text=True, timeout = 5)
            except sp.TimeoutExpired: 
                Extracted_Time.append(None)
                print(f"Server Timed Out on ping {i+1}")

                continue
        
            if result.returncode == 0 and "time=" in result.stdout:

                SplitThing = result.stdout.split("time=")[1]
                time_num = float(SplitThing.split(" ")[0])

                Extracted_Time.append(time_num)

                print(f"Ping {i+1}: Recieved reply in {time_num} ms")
            else:

                Extracted_Time.append(None)
                print(f"Ping {i+1}: Failed")
                print(f"{result.stderr}")

        return Extracted_Time

    except FileNotFoundError:
        print("Ping is not installed")
if __name__ == "__main__":
    data = NetworkProbeLauncher()