"""
Predictor 61
Generated on: 2025-09-09 04:27:27
Accuracy: 53.14%
"""


# PREDICTOR 61 - Accuracy: 53.14%
# Correct predictions: 5314/10000 (53.14%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C >= 70:
        if B > 60:
            if A >= 50:
                return 1
            else:
                return 2
        else:
            if D < 30 and E > 50:
                return 4
            elif C > 80 and E < 30 and A < 90:
                return 4
            else:
                return 1
    if C < 15:
        if B > 50 and D > 80 and E < 20:
            return 4
        elif E > 60:
            return 2
        else:
            return 3
    elif C < 25:
        return 1
    else:  # 25 <= C < 70
        if B > 60 and D > 90 and E > 80:
            return 3
        elif B > 60 and E > 70 and C < 40:
            return 2
        elif D > 80 and E < 20:
            return 3
        elif E < 30 and A < 30 and C > 50:
            return 4
        elif A > 80 and E < 40:
            return 3
        elif B > 80 and E < 20:
            return 2
        elif C < 40 and B > 30 and E > 50 and A < 20:
            return 2
        else:
            return 1