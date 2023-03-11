"""Bulk Al(fcc) test"""
from ase import Atoms
from ase.visualize import view
from gpaw import GPAW, PW
import numpy as np
from ase.parallel import paropen
f = paropen('bulk_energy_for_diff_atomic_lengths.csv', mode='w')
for a in list(np.linspace(3.9,4.2,100)):
    name = 'bulk-fcc-%.1f' % a

    b = a / 2

    bulk = Atoms('Al',
                cell=[[0, b, b],
                    [b, 0, b],
                    [b, b, 0]],
                pbc=True)

    #view(bulk)

    k = 4
    calc = GPAW(mode=PW(300),       # cutoff
                kpts=(k, k, k),     # k-points
                txt=name + '.txt')  # output file

    bulk.calc = calc #calculator, 

    energy = bulk.get_potential_energy() # we calculate, the potential energy of the system and write it to a gpaw function
    calc.write(name + '.gpw')
    #print('Energy:', energy, 'eV')

    
    print(f'{a}, {energy}', file=f)