# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# The Hartree equations for two electrons in one dimension

# <headingcell level=3>

# This script solves the Hartree equations for two interacting electrons in 
# a one-dimensional infinite potential well. The strength of the
# electron-electron interaction can by tuned by the parameter 'gamma'.

# <codecell>

import numpy as np
from scipy import linalg as LA
import scipy.sparse as sp
import matplotlib.pyplot as plt
# <codecell>

hbar = 1   # Plancks constant
m = 1      # electron mass
L = 0.5      # Length of potential well
xmin=-0.1  # minimum x-coordinate
xmax=L+0.1 # maximim x-coordinate
Vinf = 1e9 # value of (external) potential outside the well

gamma = 1e4  # Scaling of electron-electron interaction [ we use 1/|x-x'| --> V_delta*delta(x-x') ]

mixer = 0.5
dx = 0.001 # discretization in x

# <codecell>

x=np.arange(xmin,xmax,dx)
nx = len(x)
vext=0*x  # External potential
n1=np.where(x<0)
n2=np.where(x>L)
vext[n1]=Vinf
vext[n2]=Vinf
Vext=np.diag(vext) # External potential as a matrix (operator)

# <codecell>

T=np.eye(nx) # Kinetic energy operator
for i in range(nx-1):
    T[i,i+1]=-0.5
    T[i+1,i]=-0.5
T = T/(dx**2)*hbar**2/m

# <codecell>

H = T + Vext   # Non-interacting Hamiltonian

# <codecell>

En,Psi0 =LA.eigh(H,eigvals=(0,5))

# <codecell>

plt.plot(Psi0[:,4])

# <headingcell level=3>

# Start of Hartree part

# <codecell>

count = 1
psi_diff = 100
tol = 1e-3  # convergence criterion for the difference in wave functions

# <codecell>

psi1 = Psi0[:,0]
psi2 = Psi0[:,1]

# <codecell>

#while (count<100) and (psi_diff>tol):
n1 = abs(psi1**2)
n2 = abs(psi2**2)

# Setup effective potential for electron '1' and '2'
v1 = n2*gamma     
V1 = np.diag(v1)

v2 = n1*gamma  
V2 = np.diag(v2)

# New hamiltonians for '1' and '2'
H1 = T+Vext+V1
H2 = T+Vext+V2

e1,Psi1 = LA.eigh(H1,eigvals=(0,5))
e2,Psi2 = LA.eigh(H2,eigvals=(0,5))
e1=e1[0]
psi1_new=Psi1[:,0]
e2=e2[0]
psi2_new=Psi2[:,0]

psi_diff1 = sum(abs(abs(psi1)-abs(psi1_new)))
psi_diff2 = sum(abs(abs(psi2)-abs(psi2_new)))
psi_diff = max(psi_diff1,psi_diff2)
count = count+1    

psi1 = psi1*(1-mixer) + psi1_new*mixer
psi2 = psi2*(1-mixer) + psi2_new*mixer
psi1 = psi1/norm(psi1)
psi2 = psi2/norm(psi2)
plot(psi1,'r',psi2,'g')

