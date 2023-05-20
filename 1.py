import os
import tempfile

from ansys.dpf import core as dpf
from ansys.dpf.core import Model
import matplotlib.pyplot as plt
import numpy as np

from ansys.mapdl import core as pymapdl

# Start MAPDL as a service
mapdl = pymapdl.launch_mapdl()
distance = 59.98 / 2 / np.cos(30 * np.pi / 180)
total_depth = 34
cylinder_rad = 12
cylinder_depth = 6
small_cylinder_rad = 8
height = 10
cone_depth = 12
cone_rad1 = 8
cone_rad2 = 7
small_height = 3
small_block_depth = 30
mapdl.clear()
mapdl.prep7()

mapdl.et(1, 186)
mapdl.et(2, 154)
mapdl.r(1)
mapdl.r(2)

# Aluminum properties (or something)
mapdl.mp("ex", 1, 10e6)
mapdl.mp("nuxy", 1, 0.3)
mapdl.mp("dens", 1, 0.1 / 386.1)
mapdl.mp("dens", 2, 0)

mapdl.k(npt=1, x=-distance*np.sin(30*np.pi/180) + height/2*np.cos(30*np.pi/180), y=distance*np.cos(30*np.pi/180) + height / 2*np.sin(30*np.pi/180), z=0)
mapdl.k(npt=2, x=-distance*np.sin(30*np.pi/180) - height/2*np.cos(30*np.pi/180), y=distance*np.cos(30*np.pi/180) - height/2*np.sin(30*np.pi/180), z=0)
mapdl.k(npt=3, x=-height/2*np.cos(30*np.pi/180), y=-(height/2)*np.sin(30*np.pi/180), z=0)
mapdl.k(npt=4, x=height/2*np.cos(30*np.pi/180), y=height/2*np.sin(30*np.pi/180), z=0)
mapdl.k(npt=5, x=-distance*np.sin(30*np.pi/180) + height/2*np.cos(30*np.pi/180), y=distance*np.cos(30*np.pi/180) + height/2*np.sin(30*np.pi/180), z=cylinder_depth)
mapdl.k(npt=6, x=-distance*np.sin(30*np.pi/180) - height/2*np.cos(30*np.pi/180), y=distance*np.cos(30*np.pi/180) - height/2*np.sin(30*np.pi/180), z=cylinder_depth)
mapdl.k(npt=7, x=-height/2*np.cos(30*np.pi/180), y=-(height/2)*np.sin(30*np.pi/180), z=cylinder_depth)
mapdl.k(npt=8, x=height/2*np.cos(30*np.pi/180), y=height/2*np.sin(30*np.pi/180), z=cylinder_depth)
mapdl.v(1, 2, 3, 4, 5, 6, 7, 8)

mapdl.k(npt=9, x=-distance*np.sin(30*np.pi/180) + height/2*np.cos(30*np.pi/180), y=-distance*np.cos(30*np.pi/180) - height/2*np.sin(30*np.pi/180), z=0)
mapdl.k(npt=10, x=-distance*np.sin(30*np.pi/180) - height/2*np.cos(30*np.pi/180), y=-distance*np.cos(30*np.pi/180) + height/2*np.sin(30*np.pi/180), z=0)
mapdl.k(npt=11, x=-height/2*np.cos(30*np.pi/180), y=height/2*np.sin(30*np.pi/180), z=0)
mapdl.k(npt=12, x=height/2*np.cos(30*np.pi/180), y=-height/2*np.sin(30*np.pi/180), z=0)
mapdl.k(npt=13, x=-distance*np.sin(30*np.pi/180) + height/2*np.cos(30*np.pi/180), y=-distance*np.cos(30*np.pi/180) - height/2*np.sin(30*np.pi/180), z=cylinder_depth)
mapdl.k(npt=14, x=-distance*np.sin(30*np.pi/180) - height/2*np.cos(30*np.pi/180), y=-distance*np.cos(30*np.pi/180) + height/2*np.sin(30*np.pi/180), z=cylinder_depth)
mapdl.k(npt=15, x=-height/2*np.cos(30*np.pi/180), y=height/2*np.sin(30*np.pi/180), z=cylinder_depth)
mapdl.k(npt=16, x=height/2*np.cos(30*np.pi/180), y=-(height/2)*np.sin(30*np.pi/180), z=cylinder_depth)
mapdl.v(9, 10, 11, 12, 13, 14, 15, 16)

