import argparse

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import patheffects

import os
import mp_api
from mp_api.client import MPRester
from dotenv import load_dotenv

load_dotenv () # use python-dotenv library for storing secrets in a .env file in project route (or at another path that is specified here)


def dos_from_mp_id(mp_id):
    """return density of states evaluated at particular frequencies (in THz).
    Material is identified using unique ID number. Note that to use this feature you need a Materials
    Project API key (https://materialsproject.org/api)."""

    with MPRester(os.getenv('MP_API_KEY')) as mpr:
        try:
            dos = mpr.get_phonon_dos_by_material_id(mp_id)
        except:
            print("this materials project entry does not appear to have phonon data")
            pass
    freqs = dos.to_pmg.frequencies
    dos = dos.to_pmg.densities

    return freqs, dos

def get_chemical_formula(mp_id):
    """return string containing chemical formula"""

    with MPRester(os.getenv('MP_API_KEY')) as mpr:
        try:
            material_entry = mpr.materials.summary.search(material_ids=mp_id)
        except:
            print("this materials project entry does not seem to exist")
            pass  
    chemical_formulae = material_entry[0].formula_pretty

    return chemical_formulae

def main(mp_id):
    """return plt object which has dos data plotted in xkcd style"""

    freq, dos = dos_from_mp_id(mp_id)

    plt.xkcd()
    mpl.rcParams['path.effects'] = [patheffects.withStroke(linewidth=0)]
    plt.plot(freq, dos)
    plt.xlabel("Frequency (THz)")
    plt.ylabel("Density of States")
    plt.title(get_chemical_formula(mp_id))
    plt.tight_layout()

    return plt.savefig("./static/dos.png",dpi=250,transparent=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot DOS")
    parser.add_argument("mp_ids", nargs='+', help="Materials Project IDs")

    args = parser.parse_args()
    main(args)
