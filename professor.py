# Apply a uniform pressure load
mapdl.nsel("S", "LOC", "Z", 1)
mapdl.d("ALL", "PRES", 1)

# Solve the analysis
mapdl.run("/solu")
mapdl.antype("STATIC")
mapdl.solve()

# Post-processing
mapdl.post1()
mapdl.set(1, 1)
mapdl.post26()

# Extract stress and strain data
num_nodes = mapdl.post_processing.nnum.shape[0]
hydrostatic_stress = np.zeros(num_nodes)
hydrostatic_strain = np.zeros(num_nodes)

for i in range(num_nodes):
    nnum = mapdl.post_processing.nnum[i]
    hydrostatic_stress[i] = mapdl.post_processing.nodal_stress(1, "S", nnum)
    hydrostatic_strain[i] = mapdl.post_processing.nodal_stress(1, "EPTO", nnum)

# Print the hydrostatic stress and strain
for i in range(num_nodes):
    print(f"Node {i+1}: Hydrostatic Stress = {hydrostatic_stress[i]}, Hydrostatic Strain = {hydrostatic_strain[i]}")    