from ase.build import fcc111, add_adsorbate
from gpaw import GPAW, PW

#  Slab with PT so we can adsorb:
slab = fcc111('Ag', size=(1, 1, 3))

slab.center(axis=2, vacuum=4.0)
slab.calc = GPAW(mode=PW(400),
                 xc='RPBE',
                 kpts=(12, 12, 1),
                 convergence={'bands': -10},
                 txt='top.txt')
slab.get_potential_energy()
slab.calc.write('top.gpw', mode='all')

