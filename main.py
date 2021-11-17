
'''
Name: Ang Kah Shin
Class: DAAA/FT/2B/04
Admin: P2004176
'''
# Writing program 

from Morse import Morse

morse1 = Morse()
encoded = morse1.encode("SOS Our sHiP NEEds HeLP")
print(encoded)

print(morse1.decode(encoded))
