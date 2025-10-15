# fcc_db
FCC Ham and GMRS database creation for local use

There are 2 usable functions.
1) build_db() - This downloads the entire FCC database for both Ham and GRMS, then combines into a sqlite3 database and optimizes for searching.  The govt. database is updated every Tues at 10am EST?
2) get_callsign(callsign) - Enter a GMRS or HAM callsign, returns a list of dictionaries of all records found containing the callsigns FRN.


A 300M swapfile and about 300M of FREE Ram are required!
To increase the swap file on a Raspberry Pi, first turn off the current swap with the command `sudo dphys-swapfile swapoff`. Then, edit the configuration file at `/etc/dphys-swapfile`, change the CONF_SWAPSIZE value to your desired size in megabytes, save the file, and run `sudo dphys-swapfile setup` followed by `sudo dphys-swapfile swapon` to apply the changes.
