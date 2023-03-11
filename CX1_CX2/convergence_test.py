from gpaw import GPAW
from ase import Atoms
from ase.parallel import paropen
for symbol in ['H']:
    a = 8.0
    
    calc = GPAW(h=1, txt=f'conv_test.txt')
    system = Atoms('H2', positions=[[0,0,-1],[0,0,1]])
    system.calc = calc
    system.center(vacuum = 3)
    nums = range(10,50,2)
    f = paropen(f'conv_test_points.txt', 'w')
    for ngridpoints in nums:
        h = a / ngridpoints
        calc.set(h=h)
        energy = system.get_potential_energy()
        print(h, energy, file=f)

    