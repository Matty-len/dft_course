from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonons
from ase.io.trajectory import Trajectory
from ase.io import write
from ase import Atoms
import numpy as np
# Setup crystal and EMT calculator
#atoms = bulk('Al', 'fcc', a=4.05)
a = 1.42  # approximate lattice constant
b = 2.46
#b = a / 2
#print(float(a)*np.cos(120.0*np.deg2rad))
atoms = Atoms('C2',
           cell=[(b, 0, 0), (b*np.cos(2/3*np.pi), b*np.sin(2/3*np.pi), 0), (0, 0, 10)],
           pbc=1,
           calculator=EMT(), positions=[[0,0,0], [0,a,0]])

atoms.write('c6.traj')

# Phonon calculator
N = 3
ph = Phonons(atoms, EMT(), supercell=(N, N, 1), delta=0.05)
ph.run()

# Read forces and assemble the dynamical matrix
ph.read(acoustic=True)
ph.clean()

path = atoms.cell.bandpath('GMKG', npoints=100)
bs = ph.get_band_structure(path)

dos = ph.get_dos(kpts=(20, 20, 20)).sample_grid(npts=100, width=1e-3)

# Plot the band structure and DOS:
import matplotlib.pyplot as plt  # noqa
fig = plt.figure(1, figsize=(7, 4))
ax = fig.add_axes([.12, .07, .67, .85])

emax = 0.035
bs.plot(ax=ax, emin=0.0, emax=emax)

dosax = fig.add_axes([.8, .07, .17, .85])
dosax.fill_between(dos.get_weights(), dos.get_energies(), y2=0, color='grey',
                   edgecolor='k', lw=1)

dosax.set_ylim(0, emax)
dosax.set_yticks([])
dosax.set_xticks([])
dosax.set_xlabel("DOS", fontsize=18)

fig.savefig('C6_phonon.png')


L = path.special_points['L']
ph.write_modes([l / 2 for l in L], branches=[2], repeat=(8, 8, 8), kT=3e-4,
               center=True)


with Trajectory('phonon.mode.2.traj', 'r') as traj:
    write('C6_mode.gif', traj, interval=50,
          rotation='-36x,26.5y,-25z')