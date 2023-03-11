from gpaw import GPAW, PW
from ase import Atoms
from ase.parallel import paropen

for symbol in ['H']:
    a = 8.0
    
    calc = GPAW(h=0.2,mode=PW(350), txt=f'con_test.txt')
    system = Atoms('H2', positions=[[0,0,-1],[0,0,1]])
    system.calc = calc
    system.center(vacuum = 3)
    nums = range(350,700,100)
    f = paropen(f'con_test_ens.txt', 'w')
    for en in nums:
        #h = a / ngridpoints
        #calc.set(h=h)
        calc.set(mode = PW(en))
        energy = system.get_potential_energy()
        print(en, energy, file=f)

    