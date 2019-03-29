### A brief guide to CSVs

'crossmatch_[]' files: K2 sources with TESS 2 minute cadence data in sectors 1-7.

* [crossmatch_all.csv](crossmatch_all.csv) = targets <= 16 KepMag, i.e. intersection of [short_cad_all.csv](short_cad_all.csv) and [overlap_trimmed.csv](overlap_trimmed.csv) (312 targets).

* [crossmatch_candidates.csv](crossmatch_candidates.csv) = unconfirmed K2 planet candidates, i.e. intersection of [short_cad_all.csv](short_cad_all.csv) and [overlap_candidates.csv](overlap_candidates.csv) (34 targets).

* [crossmatch_planets.csv](crossmatch_planets.csv) = confirmed K2 planets, i.e. intersection of [short_cad_all.csv](short_cad_all.csv) and [overlap_planets.csv](overlap_planets.csv) (26 targets).

'overlap_[]' files: K2 sources in the TESS FOV, courtesy of Dr. Jessie Dotson at NASA Ames. Contain K2 EPIC IDs, RA, Dec, KepMag, TESS sector, basic stellar/planetary parameters (differs slightly between files).

* [overlap_all.csv](overlap_all.csv) = all overlapping targets, courtesy of Dr. Knicole Colon at NASA Goddard (57,395 targets).

* [overlap_bright.csv](overlap_bright.csv) = stars brighter than 10 KepMag (1476 targets)

* [overlap_candidates.csv](overlap_candidates.csv) = unconfirmed K2 planet candidates (132 targets)

* [overlap_K2sc.csv](overlap_K2sc.csv) = stars with 1 minute cadence in K2 (201 targets).

* [overlap_planets.csv](overlap_planets.csv) = confirmed K2 planets (50 targets).

* [overlap_stars.csv](overlap_stars.csv) = stars with stellar parameter info (55,236 targets).

* [overlap_trimmed.csv](overlap_trimmed.csv) = [overlap_all.csv](overlap_all.csv), but only <= 16 KepMag and TESS sectors 1-7.

* [overlap_trimmed_K2.csv](overlap_trimmed_K2.csv) = [overlap_trimmed.csv](overlap_trimmed.csv), but converted to TIC IDs and with no other info.

TESS short cadence targets

* [TESS_short_cad.csv](TESS_short_cad.csv) = all 72,947 targets with TESS 2 minute cadence data in sectors 1-7, courtesy of Dr. David Martin at the University of Chicago by [scraping MAST](http://archive.stsci.edu/tess/bulk_downloads/bulk_downloads_ffi-tp-lc-dv.html). Only TIC IDs.

'times_[]' files: observation periods for K2 campaigns and TESS sectors in Gregorian, Julian, and modified dates.

* [times_K2.csv](times_K2.csv) = K2 campaigns

* [times_TESS.csv](times_TESS.csv) = TESS sectors

