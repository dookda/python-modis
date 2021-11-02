import os
import subprocess
from auth import earth


username = earth["user"]
password = earth["pass"]

print("downloading...")
# cmd = f"modis_download.py -U {username} -P {password} -I -r -t h18v03,h18v04 -f 2008-01-01 -e 2008-01-31 /mnt/lst_terra/"
cmd = f"modis_download.py -U {username} -P {password} -r -s MOLA -p MYD09A1.006 -t h27v07 -f 2010-01-01 -e 2010-12-31 lst_aqua/"
# os.system(cmd)

dir = os.listdir('lst_terra/')
for f in dir:
    # print(f)
    if f.endswith(".hdf"):
        a = f.split(".")
        # print(a)
        outtrans = f"{a[0]}_{a[1]}_{a[2]}_{a[3]}_{a[4]}_trans.tif"
        cmd = f"gdal_translate -sds lst_terra/{f} {out}"
        os.system(cmd)
        print(cmd)

        outwarp = f"{a[0]}_{a[1]}_{a[2]}_{a[3]}_{a[4]}_warp.tif"
        cmd = f"gdalwarp - overwrite {outtrans} {outwarp} - t_srs EPSG: 32647"
        os.system(cmd)

print("ok")
