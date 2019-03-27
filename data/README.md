### A brief guide to CSVs

* [wtv-all-unique-targets.csv](wtv-all-unique-targets.csv) contains the list of all K2 targets to be subsequently observed with TESS in any sector, courtesy of Dr. Knicole Colon at NASA Goddard.

* [K2cut.csv](K2cut.csv) is the subset of [wtv-all-unique-targets.csv](wtv-all-unique-targets.csv) that have been observed at the time of creation of this file (through sector 7) and below 16th mag.

* [K2TICs.csv](K2TICs.csv) is equivalent to [K2cut.csv](K2cut.csv), but is the list of corresponding TIC IDs.

* [shortCadenceTargetList.csv](shortCadenceTargetList.csv) contains the list of all TESS targets observed with two-minute cadence data through sector 7, courtesy of Dr. David Martin at the University of Chicago.

* [overlapplanets.csv](overlapplanets.csv) contains the list of all confirmed K2 planets to be subsequently observed with TESS in any sector, courtesy of Dr. Jessie Dotson at NASA Ames.

* [matches.csv](matches.csv) is the intersection of[K2cut.csv](K2cut.csv) and [shortCadenceTargetList.csv](shortCadenceTargetList.csv), i.e. the list of K2 targets subsequently observed by TESS with two-minute cadence data through sector 7 and below 16th mag.

* [planetmatches.csv](planetmatches.csv) is the intersection of[overlapplanets.csv](overlapplanets.csv) and [shortCadenceTargetList.csv](shortCadenceTargetList.csv), i.e. the list of confirmed K2 planets subsequently observed by TESS with two-minute cadence data through sector 7.

* [planetinfo.csv](planetinfo.csv) is an expanded version of [planetmatches.csv](planetmatches.csv) which also contains the sector observed, RA and Dec of the host star, planet name, and planet orbital period. This is a working document.