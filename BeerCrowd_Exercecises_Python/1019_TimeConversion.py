"""
Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.

"""

time = int(input())
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60 
seconds = time
print(f"{hour}:{minutes}:{seconds}")    