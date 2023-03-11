# slap from 2 to 20 atoms is perfect for doing this kind of exercise
from ase.visualize import view
from ase.build import fcc100
s = fcc100('Al', (1, 1, 5))
view(s, repeat=(4, 4, 1))