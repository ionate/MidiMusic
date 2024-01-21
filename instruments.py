import scamp


# Dictionary of instrument names and their corresponding SCAMP instrument classes
INSTRUMENTS_DoesntWork = {
    'piano': 44,
    'violin': scamp.Violin,
    'trumpet': scamp.Trumpet,
    'flute': scamp.Flute,
    'cello': scamp.Cello,
    'alto_sax': scamp.AltoSax,
    'tenor_sax': scamp.TenorSax,
    'vibraphone': scamp.Vibraphone,
    'organ': scamp.Organ,
    'clarinet': scamp.Clarinet,
    'harpsichord': scamp.Harpsichord,
    'celesta': scamp.Celesta,
    'bassoon': scamp.Bassoon,
    'ocarina': scamp.Ocarina,
    'accordion': scamp.Accordion,
    'french_horn': scamp.FrenchHorn,
    'bass_clarinet': scamp.BassClarinet,
    'viola': scamp.Viola,
    'marimba': scamp.Marimba,
    'soprano_sax': scamp.SopranoSax,
    'trombone': scamp.Trombone,
    # Add more instruments here...

    # Additional instruments (at least 200 total)
    'guitar_acoustic': scamp.NylonStringGuitar,
    'guitar_steel': scamp.SteelStringGuitar,
    'guitar_jazz': scamp.JazzGuitar,
    'guitar_clean': scamp.CleanGuitar,
    'guitar_muted': scamp.MutedGuitar,
    'guitar_overdrive': scamp.OverdriveGuitar,
    'guitar_distorted': scamp.DistortedGuitar,
    'guitar_harmonics': scamp.HarmonicsGuitar,
    'bass_acoustic': scamp.FingeredBass,
    'bass_fingered': scamp.FingeredBass,
    'bass_picked': scamp.FingeredBass,
    'bass_fretless': scamp.FingeredBass,
    'bass_slap': scamp.FingeredBass,
    'bass_tap': scamp.FingeredBass,
    'strings_pizzicato': scamp.PizzicatoStrings,
    'strings_tremolo': scamp.TremoloStrings,
    'strings_legato': scamp.LegatoStrings,
    'strings_tremolo_legato': scamp.TremoloLegatoStrings,
    'strings_spiccato': scamp.SpiccatoStrings,
    'brass_section': scamp.BrassSection,
    'trumpet_section': scamp.TrumpetSection,
    'trombone_section': scamp.TromboneSection,
    'woodwind_section': scamp.WoodwindSection,
    'mallet_percussion': scamp.MalletPercussion,
    'percussion': scamp.Percussion,
    'synth_lead': scamp.SynthLead,
    'synth_pad': scamp.SynthPad,
    'synth_bass': scamp.SynthBass,
    'synth_effects': scamp.SynthEffects,
    # Add more instruments here...

    # Add more instruments here...
}

# Function to get a list of all instrument names
def get_all_instrument_names():
    return sorted(scamp.SupportedInstruments().keys())

# Function to check if an instrument name is valid
def is_valid_instrument(instrument_name):
    return instrument_name.lower() in scamp.SupportedInstruments()

# Function to get the SCAMP instrument class for a given instrument name
def get_instrument_class(instrument_name):
    return scamp.SupportedInstruments().get(instrument_name.lower())

# Function to get the integer representation of an instrument
def get_instrument_integer(instrument_name):
    return scamp.SupportedInstruments().get(instrument_name.lower(), -1)

# Dictionary of instrument names and their corresponding integers
INSTRUMENTS = {
    instrument_name: get_instrument_integer(instrument_name)
    for instrument_name in get_all_instrument_names()
}

# Example usage:
if __name__ == "__main__":
    print("Available Instruments:")
    for instrument_name, instrument_id in INSTRUMENTS.items():
        print(f"{instrument_name}: {instrument_id}")
        
# # Function to get a list of all instrument names
# def get_all_instrument_names():
#     return sorted(scamp.SupportedInstruments().keys())

# # Function to check if an instrument name is valid
# def is_valid_instrument(instrument_name):
#     return instrument_name.lower() in scamp.SupportedInstruments()

# # Function to get the SCAMP instrument class for a given instrument name
# def get_instrument_class(instrument_name):
#     return scamp.SupportedInstruments().get(instrument_name.lower())

# # Example usage:
# if __name__ == "__main__":
#     all_instruments = get_all_instrument_names()
#     print("Available Instruments:")
#     for instrument in all_instruments:
#         print(instrument)


# # Function to get a list of all instrument names
# def get_all_instrument_names():
#     return list(INSTRUMENTS.keys())

# # Function to check if an instrument name is valid
# def is_valid_instrument(instrument_name):
#     return instrument_name.lower() in INSTRUMENTS

# # Function to get the SCAMP instrument class for a given instrument name
# def get_instrument_class(instrument_name):
#     return INSTRUMENTS.get(instrument_name.lower())

# # Example usage:
# if __name__ == "__main__":
#     instrument_name = 'piano'
#     if is_valid_instrument(instrument_name):
#         instrument_class = get_instrument_class(instrument_name)
#         session = scamp.Session()
#         part = session.new_part('my_part', instrument_class())
#         # Play some notes with the instrument...
