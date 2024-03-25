# Exercise 3
# Your solution comes here
time = int(input("Enter the time: "))
h = time // 3600
mm = (time // 60) - h
ss = time - (h + mm)
print(f"{h}:{mm}:{ss}")