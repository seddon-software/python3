# Dawn/Data Browsing
#    i22-4996.nxs
#    MoKedge_1_15.nxs
# ... Meta Header Table:    this shows keys/values
# ... Data Analysis/Data:    this shows data sets



import os
import h5py
# fileName = "/dls/i12/epics/scans/data/pco00001.nxs"
# os.chdir("/dls_sw/apps/hdf5/1.10.5/bin")
fileName = "MoKedge_1_15.nxs"
fileName = "i22-4996.nxs"
# os.system("ls");
# cmd = f"h5dump -H {fileName} | more"
# cmd = f"h5dump -H {fileName}"
# os.system(cmd)
f = h5py.File(fileName, "r")
print(list(f.keys()))
ds = f[list(f.keys())[0]]
for group in f:
    print(f[f"/{group}"])
    for subgroup in f[group]:
        print(f[f"/{group}/{subgroup}"])
