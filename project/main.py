import pandas as pd

import numpy as np

def get_output_schema():

    return pd.DataFrame({

        'Driver': prep_string(),

        'DriverNumber': prep_int(),

        'LapNumber': prep_int(),

        'Stint': prep_int(),

        'LapTime_Seconds': prep_decimal(),

        'LapTime_Calculated_Seconds': prep_decimal()

    })

def convert_lap_time(df):

    df = df.copy()

    df['LapTime_Calculated_Seconds'] = df['LapTime_Seconds']

    return df[

        [

            'Driver',

            'DriverNumber',

            'LapNumber',

            'Stint',

            'LapTime_Seconds',

            'LapTime_Calculated_Seconds'

        ]

    ]