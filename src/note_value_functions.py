# this will be the place for calculating the note value looking at the distance between one snapped point and the next
# or the end of the rhythm section
from src.snap_functions import distance
from music21 import note, stream


def calculate_note_value(starting_point, ending_point):
    note_length = distance(starting_point, ending_point)
    note_value = None
    if note_length == 4.0:
        note_value = 'whole'
    if note_length == 2.0:
        note_value = 'half'
    if note_length == 1.0:
        note_value = 'quarter'
    if note_length == 0.5:
        note_value = 'eighth'
    if note_length == 0.25:
        note_value = 'sixteenth'
    if note_length == 0.125:
        note_value = 'thirty-second'
    if round(note_length, 2) == 0.33:  # I might have to import decimal because python has arithmetic error here
        note_value = 'triplet'
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


# def generate_notes(note_values):
#     def generate_note(note_value):
#         n = note.Note('C4', )
