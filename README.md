# fcc_db
## FCC Ham and GMRS database creation for local use
At least 500Mb of FREE memory must be available.

### fcc_db.py
The main library.  There are 2 usable functions.
1) build_db() - This downloads the entire FCC database for both Ham and GRMS, then combines into a sqlite3 database and optimizes for searching.  The govt. database is updated every Tues at 10am EST?
2) get_callsign(callsign) - Enter a GMRS or HAM callsign, returns a list of dictionaries of all records found containing the callsigns FRN.

### lookup.py
A sample command line script to lookup callsigns in the database.

### build.sh
A shell script that manages building the database.  It makes a backup of the old database and attempts to build a new database in it's place.  If the process fails, the old database will be returned.
Cleans up all downloaded data files upon completion.

### build_db.py
A python script to facilitate building the database.  If all goes well, it will return an exit(0); otherwise an exit(1) is returned.

