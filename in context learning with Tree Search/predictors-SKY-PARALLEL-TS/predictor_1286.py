"""
Predictor 1286
Generated on: 2025-09-10 01:58:17
Accuracy: 31.58%
"""


# PREDICTOR 1286 - Accuracy: 31.58%
# Correct predictions: 3158/10000 (31.58%)

def predict_output(A, B, C, D, E):
    sum_abc = A + B + C
    diff_de = D - E
    avg_all = (A + B + C + D + E) / 5
    if (A * B > 500 and diff_de < -50) or (C / D > 2 and E < 20):
        return 4
    elif (sum_abc > 200 and avg_all < 40) or (B > E and D < A):
        return 2
    elif (A + E < B + D and C > 50):
        return 3
    else:
        return 1