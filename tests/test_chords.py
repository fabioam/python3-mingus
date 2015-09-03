#!/usr/bin/env python 

from mingus.chords import Chords
from mingus.notes import Note
from hamcrest import *
from common import _chord_tester


def test_Chord_major_triad():
    chord = Chords.major_triad('C4')
    _chord_tester(chord, ['C4', 'E4', 'G4'])

def test_Chord_major_triad_on_Note():
    chord = Chords.major_triad(Note('C4'))
    _chord_tester(chord, ['C4', 'E4', 'G4'])

def test_Chord_major_triad_on_int():
    chord = Chords.major_triad(60)
    _chord_tester(chord, ['C4', 'E4', 'G4'])

def test_Chord_minor_triad():
    chord = Chords.minor_triad('C4')
    _chord_tester(chord, ['C4', 'Eb4', 'G4'])

def test_Chord_diminished_triad():
    chord = Chords.diminished_triad('C4')
    _chord_tester(chord, ['C4', 'Eb4', 'Gb4'])

def test_Chord_augmented_triad():
    chord = Chords.augmented_triad('C4')
    _chord_tester(chord, ['C4', 'E4', 'G#4'])

def test_Chord_major_seventh():
    chord = Chords.major_seventh('C4')
    _chord_tester(chord, ['C4', 'E4', 'G4', 'B4'])

def test_Chord_minor_seventh():
    chord = Chords.minor_seventh('C4')
    _chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4'])

def test_Chord_dominant_seventh():
    chord = Chords.dominant_seventh('C4')
    _chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4'])

def test_Chord_half_diminished_seventh():
    chord = Chords.half_diminished_seventh('C4')
    _chord_tester(chord, ['C4', 'Eb4', 'Gb4', 'Bb4'])

def test_Chord_minor_seventh_flat_five():
    chord = Chords.minor_seventh_flat_five('C4')
    _chord_tester(chord, ['C4', 'Eb4', 'Gb4', 'Bb4'])

def test_Chord_minor_major_seventh():
    chord = Chords.minor_major_seventh('C4')
    _chord_tester(chord, ['C4', 'Eb4', 'G4', 'B4'])

def test_Chord_minor_sixth():
    chord = Chords.minor_sixth('C4')
    _chord_tester(chord, ['C4', 'Eb4', 'G4', 'Ab4'])

def test_Chord_major_sixth():
    chord = Chords.major_sixth('C4')
    _chord_tester(chord, ['C4', 'E4', 'G4', 'A4'])

def test_Chord_dominant_sixth():
    chord = Chords.dominant_sixth('C4')
    _chord_tester(chord, ['C4', 'E4', 'G4', 'A4', 'Bb4'])

def test_Chord_sixth_ninth():
    chord = Chords.sixth_ninth('C4')
    _chord_tester(chord, ['C4', 'E4', 'G4', 'A4', 'D5'])

def test_Chord_minor_ninth():
    chord = Chords.minor_ninth('C4')
    _chord_tester(chord, ['C4', 'Eb4', 'G4', 'Bb4', 'D5'])

def test_Chord_dominant_ninth():
    chord = Chords.dominant_ninth('C4')
    _chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'D5'])

def test_Chord_dominant_flat_ninth():
    chord = Chords.dominant_flat_ninth('C4')
    _chord_tester(chord, ['C4', 'E4', 'G4', 'Bb4', 'Db5'])

