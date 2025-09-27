"""
Predictor 70
Generated on: 2025-09-09 19:43:32
Accuracy: 56.21%
"""


# PREDICTOR 70 - Accuracy: 56.21%
# Correct predictions: 5621/10000 (56.21%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            if D > 90 and E < 40:
                return 3
            elif A > 60:
                return 1
            else:
                return 2
        else:
            if D < 40:
                return 1
            else:
                return 4
    else:
        if C >= 50:
            if D > 50 or E > 50 or A > 70:
                return 1
            else:
                return 4
        else:
            if E < 20:
                return 1
            elif D < 30:
                if E > 50:
                    if B < 50:
                        return 4
                    else:
                        return 1
                else:
                    return 3
            else:
                if E > 90:
                    return 3
                elif B > 55:
                    return 4
                else:
                    return 3