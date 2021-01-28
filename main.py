import os

import pandas as pd


def get_info_on_year(df: object) -> list:
    """Получаем массив массивов в которых хрянятся статьи разбитые по разделителю"""
    arr = []
    df = df['WoS Categories']
    for i in df:
        arr_mod = []
        for j in i.split('; '):
            arr_mod.append(j.lower())
        arr.append(arr_mod)
    return arr


def to_lower_arr(arr: list) -> list:
    """Функция переводит все к общему регистру"""
    return_arr = []
    for i in arr:
        return_arr.append(i.lower())
    return return_arr


def unique(arr_data, a, b, c, d, e, f, g) -> dict:
    """Функция для получения количества публикаций в определенном критерии за каждый год"""
    def priority(p, arr) -> int:
        """Если находим статью, которая подходит к определенному критерию то возвращаем 1 в противном случае 0"""
        for prior in arr:
            for name in p:
                if name == prior:
                    return 1
        return 0
    a_return = 0
    b_return = 0
    c_return = 0
    d_return = 0
    e_return = 0
    f_return = 0
    g_return = 0
    for i in arr_data:
        a_return += priority(i, a)
        b_return += priority(i, b)
        c_return += priority(i, c)
        d_return += priority(i, d)
        e_return += priority(i, e)
        f_return += priority(i, f)
        g_return += priority(i, g)
    return {"a": a_return, "b": b_return, "c": c_return, "d": d_return, "e": e_return, "f": f_return, "g": g_return}


def main():
    os.chdir('excel/input_wos')
    df_arr_data_year = []
    df_arr_data_priority = []
    for i in os.listdir():
        df_arr_data_year.append(pd.read_excel(i))
    data_2016 = get_info_on_year(df_arr_data_year[0])
    data_2017 = get_info_on_year(df_arr_data_year[1])
    data_2018 = get_info_on_year(df_arr_data_year[2])
    data_2019 = get_info_on_year(df_arr_data_year[3])
    data_2020 = get_info_on_year(df_arr_data_year[4])
    os.chdir('../input_priority')
    for i in os.listdir():
        df_arr_data_priority.append(pd.read_excel(i))
    a_priority = to_lower_arr(df_arr_data_priority[0]['a'].values)
    b_priority = to_lower_arr(df_arr_data_priority[1]['b'].values)
    c_priority = to_lower_arr(df_arr_data_priority[2]['c'].values)
    d_priority = to_lower_arr(df_arr_data_priority[3]['d'].values)
    e_priority = to_lower_arr(df_arr_data_priority[4]['e'].values)
    f_priority = to_lower_arr(df_arr_data_priority[5]['f'].values)
    g_priority = to_lower_arr(df_arr_data_priority[6]['g'].values)

    data_2020 = unique(data_2020, a_priority, b_priority, c_priority, d_priority, e_priority, f_priority,
                       g_priority)
    data_2019 = unique(data_2019, a_priority, b_priority, c_priority, d_priority, e_priority, f_priority,
                       g_priority)
    data_2018 = unique(data_2018, a_priority, b_priority, c_priority, d_priority, e_priority, f_priority,
                       g_priority)
    data_2017 = unique(data_2017, a_priority, b_priority, c_priority, d_priority, e_priority, f_priority,
                       g_priority)
    data_2016 = unique(data_2016, a_priority, b_priority, c_priority, d_priority, e_priority, f_priority,
                       g_priority)
    retsult_dict = {'2016': data_2016, '2017': data_2017, '2018': data_2018, '2019': data_2019, '2020': data_2020}
    os.chdir('../out_wos')
    df = pd.DataFrame(retsult_dict)
    df.to_excel('out_result.xlsx', index=True)
