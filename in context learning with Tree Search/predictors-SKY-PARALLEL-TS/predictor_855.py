"""
Predictor 855
Generated on: 2025-09-10 00:55:50
Accuracy: 52.47%
"""


# PREDICTOR 855 - Accuracy: 52.47%
# Correct predictions: 5247/10000 (52.47%)

def predict_output(A, B, C, D, E):
    sum_abc = A + B + C
    diff_de = D - E
    if (A < 15 and B > 65) or (C < 15 and D > 85) or (A > 75 and C < 30 and D > 75) or (C > 60 and D > 70 and E < 10) or (A > 85 and E > 85 and D < 35) or (A > 40 and C > 45 and D < 35 and E < 15) or (A > 55 and C > 70 and D < 20):
        return 4
    elif (B > 85 and C < 30 and D > 80 and E > 75) or (A > 65 and B > 55 and C < 50 and D > 45 and E > 45) or (sum_abc > 150 and diff_de < -50):
        return 2
    elif (40 < A < 60 and C > 45 and D > 50 and E < 20) or (A < 15 and B > 35 and C < 25 and D < 35 and E > 35) or (A < 20 and B < 15 and C > 25 and D < 35 and E > 35) or (A > 45 and C < 55 and D > 65 and B > 35):
        return 3
    else:
        return 1