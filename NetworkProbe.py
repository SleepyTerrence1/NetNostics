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
            print("")
            print("Not vaild integer")

    Extracted_Time = []
    try:
        print("Please wait for results...")
     
        for i in range(Probe_Amount):

            try:
                result = sp.run(["ping", "-c", "1", Hostname], capture_output = True, text=True, timeout = 5)
            except sp.TimeoutExpired: 
                Extracted_Time.append(None)
                print("Server Timed Out")

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

        sucessful_pings = [t for t in Extracted_Time if t is not None]

        total_sent = len(Extracted_Time)
        total_recieved = len(sucessful_pings)
        loss_percent = ((total_sent - total_recieved) / total_sent) * 100

        print("")
        print(f"Packets Sent: {total_sent} | Recieved: {total_recieved} | Loss: {float(loss_percent)}")

    except FileNotFoundError:
        print("Ping is not installed")
if __name__ == "__main__":
    NetworkProbeLauncher()