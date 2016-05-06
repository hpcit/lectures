import numpy as np

a = np.dtype([('symb','|S3'),('PA',np.int),('x',np.float64),('y',np.float64),('z',np.float64)])

b = np.loadtxt('mol.xyz', dtype=a)

Ixx = (b['PA']*(b['y']**2 + b['z']**2)).sum()
Iyy = (b['PA']*(b['x']**2 + b['z']**2)).sum()
Izz = (b['PA']*(b['x']**2 + b['y']**2)).sum()
Ixy = - (b['PA']* b['x'] * b['y']).sum()
Ixz = - (b['PA']* b['x'] * b['z']).sum()
Iyz = - (b['PA']* b['y'] * b['z']).sum()

mTI = np.matrix([[Ixx,Ixy,Ixz],[Ixy,Iyy,Iyz],[Ixz,Iyz,Izz]])

e, Ev = np.linalg.eigh(mTI)

Ev.T * mTI * Ev

coord = np.array([b['x'],b['y'],b['z']])
coord = coord.transpose()
coord = np.matrix(coord)
new_coord = coord * Ev

gg = np.array([ b['symb'], b['PA']])

new_mol = np.hstack([gg.transpose(),new_coord])

np.savetxt('n_mol.xyz',new_mol, fmt=('%s', '%s', '%s', '%s', '%s'))
