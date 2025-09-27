"""
Predictor 47
Generated on: 2025-09-09 23:21:45
Accuracy: 58.94%
"""


# PREDICTOR 47 - Accuracy: 58.94%
# Correct predictions: 5894/10000 (58.94%)

def predict_output(A, B, C, D, E):
    sum_ac = A + C
    diff_be = B - E
    if (A < 10 and B > 70) or (C < 20 and (D > 60 or E > 70)) or (sum_ac < 30 and diff_be > 40):
        return 4
    elif (B > 85 and C > 75) or (A > 90 and E < 10):
        return 2
    elif (D < 15 and C > 40 and B < 80) or (C < 10 and E < 60) or (A < 50 and D < 25 and E < 20) or (A > 50 and D > 70 and B > 40 and C < 50):
        return 3
    else:
        return 1