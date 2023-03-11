from gpaw import GPAW
from ase.build import fcc100
from ase.parallel import paropen

def energy(N, k, a=4.05):
    fcc = fcc100('Al', (1, 1, N), a=a, vacuum=7.5)
    fcc.center(axis=2)
    calc = GPAW(nbands=N * 3,
                kpts=(k, k, 1),
                h=0.25,
                txt='Al_slab_%d.txt' % N)
    fcc.calc = calc
    e = fcc.get_potential_energy()
    calc.write('slab_%d.gpw' % N)
    return e
# the function energy, takes a k, and and N, and make N sized slap bands with k points,  and make a gpaw file with the slab N size


f = paropen('al_energy_surface_tension','w')

k = 12
print('N,e')
for N in [3,4,5,6,7,8]:
    e = energy(N, k)
    print(f'{N,e}',file=f)

f.close()