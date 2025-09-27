"""
Predictor 717
Generated on: 2025-09-09 19:58:25
Accuracy: 51.72%
"""


# PREDICTOR 717 - Accuracy: 51.72%
# Correct predictions: 5172/10000 (51.72%)

def predict_output(A, B, C, D, E):
    if C <= 25:
        if B < 20:
            if E > 80:
                return 4
            return 3
        elif D >= 90:
            return 1
        elif B > 60:
            return 4
        elif E > 60:
            return 4
        else:
            return 3
    if B > 60 and C > 75:
        if A > 40 and D > 75 and E >= 70:
            return 3
        else:
            return 2
    if B < 60 and E < 20:
        return 3
    return 1