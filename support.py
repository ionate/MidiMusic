CHORDS = {
    'C': (261.63, 60),
    'C#': (277.18, 61),
    'Db': (277.18, 61),
    'D': (293.66, 62),
    'D#': (311.13, 63),
    'Eb': (311.13, 63),
    'E': (329.63, 64),
    'F': (349.23, 65),
    'F#': (369.99, 66),
    'Gb': (369.99, 66),
    'G': (392.00, 67),
    'G#': (415.30, 68),
    'Ab': (415.30, 68),
    'A': (440.00, 69),
    'A#': (466.16, 70),
    'Bb': (466.16, 70),
    'B': (493.88, 71),
    'Cm': (277.18, 61),
    'Cdim': (277.18, 61),
    'C#m': (293.66, 62),
    'C#aug': (311.13, 63),
    'Dm': (293.66, 62),
    'Daug': (311.13, 63),
    'D#m': (311.13, 63),
    'D#aug': (329.63, 64),
    'Em': (329.63, 64),
    'Eaug': (349.23, 65),
    'Fm': (349.23, 65),
    'Faug': (369.99, 66),
    'F#m': (369.99, 66),
    'F#aug': (392.00, 67),
    'Gm': (392.00, 67),
    'Gaug': (415.30, 68),
    'G#m': (415.30, 68),
    'G#aug': (440.00, 69),
    'Am': (440.00, 69),
    'Aaug': (466.16, 70),
    'A#m': (466.16, 70),
    'A#aug': (493.88, 71),
    # Add more chords here...
}

EMOTIONS_BASIC = {
    # Basic Emotions
    "Sad": ["Cm", "Am", "Dm", "Em", "Fm", "Bbm", "Gm"],
    "Happy": ["C", "G", "D", "A", "E", "B", "F#"],
    "Dark": ["C#m", "Bm", "D#m", "F#m", "G#m", "A#m"],
}

EMOTIONS = {
    # Basic Emotions
    "Sad": ["Cm", "Am", "Dm", "Em", "Fm", "Bbm", "Gm"],
    "Happy": ["C", "G", "D", "A", "E", "B", "F#"],
    "Dark": ["C#m", "Bm", "D#m", "F#m", "G#m", "A#m"],
    "Melancholy": ["Cmaj7", "Bm7", "Am7", "Em7", "Dm7"],
    "Cartoon": ["C7", "G7", "F7"],
    "Western": ["Em", "A", "B7"],
    "Country": ["D", "G", "A"],
    "Spooky": ["C#dim", "D#dim", "G#dim", "Edim"],

    # Mood-Related
    "Question": ["Cmaj7sus4", "Gmaj7sus4", "Fmaj7sus4"],
    "Statement": ["C6", "G6", "F6"],
    "Soft": ["Cadd9", "Gadd9", "Dadd9"],
    "Hard": ["C5", "G5", "D5"],

    # Experimental/Unusual
    "Dreamy": ["Cmaj9", "Gmaj9", "Dmaj9"],
    "Tense": ["Caug", "Gaug", "Daug"],
    "Mysterious": ["Cmaj7#11", "Gmaj7#11", "Dmaj7#11"],
    "Magical": ["Cmaj7#5", "Gmaj7#5", "Dmaj7#5"],
    "Uplifting": ["Cmaj7#9", "Gmaj7#9", "Dmaj7#9"],
    "Epic": ["Cmaj7b5", "Gmaj7b5", "Dmaj7b5"],
}

print(CHORDS.get('C')[1])


