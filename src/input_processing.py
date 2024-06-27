def format_model_inputs(input_dict):
    input_fields = ['contract_type', 
        'referrals_category',
        'has_dependents',
        'internet_type',
        'payment_method',
        'tenure_months',
        'total_monthly_fee',
        'total_charges_quarter',
        'married',
        'senior_citizen',
        'city']

    str_fields = ['contract_type', 
        'referrals_category',
        'has_dependents',
        'internet_type',
        'payment_method',
        'married',
        'senior_citizen',
        'city']

    int_fields = [
        'tenure_months',
    ]

    float_fields = [
        'total_charges_quarter',
        'total_monthly_fee',
    ]

    feature_dict = {}

    for c in str_fields:
        if c in input_dict:
            feature_dict[c] = input_dict[c]

    for c in int_fields:
        if c in input_dict:
            feature_dict[c] = int(input_dict[c])

    for c in float_fields:
        if c in input_dict:
            feature_dict[c] = float(input_dict[c])

    return [feature_dict[c] for c in input_fields]


def format_model_inputs_all(input_dict):

    input_fields = ['contract_type',
        'has_device_protection',
        'has_internet_service',
        'has_multiple_lines',
        'has_online_backup',
        'has_online_security',
        'has_phone_service',
        'has_premium_tech_support',
        'has_unlimited_data',
        'internet_type',
        'num_referrals',
        'paperless_billing',
        'payment_method',
        'tenure_months',
        'avg_gb_download_monthly',
        'avg_long_distance_fee_monthly',
        'stream_movie',
        'stream_music',
        'stream_tv',
        'total_charges_quarter',
        'total_long_distance_fee',
        'total_monthly_fee',
        'total_refunds',
        'age',
        'gender',
        'married',
        'num_dependents',
        'senior_citizen',
        'zip_code',
        'area_id',
        'city',
        'latitutde',
        'longitude',
        'population']

    str_fields = ['contract_type',
        'has_device_protection',
        'has_internet_service',
        'has_multiple_lines',
        'has_online_backup',
        'has_online_security',
        'has_phone_service',
        'has_premium_tech_support',
        'has_unlimited_data',
        'internet_type',
        'paperless_billing',
        'payment_method',
        'stream_movie',
        'stream_music',
        'stream_tv',
        'gender',
        'married',
        'senior_citizen',
        'city']

    int_fields = [
        'num_referrals',
        'tenure_months',
        'avg_gb_download_monthly',
        'age',
        'num_dependents',
        'zip_code',
        'area_id',
        'population',
        'status'
    ]

    float_fields = [
        'avg_long_distance_fee_monthly',
        'total_charges_quarter',
        'total_long_distance_fee',
        'total_monthly_fee',
        'total_refunds',
        'latitutde',
        'longitude'
    ]

    feature_dict = {}

    for c in str_fields:
        if c in input_dict:
            feature_dict[c] = input_dict[c]

    for c in int_fields:
        if c in input_dict:
            feature_dict[c] = int(input_dict[c])

    for c in float_fields:
        if c in input_dict:
            feature_dict[c] = float(input_dict[c])

    return [feature_dict[c] for c in input_fields]