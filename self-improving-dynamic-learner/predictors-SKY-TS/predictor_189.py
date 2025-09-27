"""
Predictor 189
Generated on: 2025-09-09 20:50:39
Accuracy: 46.52%
"""


# PREDICTOR 189 - Accuracy: 46.52%
# Correct predictions: 4652/10000 (46.52%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if A < 30:
                    return 1
                else:
                    return 4
        else:
            if E < 20:
                return 1
            elif D < 30:
                return 4
            elif D > 80:
                return 1
            else:
                return 2
    else:
        if C >= 50:
            if D < 50:
                if A > 50:
                    return 3
                else:
                    return 4
            else:
                return 1
        else:
            if E > 70:
                if B < 50:
                    return 4
                else:
                    return 2
            elif B > 60 and C > 40:
                return 2
            elif A > 50 and E < 50:
                return 1
            else:
                return 3