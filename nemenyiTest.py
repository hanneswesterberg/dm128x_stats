import pandas as pd
import scikit_posthocs as sp


def nemenyi_test(df):

    # Average the rank per ID-algorithm pair
    mean_ranks = df.groupby(['ID', 'algorithm'])['rank'].mean().reset_index()

    # Pivot to wide format: rows = IDs, columns = algorithms
    pivot_df = mean_ranks.pivot(index='ID', columns='algorithm', values='rank')

    # Drop rows with missing data
    pivot_df = pivot_df.dropna()

    # Run Nemenyi test
    nemenyi_results = sp.posthoc_nemenyi_friedman(pivot_df)

    overall_mean_ranks = pivot_df.mean().sort_values()

    return nemenyi_results, overall_mean_ranks
