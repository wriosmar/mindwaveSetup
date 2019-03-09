import mindwave, time
import numpy

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

def smooth(x,window_len=5,window='hanning'):
    """smooth the data using a window with requested size.
    
    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal 
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.
    
    input:
        x: the input signal 
        window_len: the dimension of the smoothing window; should be an odd integer
        window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
            flat window will produce a moving average smoothing.

    output:
        the smoothed signal
        
    example:

    t=linspace(-2,2,0.1)
    x=sin(t)+randn(len(t))*0.1
    y=smooth(x)
    
    see also: 
    
    numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman, numpy.convolve
    scipy.signal.lfilter
 
    TODO: the window parameter could be the window itself if an array instead of a string
    NOTE: length(output) != length(input), to correct this: return y[(window_len/2-1):-(window_len/2)] instead of just y.
    """

    if x.ndim != 1:
        raise ValueError, "smooth only accepts 1 dimension arrays."

    if x.size < window_len:
        raise ValueError, "Input vector needs to be bigger than window size."

    if window_len<3:
        return x

    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"

    s=numpy.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]
    #print(len(s))
    if window == 'flat': #moving average
        w=numpy.ones(window_len,'d')
    else:
        w=eval('numpy.'+window+'(window_len)')

    y=numpy.convolve(w/w.sum(),s,mode='valid')
    return y


#while headset.status != 'connected':
#   time.sleep(0.5)
#   print(headset.status)
#    print('Headset not connected, attempting to reconnect')
#    headset.connect()

# get current signal reading, 0 being the best and 255 being the worst
print('Signal level: %s') % (headset.poor_signal)

# get current attention and meditation levels once a second for 100 seconds
print("Measuring attention and meditation levels in 5 seconds, concentrate")
time.sleep(5)
att = []
med = []
att_avg = []
att_weighted_avg = []
for i in range(100): # while headset.poor_signal < 255:
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
