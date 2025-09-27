"""
Predictor 219
Generated on: 2025-09-09 21:03:09
Accuracy: 47.21%
"""


# PREDICTOR 219 - Accuracy: 47.21%
# Correct predictions: 4721/10000 (47.21%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40 and E < 20:
                return 1
            else:
                return 4
        else:
            if A < 10:
                return 1
            elif D < 50:
                return 4
            else:
                return 2
    else:
        if C >= 50:
            if D + E > 70:
                return 1
            else:
                return 4
        else:
            if E < 20:
                if A > 60:
                    return 1
                elif B >= 60:
                    return 4
                else:
                    return 3
            else:
                if B >= 70:
                    return 4
                elif C > 40:
                    return 4
                elif A < 20:
                    return 1
                else:
                    return 3