presetlist = {'Accordion': 22, 'Acoustic Bass': 33, 'Acoustic Grand Piano': 1, 'Acoustic Guitar (nylon)': 25, 
              'Acoustic Guitar (steel)': 26, 'Agogo': 114, 'Alto Sax': 66, 'Applause': 127, 'Bag pipe': 110, 
              'Banjo': 106, 'Baritone Sax': 68, 'Bassoon': 71, 'Bells': 15, 'Bird Tweet': 124, 'Blown Bottle': 77, 
              'Brass Section': 62, 'Breath Noise': 122, 'Bright Acoustic Piano': 2, 'Celesta': 9, 'Cello': 43, 'Choir Aahs': 53, 
              'Church Organ': 20, 'Clarinet': 72, 'Clavinet': 8, 'Contrabass': 44, 'Distortion Guitar': 31, 'Drawbar Organ': 17, 
              'Dulcimer': 16, 'Electric Bass (finger)': 34, 'Electric Bass (pick)': 35, 'Electric Grand Piano': 3, 
              'Electric Guitar (clean)': 28, 'Electric Guitar (jazz)': 27, 'Electric Guitar (muted)': 29, 'Electric Piano 1': 5, 
              'Electric Piano 2': 6, 'English Horn': 70, 'FX 1 (rain)': 97, 'FX 2 (soundtrack)': 98, 'FX 3 (crystal)': 99, 
              'FX 4 (atmosphere)': 100, 'FX 5 (brightness)': 101, 'FX 6 (goblins)': 102, 'FX 7 (echoes)': 103, 'FX 8 (sci-fi)': 104, 
              'Fiddle': 111, 'Flute': 74, 'French Horn': 61, 'Fretless Bass': 36, 'Glockenspiel': 10, 'Guitar Fret Noise': 121, 
              'Honky-tonk Piano': 4, 'Horn': 61, 'Kalimba': 109, 'Koto': 108, 'Lead 1 (square)': 81, 'Lead 2 (sawtooth)': 82, 
              'Lead 3 (calliope)': 83, 'Lead 4 (chiff)': 84, 'Lead 5 (charang)': 85, 'Lead 6 (voice)': 86, 'Lead 7 (fifths)': 87, 
              'Lead 8 (bass + lead)': 88, 'Marimba': 13, 'Melodic Tom': 118, 'Music Box': 11, 'Muted Trumpet': 60, 'Oboe': 69, 'Ocarina': 80, 'Orchestra Hit': 56, 'Orchestral Harp': 47, 'Organ': 20, 'Overdriven Guitar': 30, 'Pad 1 (new age)': 89, 'Pad 2 (warm)': 90, 'Pad 3 (polysynth)': 91, 'Pad 4 (choir)': 92, 'Pad 5 (bowed)': 93, 'Pad 6 (metallic)': 94, 'Pad 7 (halo)': 95, 'Pad 8 (sweep)': 96, 'Pan Flute': 76, 'Percussive Organ': 18, 'Piano': 1, 'Piccolo': 73, 'Pizzicato Strings': 46, 'Recorder': 75, 'Reed Organ': 21, 'Reverse Cymbal': 120, 'Rock Organ': 19, 'Sax': 66, 'Seashore': 123, 'Shakuhachi': 78, 'Shamisen': 107, 'Shanai': 112, 'Sitar': 105, 'Slap Bass 1': 37, 'Slap Bass 2': 38, 'Soprano Sax': 65, 
              'Steel Drums': 115, 'String Ensemble 1': 49, 'String Ensemble 2': 50, 'Strings': 49, 'Synth Bass 1': 39, 'Synth Bass 2': 40, 'Synth Brass 1': 63, 'Synth Brass 2': 64, 
              'Synth Drum': 119, 'Synth Strings 1': 51, 'Synth Strings 2': 52, 'Synth Voice': 55, 
              'Taiko Drum': 117, 'Tango Accordion': 24, 'Telephone Ring': 125, 'Tenor Sax': 67, 'Timpani': 48, 'Tinkle Bell': 113, 'Tom': 118, 'Tremolo Strings': 45, 
              'Trombone': 58, 'Trumpet': 57, 'Tuba': 59, 'Tubular Bells': 15, 'Vibraphone': 12, 'Viola': 42, 'Violin': 41, 'Violoncello': 43, 'Voice Oohs': 54, 'Whistle': 79, 'Woodblock': 116, 'Xylophone': 14}


