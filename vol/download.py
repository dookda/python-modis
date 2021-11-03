import os
import subprocess
from auth import earth
from geo.Geoserver import Geoserver

username = earth["user"]
password = earth["pass"]

path = 'lst_terra/'

geo = Geoserver('http://127.0.0.1:8080/geoserver',
                username='admin', password='geoserver')


def warp():
    dir = os.listdir(path)
    for f in dir:
        if f.endswith(".hdf"):
            a = f.split(".")
            # print(a)
            out = f"{a[0]}_{a[1]}_{a[2]}_{a[3]}_{a[4]}"
            cmd = f'modis_convert.py -s "( 1 0 0 0 1 0 0 0 0 0 0 0 )" -o {path}{out} -e 32647  {path}{f}'
            os.system(cmd)
            print("finish warp")


def download():
    print("downloading...")
    # cmd = f"modis_download.py -U {username} -P {password} -I -r -t h18v03,h18v04 -f 2008-01-01 -e 2008-01-31 /mnt/lst_terra/"
    cmd = f"modis_download.py -U {username} -P {password} -r -s MOLA -p MYD11A1.006 -t h27v07 -f 2021-01-01 -e 2021-01-02 {path}"
    # os.system(cmd)
    print("finish download")
    # warp()


if __name__ == '__main__':
    download()
