#!/usr/bin/env python3

from fcc_db import get_callsign
print("\nHam and GMRS Callsign Lookup\nWritten by KD9YQK\n")

loop = True

while loop:
  callsign = input("Enter Callsign or (q)uit> ")
  if callsign.lower() in ['q', 'quit']:
    exit (0)
  data = get_callsign(callsign.upper())
  if len(data)< 1:
    print("\nInvalid Callsign\n")
    continue
  line = "\n" + "-" * 55
  print(line)
  for k in data[0].keys():
    line = k
    line += " " * (10 - len(k))
    try:
      d = data[0][k]
      if k == "service":
        if d == "ZA":
          d += " (GMRS)"
        if d == "HA":
          d += " (Ham)"
      line += "| " + d
      line += " " * (20 - len(d))
    except:
      line += "| " + " " * 20
    try:
      d = data[1][k]
      if k == "service":
        if d == "ZA":
          d += " (GMRS)"
        if d == "HA":
          d += " (Ham)"
      line += "| " + d
    except:
      line += "| "
    print(line)
  line = "\n" + "-" * 55 + "\n"
  print(line)
