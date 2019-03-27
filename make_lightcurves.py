from __future__ import print_function
import lightkurve as lk
import numpy as np
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import matplotlib.pyplot as plt
import pandas
print('lk version:',lk.__version__)


planet_info = pandas.read_csv('data/planetinfo.csv')


def get_timing(tic):
    tic_index = planet_info.index[planet_info['TIC'] == tic].tolist()
    period = planet_info['Period (days)'][tic_index]
    # ref_time = planet_info['Ref time (JD)'][tic_index]
    # return period, ref_time
    return period

def make_lc(tic,mission='tess',verbose=False):
    if verbose: print('Fetching TPF...')
    tpf = lk.search_targetpixelfile(tic,mission='tess').download()
    if mission == 'tess':
        if verbose: print('De-trending...')
        corrector = lk.PLDCorrector(tpf)
        lc = corrector.correct()
        if verbose: print('Success')
    elif mission == 'k2':
        if verbose: print('De-trending...')
        lc = tpf.to_lightcurve(aperture_mask=tpf.pipeline_mask)
        lc.remove_outliers(sigma=6).flatten()
        if verbose: print('Success')
    else:
        raise ValueError('Mission must be \'tess\' or \'k2\'')
    return tic,lc

def fold_lc(tic,lc):
    period = get_timing(tic)
    ref_time = 0
    # period,ref_time = get_timing(tic)
    folded_lc = lc.fold(period,ref_time)
    return folded_lc

colors = ['dodgerblue','hotpink','darkmagenta','navy','mediumseagreen']


def test_colors():
    fig, ax = plt.subplots()
    for c in colors:
        x = np.random.uniform(-3, 3, size=20)
        y = np.random.uniform(-3, 3, size=20)
        ax.scatter(x,y,color=c)
    plt.show()


def plot_lc(lc,title,transit_dict=None):
    # transit dict dict of form: {'b':[JD1,JD2]}
    ax = lc.scatter(s=0.1)
    if transit_dict:
        j = 0
        for planet in transit_dict:
            for time in transit_dict[planet]:
                plt.axvline(x=time-2457000, color=colors[j], alpha=0.5, linewidth = 3)
        j += 1
    plt.title(title) 
    plt.savefig(title+'.png')
    plt.show()


