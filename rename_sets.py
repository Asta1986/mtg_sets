# Script to rename mtg xlhq files and folders according to the conventions used by the program Forge.
# Requires Python 3.5 and a user with read/write permission to the target directory.

import os
import re

def rename_files(xlhq_dir_path):
    for file in os.listdir(xlhq_dir_path):
        ofp = xlhq_dir_path + os.sep + file
        new_name = re.sub('\.xlhq\.', '.full.', file)
        new_name = re.sub('Aether', 'AEther', new_name)
        new_name = re.sub('Aerathi', 'AErathi', new_name)
        new_name = re.sub('\[#]\.', '#.', new_name)
        nfp = xlhq_dir_path + os.sep + new_name
        os.rename(ofp, nfp)

if __name__ == '__main__':

    dest_path = input("Please enter the full path to the xlhq cards folder\n"
                          "(including last separator '/' or '\\')\n and press 'enter': ")

    local_dirs = os.listdir(dest_path)

    diff_dirs = [('9ED', '9E'), ('ARN', 'AN'), ('VIS', 'VI'), ('8ED', '8E'), ('MIR', 'MI'),
                 ('NMS', 'NE'), ('STH', 'SH'), ('SCG', 'SC'), ('5DN', 'FD'), ('ONS', 'ON'), ('MRD', 'MR'),
                 ('FEM', 'FE'), ('ATQ', 'AQ'), ('V10', 'FVR'), ('ODY', 'OD'), ('PTK', 'P3'), ('APC', 'AP'),
                 ('S99', 'ST'), ('ULG', 'UL'), ('JUD', 'JU'), ('V09', 'FVE'), ('DST', 'DS'), ('USG', 'US'),
                 ('6ED', '6E'), ('LGN', 'LE'), ('POR', 'PT'), ('CON', 'CFX'), ('5ED', '5E'), ('PLS', 'PS'),
                 ('3ED', 'R'), ('4ED', '4E'), ('LEG', 'LG'), ('CMD', 'COM'), ('ICE', 'IA'), ('V11', 'FVL'),
                 ('S00', 'S2K'), ('HML', 'HL'), ('ALL', 'AL'), ('H09', 'PDS'), ('TOR', 'TO'), ('LEA', 'A'),
                 ('7ED', '7E'), ('TMP', 'TE'), ('CHR', 'CH'), ('UDS', 'UD'), ('GPT', 'GP'), ('PO2', 'P2'),
                 ('2ED', 'U'), ('PCY', 'PY'), ('LEB', 'B'), ('CSP', 'CS'), ('EXO', 'EX'), ('INV', 'IN'),
                 ('WTH', 'WL'), ('VGD', 'VAN'), ('DRK', 'DK'), ('MMQ', 'MM')]

    eq_dirs = ['10E', 'M10', 'M11', 'M12', 'M13', 'M14', 'M15', 'ORI', 'CHK', 'BOK', 'SOK', 'RAV', 'DIS',
               'TSP', 'TSB', 'PLC', 'FUT', 'LRW', 'MOR', 'SHM', 'EVE', 'ALA', 'ARB', 'ZEN', 'WWK', 'ROE', 'SOM',
               'MBS', 'NPH', 'ISD', 'DKA', 'AVR', 'RTR', 'GTC', 'DGM', 'THS', 'BNG', 'JOU', 'KTK', 'FRF', 'DTK',
               'BFZ', 'ARC', 'MMA', 'MM2', 'EVG', 'DD2', 'DDC', 'DDD', 'DDE', 'DDF', 'DDG', 'DDH', 'DDI', 'DDJ',
               'DDK', 'DDL', 'DDM', 'DDN', 'DDO', 'DRB', 'V12', 'V13', 'V14', 'V15', 'PD2', 'PD3', 'HOP', 'PC2',
               'CM1', 'C13', 'C14', 'CNS', 'VMA', 'TPR']

    for dir in diff_dirs:
        wp = dest_path + dir[0]
        if (dir[0] in local_dirs) and (os.path.isdir(wp)):
            dp = dest_path + dir[1]
            os.rename(wp, dp)
            rename_files(dp)

    for dir in eq_dirs:
        dp = dest_path + dir
        if (dir in local_dirs) and (os.path.isdir(dp)):
            rename_files(dp)

    print("All done. Renaming complete.")

