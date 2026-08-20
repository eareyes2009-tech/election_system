from pathlib import Path
from openpyxl import Workbook


def paths_management():

    for directories, filenames in {Path("data/users"): "users.xlsx",
                        Path("data/candidates"): "candidates.xlsx", 
                        Path("data/voters"): "voters.xlsx"}.items():

        directories.mkdir(parents=True, exist_ok=True)    
        excel_management(directories, filenames)

def excel_management(directories, filenames):

    if not (directories/filenames).exists():

        wb = Workbook()
        wb.save(directories/filenames)
        wb.close()