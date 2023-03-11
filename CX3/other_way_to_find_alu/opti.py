from ase.build import bulk
from gpaw import GPAW, PW

# a = 5.421
# si = bulk('Si', 'fcc', a=a)
# # or equivalently:
# # b = a / 2
# # from ase import Atoms
# # si = Atoms('Si2', cell=[[0, b, b], [b, 0, b], [b, b, 0]], pbc=True,
# #           scaled_positions=[[0, 0, 0], [0.25, 0.25, 0.25]])

# for x in [100, 200, 300, 400, 500, 600, 700, 800]:
#     # for x in [0.24, 0.22, 0.20, 0.18, 0.16, 0.14, 0.12, 0.1]:
#     calc = GPAW(mode=PW(x),
#                 # h=x,
#                 xc='PBE',
#                 kpts=(4, 4, 4),
#                 txt=f'convergence_{x}.txt')

#     si.calc = calc

#     print(x, si.get_potential_energy())



    ###################



    # it kinda converges here as well.
# a = 5.421
# si = bulk('Al', 'fcc', a=a)
# conv_lis = []
# for x in [0.24, 0.22, 0.20, 0.18, 0.16, 0.14, 0.12]:
#     calc = GPAW(h=x,
#                 xc='PBE',
#                 kpts=(4, 4, 4),
#                 txt=f'convergence_{x}.txt')

#     si.calc = calc
#     E = si.get_potential_energy()
#     print(x, E)
#     conv_lis.append(E)

# con_lis = []

# for i,val in enumerate(conv_lis):
#     pass
#     if i > 0: 
#         con_lis.append(conv_lis[i] - conv_lis[i-1])
# print(con_lis)
# print(x)


import numpy as np
from ase.build import bulk
from ase.optimize.bfgs import BFGS
from ase.constraints import UnitCellFilter
from gpaw import GPAW
from gpaw import PW

si = bulk('Al', 'fcc', a=6.0)
# Experimental Lattice constant is a=5.421 A

si.calc = GPAW(xc='PBE',
               mode=PW(400, dedecut='estimate'),
               kpts=(4, 4, 4),
               # convergence={'eigenstates': 1.e-10},  # converge tightly!
               txt='stress.txt')

uf = UnitCellFilter(si)
relax = BFGS(uf)
relax.run(fmax=0.05)  # Consider much tighter fmax!

a = np.linalg.norm(si.cell[0]) * 2**0.5
print(f'Relaxed lattice parameter: a = {a} Ang')