"""
Predictor 310
Generated on: 2025-09-09 21:44:46
Accuracy: 47.73%
"""


# PREDICTOR 310 - Accuracy: 47.73%
# Correct predictions: 4773/10000 (47.73%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            if D < 40:
                return 1
            else:
                return 2
        else:
            if D < 40:
                return 1
            else:
                if E >= 60:
                    return 3
                else:
                    return 4
    else:
        if C >= 50:
            if D >= 50:
                return 1
            else:
                if E > 50:
                    return 1
                elif E > 20:
                    return 3
                else:
                    return 4
        else:
            if E < 20:
                return 1
            elif D < 40:
                if E > 50:
                    return 2
                elif B > 30 and E < 40:
                    return 4
                else:
                    return 3
            else:
                if E > 70 and A < 10:
                    return 1
                else:
                    return 3