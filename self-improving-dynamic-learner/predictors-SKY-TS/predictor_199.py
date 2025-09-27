"""
Predictor 199
Generated on: 2025-09-09 20:55:47
Accuracy: 50.90%
"""


# PREDICTOR 199 - Accuracy: 50.90%
# Correct predictions: 5090/10000 (50.90%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                return 4
        else:
            if E < 40:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if E < 20:
                if A + B > 100:
                    return 1
                else:
                    return 4
            else:
                return 1
        else:
            if D < 40:
                return 3
            else:
                if B < 20:
                    return 1
                elif E < 10:
                    return 3
                elif E > 80:
                    return 2
                else:
                    if E < 35:
                        return 4
                    else:
                        return 3