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

# disconnect handler
def disco(headset):
    print('Headset disconnected')
#headset.disconnected_handlers(disco)

# blink detection handler
def on_blink(headset, blink_strength):
    print("Blink detected. Strength: %s") % (blink_strength)
headset.blink_handlers.append(on_blink)

#while headset.status != 'connected':
#   time.sleep(0.5)
#   print(headset.status)
#    print('Headset not connected, attempting to reconnect')
#    headset.connect()

# get current signal reading, 0 being the best and 255 being the worst
print('Signal level: %s') % (headset.poor_signal)

# get current attention level once a second for 10 seconds
print("Measuring attention level in 5 seconds, concentrate")
time.sleep(5)
for x in range(10):
    print("Current Attention: %s, Current Meditation: %s") % (headset.attention, headset.meditation)
    time.sleep(1)

# get meditation level once a second for 10 seconds
#print('Measuring meditation level in 5 seconds, calm')
#time.sleep(5)
#for x in range(10):
    #print("current meditation: %s") % (headset.meditation)
    #time.sleep(1)

#print('Measuring blink, try to blink until we read 10 blinks')
#blinkNum = 0
#while blinkNum != 10:
#   if on_blink == True:
#       blinkNum = blinkNum + 1

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
