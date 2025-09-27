"""
Predictor 43
Generated on: 2025-09-09 19:25:48
Accuracy: 53.60%
"""


# PREDICTOR 43 - Accuracy: 53.60%
# Correct predictions: 5360/10000 (53.60%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                if E > 20:
                    return 4
                else:
                    return 1
            else:
                if D + E > 100:
                    return 4
                else:
                    return 2
        else:
            if D < 50:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if E < 20:
                return 4
            else:
                return 1
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 2
            else:
                if E > 80:
                    return 4
                elif E < 30:
                    return 1
                else:
                    if E > 60 and B < 10 and D < 10:
                        return 4
                    elif (A > 90 and D > 70) or (C < 20 and D > 50) or (B < 20 and D < 20):
                        return 3
                    else:
                        return 1