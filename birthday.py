def timeConversion(s):
    hour = int(s[0:2])
    minutes_seconds = s[2:8]
    am_pm = s[8:10]

    if am_pm == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12

    return f"{hour:02d}{minutes_seconds}"
    
s=input()
x=timeConversion(s)
print(x)

