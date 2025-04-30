import pandas as pd
from scipy.stats import friedmanchisquare


def friedman_per_condition(df, groupby_vars):

    results = []

    grouped = df.groupby(groupby_vars)
    for group_vals, group_df in grouped:

        pivot = group_df.pivot(index='ID', columns='algorithm', values='rank')

        if pivot.isnull().any().any() or len(pivot) < 2:
            continue

        stat, p = friedmanchisquare(*[pivot[col] for col in pivot.columns])

        if not isinstance(group_vals, tuple):
            group_vals = (group_vals,)
        result = dict(zip(groupby_vars, group_vals))
        result.update({'stat': stat, 'p': p})
        results.append(result)

    return pd.DataFrame(results)


def friedman_per_audio(df):

    results = {}

    for audio_type in df['audio'].unique():
        sub_df = df[df['audio'] == audio_type]

        # Average over repeated entries (e.g., different playback speeds)
        avg_df = sub_df.groupby(['ID', 'algorithm'], as_index=False)['rank'].mean()

        # Now pivot should work
        pivot = avg_df.pivot(index='ID', columns='algorithm', values='rank')

        if pivot.isnull().any().any() or len(pivot) < 2:
            results[audio_type] = {'stat': None, 'p': None, 'note': 'Insufficient data'}
            continue

        stat, p = friedmanchisquare(*[pivot[col] for col in pivot.columns])
        results[audio_type] = {'stat': stat, 'p': p}

    return results

