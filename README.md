# fcc_db
## FCC Ham and GMRS database creation for local use

There are 2 usable functions.
1) build_db() - This downloads the entire FCC database for both Ham and GRMS, then combines into a sqlite3 database and optimizes for searching.  The govt. database is updated every Tues at 10am EST?
2) get_callsign(callsign) - Enter a GMRS or HAM callsign, returns a list of dictionaries of all records found containing the callsigns FRN.


At least 500Mb of FREE memory must be available.
