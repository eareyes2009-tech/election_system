from pathlib import Path
from openpyxl import Workbook
import pandas as pd

def paths_management():

    info = pd.DataFrame({"Path": [Path("data/users"), Path("data/candidates"),Path("data/voters")],
                            "File Name": ["users.xlsx","candidates.xlsx","voters.xlsx"],
                            "Cell Names": [["ID", "Nombre", "Contraseña"],
                                        ["ID", "Nombre", "Partido","Casillas"],
                                        ["ID", "Nombre", "Identificacion", "Voto"]]})
    for directories, filenames, cellnames in info.itertuples(index=False):

        directories.mkdir(parents=True, exist_ok=True)    
        excel_management(directories, filenames, cellnames)

def excel_management(directories, filenames, cellnames):

    if not (directories/filenames).exists():

        wb = Workbook()
        ws = wb.active
        ws.append(cellnames)
        wb.save(directories/filenames)
        wb.close()