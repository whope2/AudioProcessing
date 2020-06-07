from playsound import playsound
import audio_generator

for x in range(15):
    hz = 110 + x*110
    wav_filename= 'hz_' + str(hz) + '.wav'
    print('generate audio file %s' % wav_filename)
    audio_generator.gen_audio(hz, 1, 3, wav_filename)
    playsound(wav_filename)








