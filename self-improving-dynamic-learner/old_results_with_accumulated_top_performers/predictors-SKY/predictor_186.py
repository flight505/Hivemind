"""
Predictor 186
Generated on: 2025-09-09 07:33:09
Accuracy: 48.27%
"""


# PREDICTOR 186 - Accuracy: 48.27%
# Correct predictions: 4827/10000 (48.27%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15:
        if A < 10 and E > 50:
            return 2
        elif B > 70:
            return 1
        elif D > 80 and B < 20:
            return 3
        elif A > 90:
            return 1
        elif E > 50:
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
        elif B > 80:
            return 2
        elif C < 25 and E > 70 and B > 20 and D > 60:
            return 4
        elif D > 50 and E < 10:
            return 3
        elif A > 50 and D < 10:
            return 3
        elif B > 40 and E < 10:
            return 3
        else:
            return 1
    elif C < 70:
        if C > 50:
            return 4
        if E < 40 and D < 30:
            return 4
        elif B > 90:
            return 2
        elif A > 60 and D < 10:
            return 3
        else:
            return 1
    else:
        if B > 60 and A < 50 and D > 90:
            return 3
        elif B > 60 and A < 50:
            if B > 80 or C > 70:
                return 4
            return 2
        else:
            return 1