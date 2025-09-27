"""
Predictor 184
Generated on: 2025-09-09 07:28:50
Accuracy: 57.29%
"""


# PREDICTOR 184 - Accuracy: 57.29%
# Correct predictions: 5729/10000 (57.29%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15:
        if A < 10 and E > 70:
            return 2
        elif D > 80:
            if A > 80:
                return 4
            else:
                return 3
        elif E > 70:
            return 4
        else:
            return 3
    elif C < 40:
        if A < 10 and B > 70:
            return 1
        elif E > 80 and B > 30:
            return 4
        elif A > 80 and D > 80:
            return 4
        elif A > 80:
            return 1
        elif B > 70 and D > 80:
            return 3
        elif B > 70:
            return 2
        else:
            return 1
    elif C < 70:
        if E < 40 and D < 30:
            return 4
        else:
            return 1
    else:
        if B > 60 and A < 50 and D > 90:
            return 3
        elif B > 60 and A < 50:
            return 2
        else:
            return 1