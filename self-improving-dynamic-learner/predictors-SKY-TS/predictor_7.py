"""
Predictor 7
Generated on: 2025-09-09 18:58:34
Accuracy: 50.28%
"""


# PREDICTOR 7 - Accuracy: 50.28%
# Correct predictions: 5028/10000 (50.28%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if E < 20 or E > 50:
                    return 4
                else:
                    return 2
        else:
            if D >= 50:
                return 2
            else:
                return 1
    else:
        if C > 50:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 4
            else:
                if D < 20:
                    return 3
                else:
                    return 1
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 4
            else:
                if D > 90 or E > 90:
                    return 4
                elif A > 80 and D < 50:
                    return 1
                else:
                    return 3