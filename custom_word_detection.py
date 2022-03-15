import pyaudio
import pvporcupine
import struct
import queue

porcupine = None
pa = None
audio_stream = None


try:
    porcupine = pvporcupine.create(keyword_paths=[
        'wake_word\\pause_game_windows_3_30_2021_v1.9.0\\pause_game_windows_2021-03-30-utc_v1_9_0.ppn',
        'wake_word\\play_game_windows_3_30_2021_v1.9.0\\play_game_windows_2021-03-30-utc_v1_9_0.ppn'],
        keywords=["blueberry", "grapefruit"])
        
    pa = pyaudio.PyAudio()
    print("loading complete")
    audio_stream = pa.open(rate=porcupine.sample_rate, channels=1,
                        format=pyaudio.paInt16, input=True,
                        frames_per_buffer=porcupine.frame_length)
    while True:
        print('.',end=' ')
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keyword_index = porcupine.process(pcm)
        if keyword_index==0:
            print('pause')
        elif keyword_index==1:
            print('play')
        
except Exception as e:
    print('-'*35)
    print(e)
    print('-'*35)
finally:
    if porcupine is not None:
        porcupine.delete()

    if audio_stream is not None:
        audio_stream.close()

    if pa is not None:
            pa.terminate()