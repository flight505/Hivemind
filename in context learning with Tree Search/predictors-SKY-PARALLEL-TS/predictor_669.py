"""
Predictor 669
Generated on: 2025-09-10 00:31:36
Accuracy: 47.85%
"""


# PREDICTOR 669 - Accuracy: 47.85%
# Correct predictions: 4785/10000 (47.85%)

def predict_output(A, B, C, D, E):
    sum_ab = A + B
    diff_de = D - E
    avg_ce = (C + E) / 2
    if (A < 15 and B > 65) or (C < 25 and D > 75) or (diff_de > 50) or (A > 75 and B < 35 and C > 55 and E > 75) or (A > 55 and C > 45 and B < 45 and avg_ce < 40) or (C < 25 and D > 65):
        return 4
    elif (A > 75 and B < 20 and C < 35 and D < 30) or (B > 85 and C > 75 and D > 85 and E < 20) or (A > 65 and B < 25 and C < 15 and D > 55) or (D > 85 and E > 75 and A < 55):
        return 3
    elif (A < 30 and B > 65 and D < 25) or (A > 75 and B > 75 and E < 30) or (sum_ab > 170 and C > 35 and E < 25):
        return 2
    else:
        return 1