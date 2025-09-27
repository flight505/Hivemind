"""
Predictor 525
Generated on: 2025-09-10 00:14:11
Accuracy: 57.09%
"""


# PREDICTOR 525 - Accuracy: 57.09%
# Correct predictions: 5709/10000 (57.09%)

def predict_output(A, B, C, D, E):
    sum_abc = A + B + C
    diff_de = D - E
    if ((A < 10 and B > 70) or
        (C < 15 and D > 55) or
        (C < 25 and E > 70) or
        (C > 60 and E < 15 and B < 70) or
        (A > 70 and B < 30 and C > 40 and E < 30) or
        (D > 50 and E > 60 and C < 40) or
        (E > 60 and A < 30 and B < 30 and C < 30) or
        (sum_abc > 100 and diff_de < -50)):
        return 4
    if ((A > 90 and E < 10) or
        (B > 85 and C > 80) or
        (C > 70 and (D < 10 or E < 10) and A < 60)):
        return 2
    if ((A > 50 and C < 50 and D > 70 and B > 40) or
        (A < 50 and D < 25 and E < 20 and B < 80) or
        (D < 15 and C > 40 and B < 80 and A < 70) or
        (C < 10 and E < 60) or
        (D > 80 and E < 10) or
        (A < 40 and B < 30 and C < 30 and D < 30 and E <= 30)):
        return 3
    else:
        return 1