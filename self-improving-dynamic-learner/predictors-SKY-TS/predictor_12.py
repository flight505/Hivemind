"""
Predictor 12
Generated on: 2025-09-09 19:00:54
Accuracy: 50.74%
"""


# PREDICTOR 12 - Accuracy: 50.74%
# Correct predictions: 5074/10000 (50.74%)

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
            if D < 50:
                return 1
            else:
                if E > 70:
                    return 3
                else:
                    return 2
    else:
        if C > 50:
            if E < 20:
                if D > 50 or A > 50:
                    return 1
                else:
                    return 4
            else:
                if D < 20:
                    return 3
                elif B >= 70:
                    return 2
                else:
                    return 1
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 4
            else:
                if E > 45 and D < 40:
                    return 4
                elif D > 90 or E > 90:
                    return 4
                elif A > 40 and D < 50:
                    return 1
                else:
                    return 3