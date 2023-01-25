# this will be the place for calculating the note value looking at the distance between one snapped point and the next
# or the end of the rhythm section
from src.snap_functions import distance
from music21 import note, stream


def calculate_note_value(starting_point, ending_point):
    note_value = distance(starting_point, ending_point)
    return note_value


def name_list(snapped_points):
    note_values = []

    def get_note_value(idx):
        if snapped_points[idx] == snapped_points[-1]:
            return calculate_note_value(snapped_points[idx], 4.0)
        else:
            return calculate_note_value(snapped_points[idx], snapped_points[idx + 1])

    for snapped_idx in range(len(snapped_points)):
        note_values.append(get_note_value(snapped_idx))
    return note_values


def generate_notes(note_values):
    def generate_note(note_value):
        n = note.Note('C4', quarterLength=note_value)
        return n

    s = stream.Stream()
    for note_value in note_values:
        s.append(generate_note(note_value))
    s.show()
    return s
