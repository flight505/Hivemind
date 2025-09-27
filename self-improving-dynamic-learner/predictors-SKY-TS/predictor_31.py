"""
Predictor 31
Generated on: 2025-09-09 19:14:13
Accuracy: 41.95%
"""


# PREDICTOR 31 - Accuracy: 41.95%
# Correct predictions: 4195/10000 (41.95%)

def predict_output(A, B, C, D, E):
    m = max(A, B, C, D, E)
    if m == B:
        if C > 50:
            return 2
        elif max(D, E) > 50:
            return 4
        else:
            if min(A, E) < 15:
                return 3
            else:
                return 1
    elif m == C:
        if D < 30:
            return 4
        else:
            return 1
    elif m == D:
        if B > 80:
            return 4
        elif B < 20:
            return 1
        elif D > 80:
            return 1
        elif C > 40:
            return 1
        else:
            return 3
    elif m == A:
        return 3
    elif m == E:
        if E > 50:
            return 4
        else:
            return 3
    else:
        return 1