# CHORD = {
#     'C': 261.63,
#     'C#': 277.18,
#     'Db': 277.18,
#     'D': 293.66,
#     'D#': 311.13,
#     'Eb': 311.13,
#     'E': 329.63,
#     'F': 349.23,
#     'F#': 369.99,
#     'Gb': 369.99,
#     'G': 392.00,
#     'G#': 415.30,
#     'Ab': 415.30,
#     'A': 440.00,
#     'A#': 466.16,
#     'Bb': 466.16,
#     'B': 493.88,
#     'Cm': 261.63 * (6 / 5),  # C minor (C-Eb-G)
#     'Cdim': 261.63 * (1.122462048309373),  # C diminished (C-Eb-Gb)
#     'C#m': 277.18 * (6 / 5),  # C# minor (C#-E-G#)
#     'C#aug': 277.18 * (45 / 32),  # C# augmented (C#-E-Gx)
#     'Dbm': 277.18 * (6 / 5),  # Db minor (Db-E-Ab)
#     'Dbaug': 277.18 * (45 / 32),  # Db augmented (Db-E-A)
#     'Dm': 293.66 * (6 / 5),  # D minor (D-F-A)
#     'Daug': 293.66 * (45 / 32),  # D augmented (D-Fx-A)
#     'D#m': 311.13 * (6 / 5),  # D# minor (D#-F#-A#)
#     'D#aug': 311.13 * (45 / 32),  # D# augmented (D#-Fx-A#)
#     'Ebm': 311.13 * (6 / 5),  # Eb minor (Eb-Gb-Bb)
#     'Ebaug': 311.13 * (45 / 32),  # Eb augmented (Eb-G-Bb)
#     'Em': 329.63 * (6 / 5),  # E minor (E-G-B)
#     'Eaug': 329.63 * (45 / 32),  # E augmented (E-Gx-B)
#     'Fm': 349.23 * (6 / 5),  # F minor (F-Ab-C)
#     'Faug': 349.23 * (45 / 32),  # F augmented (F-A-C)
#     'F#m': 369.99 * (6 / 5),  # F# minor (F#-A-C#)
#     'F#aug': 369.99 * (45 / 32),  # F# augmented (F#-A#-C#)
#     'Gbm': 369.99 * (6 / 5),  # Gb minor (Gb-Bb-Db)
#     'Gbaug': 369.99 * (45 / 32),  # Gb augmented (Gb-B-Db)
#     'Gm': 392.00 * (6 / 5),  # G minor (G-Bb-D)
#     'Gaug': 392.00 * (45 / 32),  # G augmented (G-B-D)
#     'G#m': 415.30 * (6 / 5),  # G# minor (G#-B-D#)
#     'G#aug': 415.30 * (45 / 32),  # G# augmented (G#-B#-D#)
#     'Abm': 415.30 * (6 / 5),  # Ab minor (Ab-B-Eb)
#     'Abaug': 415.30 * (45 / 32),  # Ab augmented (Ab-B-E)
#     'Am': 440.00 * (6 / 5),  # A minor (A-C-E)
#     'Aaug': 440.00 * (45 / 32),  # A augmented (A-Cx-E)
#     'A#m': 466.16 * (6 / 5),  # A# minor (A#-C#-F)
#     'A#aug': 466.16 * (45 / 32),  # A# augmented (A#-Cx-F)
#     'Bbm': 466.16 * (6 / 5),  # Bb minor (Bb-Db-F)
#     'Bbaug': 466.16 * (45 / 32),  # Bb augmented (Bb-D-F)
#     'Bm': 493.88 * (6 / 5),  # B minor (B-D-F#)
#     'Baug': 493.88 * (45 / 32),  # B augmented (B-Dx-F#)
#     'Gmaj7#11': 392.00 * (3 / 2) * (5 / 4) * (17 / 16),  # Gmaj7#11 (G-B-D-F#-A-C)
#     # Add more chord frequencies here...
# }
