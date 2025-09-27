"""
Predictor 242
Generated on: 2025-09-09 10:52:26
Accuracy: 55.61%
"""


# PREDICTOR 242 - Accuracy: 55.61%
# Correct predictions: 5561/10000 (55.61%)

def predict_output(A, B, C, D, E):
    if C < 15:
        return 3
    if C < 25 and E > 90:
        return 4
    if 40 <= C < 70:
        if C < 50 and D > 70:
            return 3
        elif E < 30 and A < 30:
            return 4
        else:
            return 1
    if C >= 70:
        if B > 60:
            if A >= 50:
                return 1
            else:
                return 2
        elif D > 80:
            return 1
        elif D < 20 and C > 70:
            return 4
        else:
            return 1
    return 1