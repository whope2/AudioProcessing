import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


def gen_audio(freq_in_hz, amplitude, duration_in_seconds, wav_filename):

    sr = 44100 # default sample rate per seconds for human ears
    t = np.linspace(0, duration_in_seconds, int(duration_in_seconds*sr), endpoint=False) # an array of time variable from 0 to duration_in_seconds with sr sampling rate
    x = amplitude * np.sin(2 * np.pi * t * freq_in_hz) # generate sine wave

    '''
    #Plot to debug signals
    plt.ion()
    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(x, sr=sr)
    plt.show()
    plt.pause(0.001)
    #'''
    
    librosa.output.write_wav(wav_filename, x, sr) #write to the wav file


