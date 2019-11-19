import os
import h5py
fileName = "/dls/i12/epics/scans/data/pco00001.nxs"
os.chdir("/dls_sw/apps/hdf5/1.10.5/bin")
# os.system("ls");
cmd = f"h5dump -H {fileName} | more"
cmd = f"h5dump -H {fileName}"
os.system(cmd)
f = h5py.File(fileName, "r")
print(list(f.keys()))
ds = f[list(f.keys())[0]]
print(type(ds))
for group in f:
    print(f[f"/{group}"])
    for subgroup in f[group]:
        print(type(subgroup))
        print(f[f"/{group}/{subgroup}"])
        for item in f[f"/{group}/{subgroup}"]:
            print(f[f"/{group}/{subgroup}/{item}"])
            for z in f[f"/{group}/{subgroup}/{item}"]:
                print(f[f"/{group}/{subgroup}/{item}/{z}"])
