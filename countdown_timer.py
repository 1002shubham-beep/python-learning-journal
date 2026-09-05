import time 

my_time = int(input("Enter the time in seconds: "))

print(f"Timer set for {my_time} seconds")

for i in range(my_time,0,-1):
    time.sleep(1)
    hours = int(i/3600)
    mins = int(i/60) % 60
    secs = i%60
    print(f"{hours:02}:{mins:02}:{secs:02}")

print("Times up")