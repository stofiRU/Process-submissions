import os

def parse_submissions(directory):
    # retrieve datafiles with os.walk
    datafiles = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".tcl"): # all data files end with .tcl
                datafiles.append(os.path.join(root, f))
    
    # narrow to accepted files only
    accepted = []
    for d in datafiles:
        with open(d, "r") as f:
            for line in f:
                if 'Accepted' in line:
                    accepted.append(f.name)

    acc = ()
    team = ""
    problem = ""
    submissions = []
    for a in accepted:
        with open(a, "r") as f:
            for line in f:
                # split three important line in three parts by the key phrases below
                # wanted data after phrase
                # create a tuple of the data and add to a list
                if ('Date ' in line):
                    s, d, date = line.partition('Date ')
                if ('Problem ' in line):
                    s, p, problem = line.partition('Problem ')
                if ('Team ' in line):
                    s, t, team = line.partition('Team ')
                    acc = (date.rstrip(), team.rstrip(), problem.rstrip())
                    submissions.append(acc)
    # sort list by date, remove date
    submissions = sorted(submissions)
    datelessSubs = []
    for s in submissions:
        datelessSubs.append((s[1],s[2]))
    return datelessSubs