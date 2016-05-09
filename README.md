# chordinate

## getKey.py
gets proper scale degrees for major keys according to user input

## generateCadential.py
generates chord tones for a cadential 6/4 (not including resolution to I chord), the most used cadential chord progression in classical music

## fullyDiminishedSevenths.py
generates fully diminished seventh chords (currently in root position) and checks if user input matches resolution to I chord 

## chord.py
chord class

## theory.py
main 

## todo
- document better/more
- function to resolve V7 chords
- function to generate secondary dominant chords
- add information about fully diminished seventh chords
- ~~function to generate and resolve fully diminished seventh chords~~
- improve generation of seventh chords maybe? i.e. inversions, viio7 as applied chord
- ~~it would be nice if you could spell certain keys enharmonically i.e. either F# or Gb major~~

## things learned/mistakes made
- currentKey wasn't cleared before each new key - pitches of each new key were simply appended, resulting in incorrect chord generation
- fully diminished seventh chords in minor were not being built off the leading tone
- parsing strings is difficult when you keep re-capitalizing/enharmonically spelling things
- originially unnecessarily tested if key had sharps in getLeadingTone