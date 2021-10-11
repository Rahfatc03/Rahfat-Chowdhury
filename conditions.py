print ('Please enter the current temperature.')
temp= int(input (''))
if temp > 90:
    print ('Wear Shorts')
elif temp > 70:
    print ('Short Sleeves are fine')
elif temp > 50:
    print ('Wear a jacket')
elif temp > 32:
    print ('Wear a heavy coat')
else:
    print ('Stay Inside')
