from pathlib import Path

def paths_management():

    for directories in [Path("data/users"),Path("data/candidates"), Path("data/voters")]:

        directories.mkdir(parents=True, exist_ok=True)    