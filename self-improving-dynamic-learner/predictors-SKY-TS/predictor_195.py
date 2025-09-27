"""
Predictor 195
Generated on: 2025-09-09 20:54:12
Accuracy: 51.70%
"""


# PREDICTOR 195 - Accuracy: 51.70%
# Correct predictions: 5170/10000 (51.70%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if E > 70:
                    return 1
                else:
                    return 4
        else:
            if E < 60:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if D < 30 or E < 20:
                return 4
            else:
                return 1
        else:
            if D < 40:
                if E < 25:
                    return 1
                elif E > 50:
                    if A < 10:
                        return 2
                    else:
                        return 4
                else:
                    if A > 70:
                        return 1
                    else:
                        return 3
            else:
                if E < 20:
                    return 1
                elif C > 35:
                    return 1
                else:
                    return 3