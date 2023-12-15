def calculate_premium(policy_type, coverage, policyholder_age):
    base_premium = 500

    if policy_type == 'health':
        base_premium += 500
    elif policy_type == 'auto':
        base_premium += 5000
    elif policy_type == 'property':
        base_premium += 1000

    if coverage == 'comprehensive':
        base_premium *= 1.5

    if policyholder_age < 30:
        base_premium *= 0.8

    return base_premium
