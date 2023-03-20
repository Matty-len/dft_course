from ase.build import fcc100
from ase import Atoms

from gpaw import GPAW, FermiDirac
name = 'Al-fcc'
a = 4.05  # fcc lattice parameter
b = a / 2

bulk = Atoms('Al',
             cell=[[0, b, b],
                   [b, 0, b],
                   [b, b, 0]],
             pbc=True)
atoms.center(vacuum=6.0, axis=2)
name = "ag_lcao"

h = 0.18
kx = 9
ky = 9
kz = 3

calc = GPAW(mode='lcao',
            h=h,
            kpts={'size': (kx, ky, kz), 'gamma': True},
            xc='PBE',
            basis='dzp',
            parallel={'band': 1},
            symmetry='off',
            convergence={'bands': -2},
            maxiter=600,
            txt=None,
            occupations=FermiDirac(width=0.01))

atoms.calc = calc
atoms.get_potential_energy()
calc.write(name + '.gpw')


# it kinda makes ok sense, there is no densities below, but most of the energies are occupied around the d, and some above