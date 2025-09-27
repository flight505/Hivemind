"""
Predictor 58
Generated on: 2025-09-09 19:36:20
Accuracy: 45.80%
"""


# PREDICTOR 58 - Accuracy: 45.80%
# Correct predictions: 4580/10000 (45.80%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if D + E > 90:
                    return 4
                else:
                    return 1
        else:
            if E < 10:
                return 3
            else:
                return 2
    else:
        if C > 50:
            if D < 25:
                return 4
            elif E < 20:
                return 4
            else:
                return 1
        else:
            if E < 20:
                if D > 50:
                    if A > 50:
                        return 1
                    else:
                        return 3
                else:
                    return 1
            else:
                if D > 70 and E < 30:
                    return 4
                elif D < 40 and E > 50:
                    return 1
                else:
                    return 3