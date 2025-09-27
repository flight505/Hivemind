"""
Predictor 9
Generated on: 2025-09-09 04:09:52
Accuracy: 48.71%
"""


# PREDICTOR 9 - Accuracy: 48.71%
# Correct predictions: 4871/10000 (48.71%)

def predict_output(A, B, C, D, E):
    if A <= 20 and B >= 76 and C >= 95 and D >= 78:
        return 1
    elif E >= 90:
        return 4
    elif B >= 90 and E >= 80:
        return 4
    elif B >= 80 and E <= 30 and D >= 80:
        return 4
    elif B >= 65 and C >= 75:
        return 2
    elif B >= 81 and C <= 30 and E >= 50 and A >= 20:
        return 2
    elif B >= 90 and E <= 50:
        return 3
    elif B <= 15 and C <= 12:
        return 3
    elif C <= 10 and E <= 30 and B <= 70:
        return 3
    elif B >= 30 and B <= 40 and D <= 10:
        return 3
    else:
        return 1