"""
Predictor 320
Generated on: 2025-09-09 21:48:45
Accuracy: 51.01%
"""


# PREDICTOR 320 - Accuracy: 51.01%
# Correct predictions: 5101/10000 (51.01%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                return 4
        else:
            return 2
    else:
        if C > 50:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 4
            else:
                return 1
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    if E < 10:
                        return 1
                    else:
                        return 3
            else:
                if C < 10:
                    return 4
                else:
                    if D < 40:
                        if C > 40:
                            return 4
                        else:
                            return 3
                    else:
                        if B > 60:
                            if E < 30:
                                return 3
                            else:
                                return 1
                        else:
                            if E > 80:
                                return 1
                            else:
                                return 3