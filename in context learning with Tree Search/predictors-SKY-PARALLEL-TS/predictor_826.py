"""
Predictor 826
Generated on: 2025-09-10 00:53:24
Accuracy: 51.56%
"""


# PREDICTOR 826 - Accuracy: 51.56%
# Correct predictions: 5156/10000 (51.56%)

def predict_output(A, B, C, D, E):
    sum_ab = A + B
    sum_cd = C + D
    diff_ae = A - E
    avg_be = (B + E) / 2
    if (A < 15 and B > 65) or (C < 20 and D > 70) or (C > 90 and E < 20 and D > 45) or (sum_cd > 140 and avg_be < 30):
        return 4
    elif (sum_ab > 150 and diff_ae > 50) or (B > 80 and C > 85 and E < 10) or (B > 70 and C > 90 and E < 5 and A < 45):
        return 2
    elif (A > 45 and D > 60 and B > 35 and C < 55) or (D < 20 and C > 40 and E < 50) or (C < 15 and E < 65):
        return 3
    else:
        return 1