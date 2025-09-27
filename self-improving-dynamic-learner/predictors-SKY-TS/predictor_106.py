"""
Predictor 106
Generated on: 2025-09-09 20:03:05
Accuracy: 52.68%
"""


# PREDICTOR 106 - Accuracy: 52.68%
# Correct predictions: 5268/10000 (52.68%)

def predict_output(A, B, C, D, E):
    if C > 50:
        if B < 50:
            if E < 20:
                return 4
            else:
                return 1
        else:
            if B > 80:
                return 2
            else:
                return 1
    else:
        if B >= 70:
            if D < 40:
                return 1
            else:
                if E < 20 and D > 90 and C > 30:
                    return 3
                elif A < 20 and E > 50:
                    return 1
                else:
                    return 4
        else:
            if E < 20:
                return 1
            elif E >= 60:
                if A > 90 and C > 25:
                    return 3
                else:
                    return 1
            else:
                return 3