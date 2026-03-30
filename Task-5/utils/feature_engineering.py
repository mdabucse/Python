import pandas as pd

def engineer_features(df):
    new_features = []

    if 'total_spend' in df.columns and 'tenure_months' in df.columns:
        df['avg_monthly_spend'] = df['total_spend'] / (df['tenure_months'] + 1)
        new_features.append('avg_monthly_spend')

    if 'support_ticket_count' in df.columns and 'tenure_months' in df.columns:
        df['support_freq_ratio'] = df['support_ticket_count'] / (df['tenure_months'] + 1)
        new_features.append('support_freq_ratio')

    if 'tenure_months' in df.columns:
        df['tenure_bin'] = pd.cut(df['tenure_months'], bins=5, labels=False)
        new_features.append('tenure_bin')

    print(f"Engineered {len(new_features)} new features ({', '.join(new_features)}...)")

    return df