"""
Utitlity methods calculating interquantile statistics
for the survey responses
"""

def calculate_quantiles(values: list[int] = None):
    if values:
        values.sort()
        input_length = len(values)
        q1_idx = int(input_length * 0.25)
        median_idx = int(input_length * 0.5)
        q3_idx = int(input_length * 0.75)
        return values[q1_idx], values[median_idx], values[q3_idx]

    raise ValueError("Empty values")


def determine_position_in_quantiles(response: int, quantiles: tuple):
    quant1, median, quant3 = quantiles
    msg = ""
    if response < quant1:
        msg = "Below 25th percentile"
    elif response < median:
        msg = "25th to 50th percentile"
    elif response < quant3:
        msg = "50th to 75th percentile"
    else:
        msg = "Above 75th percentile"
    return msg
