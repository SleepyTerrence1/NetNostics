#Calculate the results of measurements
import statistics as st
list = [56.2, 30.9, 28.5, None, 28.2, None]

def AverageRTT(List):
    return st.mean(List)

def MinRTT(List):
    return st.median_low(List)

def MaxRTT(List):
    return st.median_high(List)

ListMOD = [t for t in list if t is not None]
print(AverageRTT(ListMOD))
print(MaxRTT(ListMOD))
print(MinRTT(ListMOD))