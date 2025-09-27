"""
Predictor 197
Generated on: 2025-09-09 20:55:47
Accuracy: 50.47%
"""


# PREDICTOR 197 - Accuracy: 50.47%
# Correct predictions: 5047/10000 (50.47%)

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
                if A > 50:
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