# web-page: pdos.png
from gpaw import GPAW, restart
import matplotlib.pyplot as plt
# web-page: lcaodos.png
import matplotlib.pyplot as plt
import numpy as np
from ase.io import read
from ase.units import Hartree

from gpaw import GPAW
from gpaw.utilities.dos import RestartLCAODOS, fold



# Density of States
plt.subplot(211)
slab, calc = restart('Ag_gs.gpw') # WE mad platinum slab 
e, dos = calc.get_dos(spin=0, npts=2001, width=0.2)
e_f = calc.get_fermi_level()
plt.plot(e, dos)
plt.axis([0, 25, None, 4])
plt.ylabel('DOS')

plt.subplot(212)

calc = GPAW('Ag_gs.gpw', txt=None)
energy, pdos = calc.get_orbital_ldos(a=0, angular='d') #PDOS here
I = np.trapz(pdos, energy)
center = np.trapz(pdos * energy, energy) / I
width = np.sqrt(np.trapz(pdos * (energy - center)**2, energy) / I)
plt.plot(energy, pdos)

energy, pdos = calc.get_orbital_ldos(a=0, angular='s')
I = np.trapz(pdos, energy)
center = np.trapz(pdos * energy, energy) / I
width = np.sqrt(np.trapz(pdos * (energy - center)**2, energy) / I)
plt.plot(energy, pdos)

energy, pdos = calc.get_orbital_ldos(a=0, angular='p')
I = np.trapz(pdos, energy)
center = np.trapz(pdos * energy, energy) / I
width = np.sqrt(np.trapz(pdos * (energy - center)**2, energy) / I)
plt.plot(energy, pdos)


#plt.xlabel('Energy (eV)')
#plt.ylabel('d-projected DOS on atom 10')
#plt.title('d-band center = %s eV, d-band width = %s eV' % (center, width))
plt.savefig('pdos_au.png')
plt.show()

