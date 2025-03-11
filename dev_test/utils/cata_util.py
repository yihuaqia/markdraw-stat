import pandas as pd
import os
import numpy as np
import json
from collections import Counter
from collections import OrderedDict
import ast
import sys
sys.path.append(os.path.abspath('../../'))


def load_data(path):
    """ read in excel sheets
        grab all .xlsx files in the dir specified by path """
    files_under_path = os.listdir(path)
    fnames = [f[:-5] for f in files_under_path if f.endswith('.xlsx')]

    all_files = {}
    for i in range(len(fnames)):
        file = pd.read_excel(
            f'{path}/{fnames[i]}.xlsx', sheet_name=None, engine='openpyxl')
        all_files[fnames[i]] = file

    return fnames, all_files


def get_cell_info(file):
    """ get the cell names from the StartLayoutAssembler or zonal_background """
    # df_list = []
    od_df = OrderedDict()
    name_list = []
    for sname in file.keys():
        cell_names = []
        new_cell_idx = []
        df = pd.DataFrame(file[sname])
        # check if the StartLayoutAssembler is in any place in the df
        if 'StartLayoutAssembler' not in df.values and 'zonal_background' not in df.values:
            continue

        # get cell names; i is the row index
        for i in range(df.shape[0]):
            # print(f'{i}: {df.iloc[i,1]}')
            if df.iloc[i, 1] == 'StartLayoutAssembler' or df.iloc[i, 1] == 'zonal_background':
                c_name = df.iloc[i]['CellName.string']

                if c_name not in cell_names:
                    # cell_names.append((c_name,i))
                    cell_names.append(c_name)
                    new_cell_idx.append(i)

        # print(f'{fname}: {cell_names}')
        # slice the cells based on cellnames
        df_cells = {}
        for i in range(len(cell_names)-1):
            df_cells[cell_names[i]] = df.iloc[new_cell_idx[i]
                :new_cell_idx[i+1], :].dropna(how='all')
        df_cells[cell_names[-1]] = df.iloc[new_cell_idx[-1]
            :, :].dropna(how='all')

        # df_list.append(df_cells)
        od_df[sname] = df_cells
        name_list.append(cell_names)
    return od_df, name_list


def get_df_info(technology, file_name, sheet_name, cell_name):
    """ get the cell information from the file """
    in_file_path = f'../../input_sheets/{technology}'
    fnames, all_files = load_data(in_file_path)
    od_df, name_lst = get_cell_info(all_files[file_name])
    return od_df[sheet_name][cell_name]


def get_catalog_seq(cc):
    catalog_seq = {}
    for k in cc.keys():
        catalog_seq[k] = list(cc[k]['CAD_info']['function_sequence'])
    return catalog_seq
