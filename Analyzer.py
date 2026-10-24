#Calculate the results of measurements
import statistics as st
list = [56.2, 30.9, 28.5, None, 28.2, None]

def AverageRTT(List):
    return st.mean(List)

def MinRTT(List):
    return st.median_low(List)

def MaxRTT(List):
    return st.median_high(List)

def PacketAnyalsis(list):
    sucessful_pings = [t for t in list if t is not None]

    total_sent = len(list)
    total_recieved = len(sucessful_pings)
    loss_percent = ((total_sent - total_recieved) / total_sent) * 100
    print(f"Packets Sent: {total_sent} | Recieved: {total_recieved} | Loss: {loss_percent}")

ListMOD = [t for t in list if t is not None]
print(AverageRTT(ListMOD))
print(MaxRTT(ListMOD))
print(MinRTT(ListMOD))
PacketAnyalsis(list)