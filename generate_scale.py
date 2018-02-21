"""
A script to generate scales.

Ex: `python generate_scale.py D minor`
"""

import sys

def step_to_int(step):
    return {'h': 1, 'W': 2}[step]

class ScaleGenerator:
    """
    Can generate each note found in a particular scale. Assumes all accidentals
    are sharp.
    """

    NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    SCALE_SEQUENCES = {
        'major': ['W', 'W', 'h', 'W', 'W', 'W', 'h'],
        'minor': ['W', 'h', 'W', 'W', 'h', 'W', 'W']
    }

    @classmethod
    def scale(cls, root, key):
        sequence = cls.SCALE_SEQUENCES[key]
        root_idx = cls.NOTES.index(root)

        result = [root]
        step_total = 0
        for step in sequence:
            step_total += step_to_int(step)
            result.append(cls.NOTES[(root_idx + step_total) % len(cls.NOTES)])

        return result

    @classmethod
    def print_all_scales(cls):
        for key in cls.SCALE_SEQUENCES:
            for note in cls.NOTES:
                print('{} {}:'.format(note, key))
                for key_note in cls.scale(note, key):
                    print(key_note)
                print('')


if __name__ == "__main__":
    ROOT = sys.argv[1]
    KEY = sys.argv[2]

    print(ScaleGenerator.scale(ROOT, KEY))
