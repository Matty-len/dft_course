# Refer to G. Kresse, Phys. Rev. B 73, 045112 (2006)
# for comparison of macroscopic and microscopic dielectric constant
# and absorption peaks.
from pathlib import Path

from ase.build import bulk
from ase.parallel import paropen, world

from gpaw import GPAW, FermiDirac
from gpaw.response.df import DielectricFunction

# Ground state calculation
a = 5.431
atoms = bulk('Si', 'diamond', a=a)

calc = GPAW(mode='pw',
            kpts={'density': 5.0, 'gamma': True},
            parallel={'band': 1, 'domain': 1},
            xc='LDA',
            occupations=FermiDirac(0.001))  # use small FD smearing

atoms.calc = calc
atoms.get_potential_energy()  # get ground state density

# Restart Calculation with fixed density and dense kpoint sampling
calc = calc.fixed_density(
    kpts={'density': 15.0, 'gamma': False})  # dense kpoint sampling

calc.diagonalize_full_hamiltonian(nbands=70)  # diagonalize Hamiltonian
calc.write('si_large.gpw', 'all')  # write wavefunctions