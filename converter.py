# quick converter for SDR++ bookmark files for use in Portapack
import sys
import json

if len(sys.argv) != 2:
    print("Usage: \"python3 converter.py <filename>\"")
    exit()

try:
    raw_json = open(sys.argv[1], "r")
except:
    print("Could not open {0}".format(sys.argv[1]))
    exit()

try:
    loaded_json = json.load(raw_json)
except:
    print("File not loaded\nPossible bad json")
    exit()

freq_dict = dict()
for entry in loaded_json["bookmarks"]:
    for key,value in (loaded_json["bookmarks"][entry].items()):
        kdmp = json.dumps(key)
        vdmp = json.dumps(value)
        if "frequency" in kdmp:
            # lol
            freq_dict["f=" + (str(int(float(vdmp))))] = ("d=" + entry)

final_dict = '\n'.join(",".join(_) for _ in freq_dict.items())
output_name = (sys.argv[1].split(".",1)[0]).upper() + ".TXT"
try:
    f = open(output_name, "x")
    if (f.write(final_dict)):
        print("Wrote {0}".format( output_name))
except:
    print("Could not write {0}\nCheck if file already exists".format(output_name))
    exit()
