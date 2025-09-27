"""
Predictor 318
Generated on: 2025-09-09 21:48:45
Accuracy: 50.42%
"""


# PREDICTOR 318 - Accuracy: 50.42%
# Correct predictions: 5042/10000 (50.42%)

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
                if D < 50:
                    return 4
                else:
                    return 1
            else:
                return 1
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    if B > 30:
                        return 1
                    else:
                        return 3
            else:
                if D < 50:
                    if C > 40:
                        return 4
                    else:
                        return 3
                else:
                    if D > 90:
                        if C < 10:
                            return 4
                        else:
                            return 1
                    else:
                        if (B > 60 and C < 20) or E > 80:
                            return 1
                        else:
                            return 3