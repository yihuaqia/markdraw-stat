import pandas as pd
import os
import numpy as np
import json
import sys
sys.path.insert(0,'/c/Users/yihuaqia/work/markdraw_stat/source_code')

def data_gen_xy_canon(technology, func_name):
    data = {}
    df = pd.read_csv(f'{os.getcwd()}/../analysis/{func_name}_analysis/{func_name}_{technology}.csv', index_col=0)
    for i in range(len(df)):
        cv = df.iloc[i]['cv.cvid']
        lpp = df.iloc[i]['lpp.lpp']
        cds = df.iloc[i]['xy_cds.points']
        lengths = df.iloc[i]['xy_lengths.points']
        dist = df.iloc[i]['xy_distance.points']
        step = df.iloc[i]['stepping.list']
        shift = df.iloc[i]['shift.float']
        cell_size = df.iloc[i]['CellSize']
        # categorize the data by lpp
        if lpp not in data:
            data[lpp] = []
        data[lpp].append({'lpp': lpp, 'cell_size': cell_size, 'args': {'cv.cvid':cv, 'lpp.lpp':lpp, 'xy_cds.points': cds, 'xy_lengths.points': lengths, 'xy_distance.points': dist, 'stepping.list': step, 'shift.float': shift}})
    return data


def get_unique_data(data):
    for lpp in data:
        args = set()
        unique_data = []
        for d in data[lpp]:
            if tuple(d['args'].items()) not in args:
                args.add(tuple(d['args'].items()))
                unique_data.append(d)
        data[lpp] = unique_data
    return data

def output_data(data, func_name):
    result = {}
    result[technology] = {}
    result[technology][func_name] = {}
    for lpp in data:
        print(lpp)
        result[technology][func_name][lpp] = {}
        # result[technology] = {func_name: {lpp: {}}}
        result[technology][func_name][lpp]['layer'] = lpp.split('.')[0].upper()
        result[technology][func_name][lpp]['cell_size'] = data[lpp][0]['cell_size']
        # result[technology][func_name][lpp]['args'] = []
        for i,d in enumerate(data[lpp]):
            if not d['args']['shift.float'] > -1:
                # remove NaN with empty string
                d['args']['shift.float'] = ''
            result[technology][func_name][lpp][f'args{i}'] = (d['args'])
        
    return result


if __name__ == '__main__':
    technology = '1227'
    func_list = ['xy_canon']
    print(os.getcwd())

    for func_name in func_list:
        df = pd.read_csv(f'{os.getcwd()}/../analysis/{func_name}_analysis/{func_name}_{technology}.csv', index_col=0)
        data = data_gen_xy_canon(technology, func_name)
        data = get_unique_data(data)
        result = output_data(data, func_name)
        with open(f'TEST_{technology}.json', 'w+') as f:
            json.dump(result, f, indent=4)
    print('done')
