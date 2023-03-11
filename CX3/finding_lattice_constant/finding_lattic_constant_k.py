import numpy as np
from ase.build import bulk
from gpaw import GPAW, PW
from ase.parallel import paropen

a0 = 4.04
al = bulk('Al', 'fcc', a=a0)
cell0 = al.cell
f = paropen('data_k_mode.csv','w')
for ecut in range(200, 501, 50):
    al.calc = GPAW(mode=PW(ecut),
                   xc='PBE',
                   kpts=(8, 8, 8),
                   basis='dzp',
                   txt=f'Al-{ecut}.txt')
    for eps in np.linspace(-0.02, 0.02, 5):
        al.cell = (1 + eps) * cell0
        al.get_potential_energy()


al.calc.set(mode=PW(400))
E_min = 100
for k in range(4, 17):
    al.calc.set(kpts=(k, k, k),
                txt=f'Al-{k:02}.txt')
    for eps in np.linspace(-0.02, 0.02, 5):
        al.cell = (1 + eps) * cell0
        E = al.get_potential_energy()
        if E < E_min:
            E_min = E
    print(f'{k},{E_min}',file=f)
    