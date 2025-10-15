#!/bin/bash

echo "Backing up database"
mv callsign.sqlite3 callsign.sqlite3.old
python build.py
exit_status=$?
echo $exit_status
if [ $exit_status -eq 0 ]; then
  rm callsign.sqlite3.old
else
  echo "Failed to create DB.  Reverting to backup."
  rm callsign.sqlite3
  mv callsign.sqlite3.old callsign.sqlite3
fi
echo "Deleting downloaded files"
cd data
rm -r *