mapdl.k(npt=17, x=0, y=small_height/2, z=small_block_depth)
mapdl.k(npt=18, x=0, y=-(small_height/2), z=small_block_depth)
mapdl.k(npt=19, x=distance, y=-(small_height/2), z=small_block_depth)
mapdl.k(npt=20, x=distance, y=small_height/2, z=small_block_depth)
mapdl.k(npt=21, x=0, y=small_height/2, z=small_height+small_block_depth)
mapdl.k(npt=22, x=0, y=-(small_height/2), z=small_height+small_block_depth)
mapdl.k(npt=23, x=distance, y=-(small_height/2), z=small_height+small_block_depth)
mapdl.k(npt=24, x=distance, y=small_height/2, z=small_height+small_block_depth)
mapdl.v(17, 18, 19, 20, 21, 22, 23, 24)

mapdl.k(npt=25, x=-distance*np.sin(30*np.pi/180) + small_height/2*np.cos(30*np.pi/180), y=-distance*np.cos(30*np.pi/180) - small_height / 2*np.sin(30*np.pi/180), z=small_block_depth)
mapdl.k(npt=26, x=-distance*np.sin(30*np.pi/180) - small_height/2*np.cos(30*np.pi/180), y=-distance*np.cos(30*np.pi/180) + small_height/2*np.sin(30*np.pi/180), z=small_block_depth)
mapdl.k(npt=27, x=-small_height/2*np.cos(30*np.pi/180), y=(small_height/2)*np.sin(30*np.pi/180), z=small_block_depth)
mapdl.k(npt=28, x=small_height/2*np.cos(30*np.pi/180), y=-small_height/2*np.sin(30*np.pi/180), z=small_block_depth)
mapdl.k(npt=29, x=-distance*np.sin(30*np.pi/180) + small_height/2*np.cos(30*np.pi/180), y=-distance*np.cos(30*np.pi/180) - small_height/2*np.sin(30*np.pi/180), z=small_height+small_block_depth)
mapdl.k(npt=30, x=-distance*np.sin(30*np.pi/180) - small_height/2*np.cos(30*np.pi/180), y=-distance*np.cos(30*np.pi/180) + small_height/2*np.sin(30*np.pi/180), z=small_height+small_block_depth)
mapdl.k(npt=31, x=-small_height/2*np.cos(30*np.pi/180), y=(small_height/2)*np.sin(30*np.pi/180), z=small_height+small_block_depth)
mapdl.k(npt=32, x=small_height/2*np.cos(30*np.pi/180), y=-small_height/2*np.sin(30*np.pi/180), z=small_height+small_block_depth)
mapdl.v(25, 26, 27, 28, 29, 30, 31, 32)

mapdl.k(npt=33, x=-distance*np.sin(30*np.pi/180) + small_height/2*np.cos(30*np.pi/180), y=distance*np.cos(30*np.pi/180) + small_height / 2*np.sin(30*np.pi/180), z=small_block_depth)
mapdl.k(npt=34, x=-distance*np.sin(30*np.pi/180) - small_height/2*np.cos(30*np.pi/180), y=distance*np.cos(30*np.pi/180) - small_height/2*np.sin(30*np.pi/180), z=small_block_depth)
mapdl.k(npt=35, x=-small_height/2*np.cos(30*np.pi/180), y=-(small_height/2)*np.sin(30*np.pi/180), z=small_block_depth)
mapdl.k(npt=36, x=small_height/2*np.cos(30*np.pi/180), y=small_height/2*np.sin(30*np.pi/180), z=small_block_depth)
mapdl.k(npt=37, x=-distance*np.sin(30*np.pi/180) + small_height/2*np.cos(30*np.pi/180), y=distance*np.cos(30*np.pi/180) + small_height/2*np.sin(30*np.pi/180), z=small_height+small_block_depth)
mapdl.k(npt=38, x=-distance*np.sin(30*np.pi/180) - small_height/2*np.cos(30*np.pi/180), y=distance*np.cos(30*np.pi/180) - small_height/2*np.sin(30*np.pi/180), z=small_height+small_block_depth)
mapdl.k(npt=39, x=-small_height/2*np.cos(30*np.pi/180), y=-(small_height/2)*np.sin(30*np.pi/180), z=small_height+small_block_depth)
mapdl.k(npt=40, x=small_height/2*np.cos(30*np.pi/180), y=small_height/2*np.sin(30*np.pi/180), z=small_height+small_block_depth)
mapdl.v(33, 34, 35, 36, 37, 38, 39, 40)

