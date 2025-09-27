"""
Predictor 226
Generated on: 2025-09-09 21:06:49
Accuracy: 42.86%
"""


# PREDICTOR 226 - Accuracy: 42.86%
# Correct predictions: 4286/10000 (42.86%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C > 50:
            if D < 50:
                return 1
            else:
                return 2
        else:
            if D < 40:
                return 1
            else:
                if A > 60:
                    return 2
                else:
                    return 4
    else:
        if C > 50:
            if A > 50:
                return 1
            else:
                if D < 10:
                    return 3
                else:
                    return 4
        else:
            if E < 20:
                return 1
            else:
                if C > 40:
                    return 1
                elif D < 5:
                    return 2
                else:
                    return 3