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
                    accepted.append(f.name)

    acc = ()
    team = ""
    problem = ""
    submissions = []
    for a in accepted:
        with open(a, "r") as f:
            for line in f:
                if ('Problem ' in line):
                    s, p, problem = line.partition('Problem ')
                if ('Team ' in line):
                    s, t, team = line.partition('Team ')
                    acc = (team.rstrip(), problem.rstrip())
                    submissions.append(acc)
    return submissions

print(parse_submissions('submissions'))