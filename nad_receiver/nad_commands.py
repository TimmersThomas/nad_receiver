"""
Commands and operators used by NAD.

CMDS[domain][function]
"""
CMDS = {
    'main':
        {
            'dimmer':
                {'cmd': 'Main.Dimmer',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'mute':
                {'cmd': 'Main.Mute',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'power':
                {'cmd': 'Main.Power',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'volume':
                {'cmd': 'Main.Volume',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'ir':
                {'cmd': 'Main.IR',
                 'supported_operators': ['=']
                 },
            'listeningmode':
                {'cmd': 'Main.ListeningMode',
                 'supported_operators': ['+', '-']
                 },
            'sleep':
                {'cmd': 'Main.Sleep',
                 'supported_operators': ['+', '-']
                 },
            'source':
                {'cmd': 'Main.Source',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'version':
                {'cmd': 'Main.Version',
                 'supported_operators': ['?']
                 }
        },
    'tuner':
        {
            'am_frequency':
                {'cmd': 'Tuner.AM.Frequency',
                 'supported_operators': ['+', '-']
                 },
            'am_preset':
                {'cmd': 'Tuner.AM.Preset',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'band':
                {'cmd': 'Tuner.Band',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'fm_frequency':
                {'cmd': 'Tuner.FM.Frequency',
                 'supported_operators': ['+', '-']
                 },
            'fm_mute':
                {'cmd': 'Tuner.FM.Mute',
                 'supported_operators': ['+', '-', '=', '?']
                 },
            'fm_preset':
                {'cmd': 'Tuner.FM.Preset',
                 'supported_operators': ['+', '-', '=', '?']
                 }
        }
}

CMD_MAIN = "Main"
CMD_BRIGHTNESS = "Main.Brightness"
CMD_BASS_EQ = "Main.Bass"
CMD_CONTROL_STANDBY = "Main.ControlStandby"
CMD_AUTO_STANDBY = "Main.AutoStandby"
CMD_VERSION = "Main.Version"
CMD_MUTE = "Main.Mute"
CMD_POWER = "Main.Power"
CMD_AUTO_SENSE = "Main.AutoSense"
CMD_SOURCE = "Main.Source"
CMD_VOLUME = "Main.Volume"

MSG_ON = 'On'
MSG_OFF = 'Off'

C338_CMDS = {
    'Main':
        {'supported_operators': ['?']
         },
    'Main.AnalogGain':
        {'supported_operators': ['+', '-', '=', '?'],
         'values': range(0, 0),
         'type': int
         },
    'Main.Brightness':
        {'supported_operators': ['+', '-', '=', '?'],
         'values': range(0, 4),
         'type': int
         },
    'Main.Mute':
        {'supported_operators': ['+', '-', '=', '?'],
         'values': [MSG_OFF, MSG_ON],
         'type': bool
         },
    'Main.Power':
        {'supported_operators': ['+', '-', '=', '?'],
         'values': [MSG_OFF, MSG_ON],
         'type': bool
         },
    'Main.Volume':
        {'supported_operators': ['+', '-', '=', '?'],
         'values': range(-80, 0),
         'type': float
         },
    'Main.Bass':
        {'supported_operators': ['+', '-', '=', '?'],
         'values': [MSG_OFF, MSG_ON],
         'type': bool
         },
    'Main.ControlStandby':
        {'supported_operators': ['+', '-', '=', '?'],
         'values': [MSG_OFF, MSG_ON],
         'type': bool
         },
    'Main.AutoStandby':
        {'supported_operators': ['+', '-', '=', '?'],
         'values': [MSG_OFF, MSG_ON],
         'type': bool
         },
    'Main.AutoSense':
        {'supported_operators': ['+', '-', '=', '?'],
         'values': [MSG_OFF, MSG_ON],
         'type': bool
         },
    'Main.Source':
        {'supported_operators': ['+', '-', '=', '?'],
         'values': ["Stream", "Wireless", "TV", "Phono", "Coax1", "Coax2", "Opt1", "Opt2"]
         },
    'Main.Version':
        {'supported_operators': ['?'],
         'type': float
         },
    'Main.Model':
        {'supported_operators': ['?'],
         'values': ['NADC338']
         }
}