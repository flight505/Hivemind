"""
Predictor 81
Generated on: 2025-09-09 04:47:38
Accuracy: 53.72%
"""


# PREDICTOR 81 - Accuracy: 53.72%
# Correct predictions: 5372/10000 (53.72%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40 and C < 30:
        return 4
    if C < 15:
        if B < 40 and E > 60:
            return 2
        else:
            return 3
    if C >= 70:
        if B > 60:
            if A >= 50:
                return 1
            else:
                return 2
        else:
            if D < 30 and E > 50:
                return 4
            elif E < 30:
                return 4
            else:
                return 1
    if C < 40:
        if B > 60 and E > 70:
            return 2
        if D > 80 and E < 20 and B > 40:
            return 3
        if A < 20 and B < 40 and E > 50:
            return 2
        else:
            return 1
    # 40 <= C < 70
    if E < 30 and A < 50 and C > 50:
        return 4
    if A > 80 and D > 70 and E < 40:
        return 3
    if B > 60:
        if E > 80:
            if B > 70 and D > 90:
                return 3
            else:
                return 1
        if E < 20:
            if A > 80:
                return 2
            else:
                return 1
        if A > 70 and C < 50:
            return 2
        if B > 70 and D > 90 and A < 60:
            return 3
        elif D < 20:
            return 1
        else:
            return 1
    else:
        return 1