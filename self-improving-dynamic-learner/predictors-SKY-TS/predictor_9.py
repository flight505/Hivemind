"""
Predictor 9
Generated on: 2025-09-09 19:00:54
Accuracy: 50.45%
"""


# PREDICTOR 9 - Accuracy: 50.45%
# Correct predictions: 5045/10000 (50.45%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D <= 35:
                return 1
            else:
                return 4
        else:
            if D < 50:
                return 1
            elif D < 80:
                return 2
            else:
                return 3
    else:
        if C > 50:
            if E < 20:
                if D < 25:
                    return 4
                else:
                    return 1
            else:
                if B >= 75:
                    return 2
                else:
                    return 1
        else:
            if E < 20:
                return 1
            else:
                if D > 50:
                    return 3
                else:
                    if C < 20:
                        return 3
                    else:
                        if D < 20:
                            return 1
                        else:
                            if D > 35:
                                return 1
                            else:
                                return 4