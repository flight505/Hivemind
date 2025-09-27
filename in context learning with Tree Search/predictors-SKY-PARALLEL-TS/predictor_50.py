"""
Predictor 50
Generated on: 2025-09-09 23:21:45
Accuracy: 44.74%
"""


# PREDICTOR 50 - Accuracy: 44.74%
# Correct predictions: 4474/10000 (44.74%)

def predict_output(A, B, C, D, E):
    sum_abc = A + B + C
    diff_de = D - E
    if C < 5 and B > 50 and D > 50:
        return 3
    elif (B < 10 and D > 80) or (C > 90 and D > 90) or (A < 5 and C < 10) or (sum_abc < 100 and diff_de > 70):
        return 3
    elif (C > 90 and D < 10) or (B > 70 and C > 80) or (B > 90) or (A > 90 and E < 10):
        return 2
    elif B < 10 and C > 90:
        if A > 60:
            return 4
        else:
            return 2
    elif (A < 10 and B > 70) or (C < 20 and D > 40) or (E < 20 and D > 50 and B < 50) or (B > 60 and E < 20) or (C > 70 and B < 30) or (A + E < 30 and D > 50):
        return 4
    else:
        return 1