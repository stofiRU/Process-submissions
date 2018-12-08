import os

def parse_submissions(directory):
    datafiles = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".tcl"):
                datafiles.append(os.path.join(root, f))

    accepted = []
    for d in datafiles:
        with open(d, "r") as f:
            for line in f:
                if 'Accepted' in line:
                    accepted.append(f)
    return accepted

print(parse_submissions('submissions'))