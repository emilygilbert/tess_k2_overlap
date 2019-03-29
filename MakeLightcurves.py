from __future__ import print_function
import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt
import pandas
print('lk version:',lk.__version__)

# Fetching planet information
planet_info = pandas.read_csv('data/planet_matches.csv')
candidate_info = pandas.read_csv('data/candidate_matches.csv')
combined_info = pandas.concat([planet_info,candidate_info])

def get_star_name(tic):
    """Return the name of a host star based on its TIC ID."""
    tic_index = planet_info.index[planet_info['TIC'] == tic].tolist()
    full_name = planet_info['Planet'][tic_index]
    name = full_name[:-2]
    return name

def get_tic_from_name(name):
    """Return the name of a host star based on its TIC ID."""
    name_index = planet_info.index[planet_info['Planet'] == name].tolist()
    tic = planet_info['TIC'][name_index]
    return tic

def make_lc(tic=None,planet=None,mission='tess',verbose=False):
    """Return a LightCurve object from TESS or K2 planet.

    Keyword arguments:
    Need ONE of:
        tic -- TIC ID # of the planet
        planet -- name of the planet
    mission -- which mission to get the data from (default 'tess')
    verbose -- whether to print status updates (default False)
    """
    if tic == None:
        if planet == None:
            raise ValueError('Must specify either TIC or planet.')
        tic = get_tic_from_name(planet)
    
    if verbose: print('Fetching TPF...')
    tpf = lk.search_targetpixelfile(tic,mission='tess').download()
    
    if mission.lower() == 'tess':
        if verbose: print('De-trending...')
        corrector = lk.PLDCorrector(tpf)
        lc = corrector.correct()
        if verbose: print('Success')
    
    elif mission.lower() == 'k2':
        if verbose: print('De-trending...')
        lc = tpf.to_lightcurve(aperture_mask=tpf.pipeline_mask)
        lc.remove_outliers(sigma=6).flatten()
        if verbose: print('Success')
    
    else:
        raise ValueError('Mission must be \'tess\' or \'k2\'.')
    
    return lc

# For pretty plotting
colors = ['dodgerblue','hotpink','darkmagenta','navy','mediumseagreen']

def test_colors():
    """Test the color scheme."""
    fig, ax = plt.subplots()
    for c in colors:
        x = np.random.uniform(-3, 3, size=20)
        y = np.random.uniform(-3, 3, size=20)
        ax.scatter(x,y,color=c)
    plt.show()

def plot_lc(lc=None,tic=None,planet=None,mission='tess',transit_dict=None,verbose=False):
    """Plot the light curve of a host star with predicted transit overlaid.

    Keyword arguments (must have tic OR planet):
    lc -- LightCurve object
    tic -- TIC ID # of the host star
    planet -- name of the planet
    mission -- which mission to get the data from (default 'tess')
    transit_dict -- predicted transits, of the form {'b':[JD1,JD2]}
    verbose -- whether to print status updates (default False)
    """
    if planet == None:
        if tic:
            title = get_star_name(tic)
    else:
        title = planet[:-2]
    
    if lc == None:
        lc = make_lc(tic=tic,planet=planet,mission=mission,verbose=verbose)

    ax = lc.scatter(s=0.1)
    
    if transit_dict:
        j = 0
        color_index = j % len(colors)
        for p in transit_dict:
            for time in transit_dict[p]:
                plt.axvline(x=time-2457000, color=colors[color_index], alpha=0.5, linewidth = 3)
        j += 1
    
    plt.title(title) 
    plt.savefig(title+'.png')
    plt.show()


