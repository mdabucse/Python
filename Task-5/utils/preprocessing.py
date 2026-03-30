def handle_missing_values(df):
    missing_info = {}

    if 'billing_amount' in df.columns:
        pct = df['billing_amount'].isna().mean() * 100
        df['billing_amount'] = df['billing_amount'].fillna(df['billing_amount'].median())
        missing_info['billing_amount'] = round(pct, 1)

    if 'last_login_days_ago' in df.columns:
        pct = df['last_login_days_ago'].isna().mean() * 100
        df['last_login_days_ago'] = df['last_login_days_ago'].fillna(df['last_login_days_ago'].median())
        missing_info['last_login_days_ago'] = round(pct, 1)

    msg = ", ".join([f"{col} ({pct}%)" for col, pct in missing_info.items()])
    print(f"Missing values filled: {msg}")

    return df