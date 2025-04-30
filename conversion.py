import pandas as pd


def convert_to_long(df):

    df_long = pd.melt(df, id_vars=["ID"], var_name="question", value_name="rank")
    df_long[['audio', 'playback_speed', 'algorithm']] = df_long['question']\
        .str.extract(r'([A-Za-z]+)_(\d+\.\d+)_([A-Za-z]+)')
    df_long.drop(columns=['question'], inplace=True)
    df_long = df_long[['ID', 'audio', 'playback_speed', 'algorithm', 'rank']]
    df_long.to_csv("reshaped_file.csv", index=False)

    return df_long


def prepare_long_df(input_csv_path, id_col='ID'):
    # 1) Read wide CSV
    df = pd.read_csv(input_csv_path)

    # 2) Identify the 64 rank columns
    rank_cols = [c for c in df.columns if c != id_col]

    # 3) Melt to long: one row per subject×rank_col
    long = df.melt(id_vars=[id_col],
                   value_vars=rank_cols,
                   var_name='condition_algo',
                   value_name='rank')

    # 4) Parse 'condition_algo' into audio, speed, and algorithm.
    #    This depends on how your columns are named; for example 'audio1_speed2_alg3'.
    #    Adjust the split logic to match your actual naming convention.
    parts = long['condition_algo'].str.split('_', expand=True)
    long['audio'] = parts[0]  # e.g. 'audio1'
    long['playback_speed'] = parts[1]  # e.g. 'speed2'
    long['algorithm'] = parts[2]  # e.g. 'alg3'

    return long
