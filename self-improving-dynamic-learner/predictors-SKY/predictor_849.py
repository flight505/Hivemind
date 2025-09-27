"""
Predictor 849
Generated on: 2025-09-09 21:26:57
Accuracy: 46.51%
"""


# PREDICTOR 849 - Accuracy: 46.51%
# Correct predictions: 4651/10000 (46.51%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B < 30 and C > 60:
        return 4
    if B > 60 and C < 30:
        if D > 70:
            if E > 80:
                return 3
            elif E > 50:
                return 1
            else:
                return 4
        else:
            return 4
    if C < 30 and E > 90:
        return 4
    if B > 60 and 30 <= C < 75 and E > 90:
        return 4
    if B > 60 and 40 < C < 60 and E < 10:
        return 4
    if B > 60 and C > 75:
        if D < 20 and E < 50:
            return 1
        elif D > 80 and E > 80:
            return 3
        elif E > 90:
            return 4
        else:
            return 2
    return 1