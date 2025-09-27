"""
Predictor 190
Generated on: 2025-09-09 20:50:39
Accuracy: 46.02%
"""


# PREDICTOR 190 - Accuracy: 46.02%
# Correct predictions: 4602/10000 (46.02%)

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
            elif B + C > 100:
                return 2
            elif A - E > 40:
                return 1
            else:
                return 3