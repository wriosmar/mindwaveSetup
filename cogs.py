import mindwave, time

headset = mindwave.Headset('/dev/tty.MindWaveMobile-SerialPo')
time.sleep(2)

print('Connecting...')
# Note: ID not necessary for bluetooth connection
# headset.status doesn't appear to work, connected but gives None
# known issues with blink readings

# 'None' expected
print(headset.headset_id)
print(headset.status)

def smooth_avg (arr):
    points = arr[-5:]
    return (sum(points))/5

def smooth_weighted_avg (arr):
    points = arr[-5:]
    points[2] = 2 * points[2]
    points[3] = 3 * points[3]
    points[4] = 3 * points[4]
    return (sum(points))/10


#while headset.status != 'connected':
#   time.sleep(0.5)
#   print(headset.status)
#    print('Headset not connected, attempting to reconnect')
#    headset.connect()

# get current signal reading, 0 being the best and 255 being the worst
print('Signal level: %s') % (headset.poor_signal)

# get current attention and meditation levels once a second for 20 seconds
print("Measuring attention and meditation levels in 5 seconds, concentrate")
time.sleep(5)
att = []
med = []
att_avg = []
att_weighted_avg = []
for i in range(20): # while headset.poor_signal < 255:
    print("Current Attention: %s, Current Meditation: %s") % (headset.attention, headset.meditation)
    att.append(headset.attention)
    med.append(headset.meditation)
    if len(att) < 5:
        continue
    att_avg.append(smooth_avg(att))
    att_w_avg.append(smooth_weighted_avg(att))
    time.sleep(1)

# 'None' expected
print('Headset Status: %s') % (headset.status)

#while headset.status is None:
#   print('Headset not connected, attempting to reconnect..')  
#   if headset.status == 'connected':
#       print('Headset connected')
#   elif headset.status == 'scanning':
#       print('Headset scanning')
#   elif headset.status == 'standby':
#       print('Headset on standby')
