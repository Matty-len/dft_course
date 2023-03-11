"""Bulk Al(fcc) test"""
from ase import Atoms
from ase.visualize import view
from gpaw import GPAW, PW
import numpy as np
from ase.parallel import paropen
f = paropen('bulk_energy_for_diff_k.csv', mode='w')
print('k,e',file=f)
for k in [4,6,8,10,12,14,16,18,20]:
    name = f'fcc_all_for_k_{k}'
    a = 4.05 #Å
    b = a / 2

    bulk = Atoms('Al',
                cell=[[0, b, b],
                    [b, 0, b],
                    [b, b, 0]],
                pbc=True)

    #view(bulk)

    #k = 4
    calc = GPAW(mode=PW(300),       # cutoff
                kpts=(k, k, k),     # k-points
                txt=name + '.txt')  # output file

    bulk.calc = calc #calculator, 

    energy = bulk.get_potential_energy() # we calculate, the potential energy of the system and write it to a gpaw function
    calc.write(name + '.gpw')
    #print('Energy:', energy, 'eV')

    
    print(f'{k}, {energy}', file=f)