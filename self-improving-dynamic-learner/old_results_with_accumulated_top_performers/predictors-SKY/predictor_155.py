"""
Predictor 155
Generated on: 2025-09-09 06:49:24
Accuracy: 44.85%
"""


# PREDICTOR 155 - Accuracy: 44.85%
# Correct predictions: 4485/10000 (44.85%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15:
        if E > 80:
            return 4
        if B < 20:
            return 3
        elif B > 50:
            if E > 60:
                return 4
            else:
                return 1
        else:
            return 3
    if C > 70:
        if B < 10:
            return 4
        if B > 60 and E > 80:
            return 1
        if C > 50 and B > 60 and D > 70 and E > 80:
            return 1
        if B > 60:
            if A >= 50:
                return 1
            else:
                return 2
        else:
            return 2
    if C < 40:
        if B < 10 and E > 70:
            return 4
        if B < 20 and D < 20 and C < 20 and A > 40:
            return 3
        if D < 10 and E > 80:
            return 2
        if E > 70 and C < 25 and B < 30:
            return 2
        if E > 80 and C < 25 and B > 30 and A > 30:
            return 4
        elif D > 90 and C > 30:
            return 3
        elif B > 70 and C > 30:
            return 2
        elif B > 70 and E > 60 and A > 30:
            return 2
        elif B > 50 and E < 40:
            return 3
        else:
            return 1
    else:
        if C > 50 and B > 60 and D > 70 and E < 50:
            return 1
        if B > 60 and E > 70:
            return 2
        elif D > 70 and B > 40:
            return 3
        else:
            return 1