
# coding: utf-8

# In[ ]:


"""
Thanks to Christina Hedges for the NEXSCI data retrieval function
"""


import pandas as pd
import numpy as np

def retrieve_online_data():
    ''' Obtain a dataframe from NExScI of all planet data and store it in the
    package data directory.
    '''
    NEXSCI_API = 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI'
    try:
        planets = pd.read_csv(NEXSCI_API + '?table=planets&select=pl_hostname,pl_letter,'
                'pl_disc,ra,dec,pl_trandep,pl_tranmid,pl_tranmiderr1,pl_tranmiderr2,'
                'pl_tranflag,pl_trandur,pl_pnum,pl_k2flag,pl_kepflag,pl_facility,'
                'pl_orbincl,pl_orbinclerr1,pl_orbinclerr2,pl_orblper,st_mass,st_masserr1,'
                'st_masserr2,st_rad,st_raderr1,st_raderr2,st_teff,st_tefferr1,'
                'st_tefferr2,st_optmag,st_j,st_h', comment='#')
        composite = pd.read_csv(NEXSCI_API + '?table=compositepars&select=fpl_hostname,'
                    'fpl_letter,fpl_smax,fpl_smaxerr1,fpl_smaxerr2,fpl_radj,fpl_radjerr1,'
                    'fpl_radjerr2,fpl_bmassj,fpl_bmassjerr1,fpl_bmassjerr2,fpl_eqt,'
                    'fpl_orbper,fpl_orbpererr1,fpl_orbpererr2,fpl_eccen,'
                    'fpl_eccenerr1,fpl_eccenerr2, ', comment='#')
        composite.columns = ['pl_hostname', 'pl_letter', 'pl_orbsmax', 'pl_orbsmaxerr1',
                             'pl_orbsmaxerr2', 'pl_radj', 'pl_radjerr1', 'pl_radjerr2',
                             'pl_bmassj', 'pl_bmassjerr1', 'pl_bmassjerr2', 'pl_eqt',
                             'pl_orbper', 'pl_orbpererr1', 'pl_orbpererr2', 'pl_eccen',
                             'pl_eccenerr1', 'pl_eccenerr2']
    except:
        raise OnlineRetrievalFailure("Couldn't obtain data from NExScI. Do you have an internet connection?")
    df = pd.merge(left=planets, right=composite, how='left', left_on=['pl_hostname', 'pl_letter'],
         right_on=['pl_hostname', 'pl_letter'])
    return df[df.pl_tranflag == 1]
    
df = retrieve_online_data()
df.to_csv('nexsci_output.csv')

def get_number_of_planets(hostname):
    n = np.asarray(df.loc[df.pl_hostname == hostname][['pl_pnum']])[0]
    return n

def get_planet_params(hostname, planet_letter='b'):
    period, t0, dur, depth = np.asarray(df.loc[df.pl_hostname == hostname][['pl_orbper', 'pl_tranmid', 
                                                                     'pl_trandur', 'pl_trandep']])[0]

    return period, t0, dur, depth

