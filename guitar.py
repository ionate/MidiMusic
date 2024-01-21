from scamp import *
import time
import random

from support import CHORDS
from support import presetlist
from support import EMOTIONS

def create_midi_file():
    s = Session()
    piano = s.new_part("piano")
    scale = [0, 2, 4, 5, 7, 9, 11]
    notes = [random.choice(scale) for _ in range(10)]
    s.start_transcribing()

    for note in notes:
        piano.play_note(note + 60, 1, 0.5)  # 60 is middle C in MIDI

    performance = s.stop_transcribing()
    performance.export_to_midi_file("random_midi.mid")
    print('done!')

def session_tests_V2(verbose=False):
    session1 = Session()
    t1 = session1.new_part('string ensemble 1')
    tubebells = session1.new_part('string ensemble 2')
    t1.start_note(48, 1.0)
    ionian = [2, 2, 1, 2, 2, 2, 1] # number of steps between notes
    ionian2 = [2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1,] #2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1]
    
    pitch = 48 # C Maj
    for i in ionian2:
        tubebells.play_note(pitch, 1.0, 0.1)
        pitch = pitch + ionian[i]
    
    time.sleep(6)
    print('sound ok?')

def session_tests(verbose=False):
    session1 = Session()
    t1 = session1.new_part('trombone')
    tubebells = session1.new_part('tubular bells')
    t1.start_note(48, 1.0)
    ionian = [2, 2, 1, 2, 2, 2, 1] # number of steps between notes
    ionian2 = [2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1]
    ionian4 = [2, 4, 1, -2, 2, 4, 1, 1, 5, 7, 8, 2, 6, 7, 1, 2, 1, -2, 2, 4, 1, 5, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1]

    dorian = ionian[1:7]+ionian[0:1]
    pitch = 48 # C Maj
    for i in ionian2:
        tubebells.play_note(pitch, 1.0, 0.1)
        pitch = pitch + ionian[i]
    time.sleep(6)
    print('sound ok?')

def my_first_song_noise(verbose=False):
    try:
        s = Session()
        trombone = s.new_part('trombone')
        trombone.play_note(55, 1.0, 2.0, blocking=False) # low c
        trombone.play_note(66, 0.5, 3.0, blocking=False) # low c
        trombone.play_note(33, 1.0, 5.0, blocking=False) # low c


        s5 = Session()
        synthdrum = s5.new_part('Synth Drum')
        synthdrum.play_note(89, 1.0, 10.0, blocking=False) 

        s6 = Session()
        guitar = s6.new_part('guitar')
        guitar.play_note(48, 1.0, 1.0) # low c

        s = Session()
        gh = s.new_part('Guitar harmonics')
        gh.play_note(48, 1.0, 1.0) # low c

        s2 = Session()
        piano = s2.new_part('piano')
        piano.play_note(48, 1.0, 5.0, blocking=False) # low c

        s3 = Session()
        Celesta = s3.new_part('Celesta')
        Celesta.play_note(48, 1.0, 5.0, blocking=False) # low c

        s4 = Session()
        banjo = s4.new_part('Banjo')
        banjo.play_note(48, 1.0, 5.0, blocking=False) # low c

        s.tempo = 100
        guitar.play_note(40, 1.0, 1.0, blocking=False) # low e

        # for major scale
        # do re mi fa so la ti (do)
        ionian = [2, 2, 1, 2, 2, 2, 1] # number of steps between notes
        ionian2 = [2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1]
        ionian4 = [2, 4, 1, -2, 2, 4, 1, 1, 5, 7, 8, 2, 6, 7, 1, 2, 1, -2, 2, 4, 1, 5, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1]

        dorian = ionian[1:7]+ionian[0:1]
        pitch = 48 # C Maj
        for i in ionian2:
            synthdrum.play_note(pitch, 1.0, 0.1)
            pitch = pitch + ionian[i]

        for i in ionian4:
            synthdrum.play_note(pitch, 1.0, 0.1)
            pitch = pitch + ionian[i]

        pitch = 50 # D Maj
        for i in dorian:
            synthdrum.play_note(pitch, 1.0, 0.5)
            pitch = pitch + ionian[i]

        for i in dorian:
            synthdrum.play_note(pitch, 1.0, 0.5)
            pitch = pitch + ionian[i]

        for i in dorian:
            synthdrum.play_note(pitch, 1.0, 0.5)
            pitch = pitch + ionian[i]

        dorian = ionian[1:7]+ionian[0:1]
        pitch = 48 # C Maj
        for i in ionian2:
            synthdrum.play_note(pitch, 1.0, 0.1)
            pitch = pitch + ionian[-i]
    except Exception as ex:
        print (f'Exc={ex}')

def playing_with_freqs():
    s = Session()
    guitar = s.new_part('Guitar')
    emotions = EMOTIONS.get('Spooky')
    for ch in emotions:
        mid = CHORDS.get(ch)[1]
        guitar.play_note(mid, 0.5, 0.5)

    guitar.play_note(CHORDS.get('C')[1], 1.0, 2.0, blocking=False)
    guitar.play_note(CHORDS.get('G')[1], 0.5, 3.0, blocking=False)
    guitar.play_note(CHORDS.get('B')[1], 1.0, 5.0, blocking=False)
    
if __name__ == '__main__':
    #playing_with_freqs()
    create_midi_file()
    session_tests_V2()
    my_first_song_noise()
    print ('bye!')
