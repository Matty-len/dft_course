from ase.units import Hartree
from gpaw import GPAW
from gpaw.utilities.dos import fold
import pickle
import matplotlib.pyplot as plt

e_f = GPAW('top.gpw').get_fermi_level()

e_n, P_n = pickle.load(open('top.pickle', 'rb')) # reads the pickle file with energy and projections
for n in range(2, 7):
    e, ldos = fold(e_n[n] * Hartree, P_n[n], npts=2001, width=0.2) #fold? maybe some kind 
    plt.plot(e - e_f, ldos, label='Band: ' + str(n))
plt.legend()
plt.axis([-15, 10, None, None])
plt.xlabel('Energy [eV]')
plt.ylabel('PDOS')
plt.savefig('p2fig.png')
plt.show()
