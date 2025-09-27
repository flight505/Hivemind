"""
Predictor 183
Generated on: 2025-09-09 07:26:17
Accuracy: 54.53%
"""


# PREDICTOR 183 - Accuracy: 54.53%
# Correct predictions: 5453/10000 (54.53%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15:
        if E > 70:
            if B > 70:
                return 1
            else:
                return 4
        elif D > 80:
            if E > 60:
                return 4
            else:
                if A > 50:
                    return 3
                else:
                    return 1
        else:
            return 3
    elif C < 40:
        if E > 80 and B > 30:
            return 4
        elif A > 80 and D > 60:
            return 4
        elif B > 70:
            return 2
        elif D < 10 and E < 30:
            return 3
        else:
            return 1
    elif C > 70:
        if B > 60:
            if A >= 50:
                return 1
            else:
                return 2
        elif B < 20 and E < 20:
            return 4
        else:
            return 1
    else:
        if B > 60 and E > 70:
            return 2
        elif D > 70 and B > 40:
            return 3
        else:
            return 1