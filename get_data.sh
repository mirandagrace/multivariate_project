#!/bin/bash

ftp -d -i -o 'data_files/' ftp://ftp.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/ <<ftpEOF
mget StormEvents_*.csv.gz
quit
ftpEOF