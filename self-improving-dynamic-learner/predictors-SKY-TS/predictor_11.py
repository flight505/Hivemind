"""
Predictor 11
Generated on: 2025-09-09 19:00:54
Accuracy: 51.72%
"""


# PREDICTOR 11 - Accuracy: 51.72%
# Correct predictions: 5172/10000 (51.72%)

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
                if D > 90:
                    return 3
                else:
                    return 2
    else:
        if C > 50:
            if E < 20:
                if A > 90 or D > 50:
                    return 1
                else:
                    return 4
            else:
                if D < 20:
                    return 3
                else:
                    if B >= 75:
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
                elif D > 50:
                    return 3
                else:
                    if C > 20:
                        return 1
                    else:
                        return 3