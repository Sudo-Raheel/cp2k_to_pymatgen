import numpy as np
from pymatgen.io.common import VolumetricData
from matplotlib import pyplot as plt 
# Assuming you have a structure object already loaded or defined in Pymatgen

chgcar_AB = VolumetricData.from_cube("run-v_hartree-1_0.cube")
grid=np.shape(chgcar_AB.data['total'])
poscar = chgcar_AB.structure  # strucutre of total system 

planar_avg = chgcar_AB.get_average_along_axis(ind=2)  # ind 2 is for 001 direction 
c_latt=poscar.lattice.c

c_arr=np.linspace(0,c_latt,grid[2])
Dis,Pot= np.loadtxt('profile_int_3.dat', unpack=True, dtype = float ,usecols=(0,1))


#plotting 
fig,ax = plt.subplots()
req_size = 18

plt.xticks(fontsize=14) 
plt.yticks(fontsize=14)

ax.plot(Dis, Pot,marker="x", linewidth=1.0,color="black",alpha=1.0,markersize=5,label='cubecruncher')
ax.plot(c_arr,planar_avg,marker="s", linewidth=1.0,color="blue",alpha=1.0,markersize=2,label='pymatgen')
ax.set_xlabel(r"Z-Distance($A^{o}$)",fontsize=15)
# ax.set_xlim([0, 31])
# ax.set_ylim([-1, 0.5])
ax.set_ylabel(r"Potential(Hartree/e)" ,color="black",fontsize=15)
#plt.axvline(x=5.430697500)
plt.legend()
# plt.title(r"TiS2(Dipole=20)",fontsize=22)
plt.savefig('potential_profile.png',bbox_inches='tight')
#plt.show()
