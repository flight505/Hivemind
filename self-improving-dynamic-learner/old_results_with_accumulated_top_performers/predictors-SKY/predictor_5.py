"""
Predictor 5
Generated on: 2025-09-09 03:38:12
Accuracy: 46.85%
"""


# PREDICTOR 5 - Accuracy: 46.85%
# Correct predictions: 4685/10000 (46.85%)

def predict_output(A, B, C, D, E):
    if C < 25 and E > 70:
        return 4
    elif C < 20:
        if B < 20:
            return 3
        else:
            return 1
    elif C >= 70:
        if A > 50 and D < 50:
            return 1
        elif B < 25:
            return 1
        elif E < 30:
            if A > 50 or B > 60:
                return 4
            elif D > 50:
                return 1
            else:
                return 3
        else:
            if B < 60:
                return 3
            else:
                return 2
    else:
        if C < 40:
            if A > 40 and E > 50:
                return 4
            elif D < 20 and E < 20:
                return 3
            else:
                return 1
        else:
            if E < 15 and A > 40:
                return 4
            elif B > 80 and D > 80 and E > 50:
                return 2
            elif B < 20 or D >= 90 or (A > 70 and B < 40 and E > 70):
                return 3
            else:
                return 1