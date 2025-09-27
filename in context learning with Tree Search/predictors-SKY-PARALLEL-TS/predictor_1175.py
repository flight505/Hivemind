"""
Predictor 1175
Generated on: 2025-09-10 01:39:40
Accuracy: 49.51%
"""


# PREDICTOR 1175 - Accuracy: 49.51%
# Correct predictions: 4951/10000 (49.51%)

def predict_output(A, B, C, D, E):
    sum_abe = A + B + E
    diff_cd = C - D
    if (A < 15 and B > 65) or (C < 25 and D > 85 and E > 75) or (B > 65 and E > 75 and A < 40):
        return 4
    elif (B > 75 and C < 55) or (A > 75 and B > 65 and C < 55) or (sum_abe > 200 and diff_cd < -20):
        return 2
    elif (A > 65 and B < 45 and D > 75) or (A < 15 and B > 55 and D < 20 and C < 30) or (C < 25 and E < 15 and B > 25) or (sum_abe < 100 and diff_cd > 30):
        return 3
    else:
        return 1