anum0 = mapdl.cyl4(xcenter=0, ycenter=0, rad1=0, theta1=0, rad2=small_cylinder_rad, theta2=360, depth=cylinder_depth)
anum1 = mapdl.cyl4(xcenter=distance, ycenter=0, rad1=0, theta1=0, rad2=cylinder_rad, theta2=360, depth=cylinder_depth)
anum2 = mapdl.cyl4(xcenter=-distance*np.sin(30*np.pi/180), ycenter=distance*np.cos(30*np.pi/180), rad1=0, theta1=0, rad2=cylinder_rad, theta2=360, depth=cylinder_depth)
anum3 = mapdl.cyl4(xcenter=-distance*np.sin(30*np.pi/180), ycenter=-distance*np.cos(30*np.pi/180), rad1=0, theta1=0, rad2=cylinder_rad, theta2=360, depth=cylinder_depth)

con0 = mapdl.con4(xcenter=0, ycenter=0, rad1=cone_rad1, rad2=cone_rad2, depth=cone_depth+cylinder_depth)
con1 = mapdl.con4(xcenter=distance, ycenter=0, rad1=cone_rad1, rad2=cone_rad2, depth=cone_depth+cylinder_depth)
con2 = mapdl.con4(xcenter=-distance*np.sin(30*np.pi/180), ycenter=distance*np.cos(30*np.pi/180), rad1=cone_rad1, rad2=cone_rad2, depth=cone_depth+cylinder_depth)
con3 = mapdl.con4(xcenter=-distance*np.sin(30*np.pi/180), ycenter=-distance*np.cos(30*np.pi/180), rad1=cone_rad1, rad2=cone_rad2, depth=cone_depth+cylinder_depth)

bnum0 = mapdl.cyl4(xcenter=0, ycenter=0, rad1=0, theta1=0, rad2=cone_rad2, theta2=360, depth=total_depth)
bnum1 = mapdl.cyl4(xcenter=distance, ycenter=0, rad1=0, theta1=0, rad2=cone_rad2, theta2=360, depth=total_depth)
bnum2 = mapdl.cyl4(xcenter=-distance*np.sin(30*np.pi/180), ycenter=distance*np.cos(30*np.pi/180), rad1=0, theta1=0, rad2=cone_rad2, theta2=360, depth=total_depth)
bnum3 = mapdl.cyl4(xcenter=-distance*np.sin(30*np.pi/180), ycenter=-distance*np.cos(30*np.pi/180), rad1=0, theta1=0, rad2=cone_rad2, theta2=360, depth=total_depth)

block0 = mapdl.blc5(xcenter=distance/2, ycenter=0, width=distance, height=height, depth=cylinder_depth)
# block1 = mapdl.blc5(xcenter=distance/2, ycenter=0, width=distance, height=1.5, depth=1)
# block2 = mapdl.blc5(xcenter=distance/2, ycenter=0, width=distance, height=1.5, depth=1)
mapdl.nummrg("KP")
mapdl.aplot()

mapdl.esize(0.5)
mapdl.amesh("all")
mapdl.aplot()

mapdl.allsel(mute=True)
mapdl.run("/SOLU")
mapdl.antype("STATIC")
mapdl.solve()
mapdl.finish(mute=True)

result = mapdl.result
#nnum, stress = result.nodal_stress(0)
#element_stress, elemnum, enode = result.element_stress(0)
#nodenum, stress = result.nodal_stress(0)

# plot interactively
result.plot_nodal_solution(0, cmap="bwr")
#result.plot_nodal_stress(0, "Sx", cmap="bwr")
result.plot_principal_nodal_stress(0, "SEQV", cmap="bwr")
cpos = [
    (20.992831318277517, 9.78629316586435, 31.905115108541928),
    (0.35955395443745797, -1.4198191001571547, 10.346158032932495),
    (-0.10547549888485548, 0.9200673323892437, -0.377294345312956),
]

result.plot_nodal_displacement(0, cpos=cpos)
