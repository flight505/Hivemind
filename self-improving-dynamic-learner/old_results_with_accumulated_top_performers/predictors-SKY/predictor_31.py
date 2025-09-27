"""
Predictor 31
Generated on: 2025-09-09 04:02:20
Accuracy: 54.59%
"""


# PREDICTOR 31 - Accuracy: 54.59%
# Correct predictions: 5459/10000 (54.59%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40 and C < 30:
        return 4
    if C < 15:
        if E > 60 and A < 20:
            return 2
        else:
            return 3
    if C >= 15 and C < 40:
        if D > 90:
            return 1
        elif E < 20 and A > 50:
            return 3
        elif B > 60 and E > 70 and C < 35:
            return 2
        elif E > 50 and B < 40 and D < 30 and C < 40 and A < 20:
            return 2
        else:
            return 1
    if C > 70:
        if B > 60:
            if A >= 50:
                return 1
            else:
                return 2
        else:
            if D < 30 or E < 30:
                return 4
            else:
                return 1
    # For 40 <= C <= 70
    if B > 60 and D > 90 and E > 80:
        return 3
    elif B > 80 and C < 45:
        return 2
    elif E < 30 and A < 30 and C > 50:
        return 4
    elif A > 80 and B < 20 and D > 70:
        return 3
    else:
        return 1