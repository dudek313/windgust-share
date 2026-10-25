

import pdb
import os
from pathlib import Path


class NcDir(object):

    def __init__(self):

        assert "NETCDF_ROOT" in os.environ
        assert "CASE_PATH" in os.environ

        self.ncroot = Path(os.environ["NETCDF_ROOT"])
        self.caseroot = Path(os.environ["CASE_PATH"])



    def create(self):
        path = self.caseroot / 'deps' / 'netcdf'

        ipath = path / 'include'
        lpath = path / 'lib'
        bpath = path / 'bin'

        ipath.mkdir(exist_ok=True, parents=True)
        lpath.mkdir(exist_ok=True, parents=True)
        bpath.mkdir(exist_ok=True, parents=True)


        indir = self.ncroot / 'include'
        self._create_symlinks(ipath, indir)

        indir = self.ncroot / 'include' / 'Intel'
        self._create_symlinks(ipath, indir)

        indir = self.ncroot / 'lib'
        self._create_symlinks(lpath, indir)

        indir = self.ncroot / 'lib' / 'Intel'
        self._create_symlinks(lpath, indir)

        indir = self.ncroot / 'bin'
        self._create_symlinks(bpath, indir)



    def _create_symlinks(self, outdir, indir):
        files = indir.glob('*')

        for ipath in files:
            if ipath.is_dir():
                print('skipping: ', ipath)
                continue

            opath = outdir / ipath.name
            opath.symlink_to(ipath)

NcDir().create()
