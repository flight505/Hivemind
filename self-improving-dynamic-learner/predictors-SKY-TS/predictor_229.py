"""
Predictor 229
Generated on: 2025-09-09 21:08:18
Accuracy: 50.50%
"""


# PREDICTOR 229 - Accuracy: 50.50%
# Correct predictions: 5050/10000 (50.50%)

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
                return 4
            else:
                if D >= 50:
                    return 1
                else:
                    if B >= 60:
                        return 2
                    else:
                        return 1
        else:
            if E < 20:
                if D < 50:
                    return 3
                else:
                    if B > 50:
                        return 4
                    else:
                        return 1
            else:
                if D < 50:
                    if E > 50:
                        if B >= 75 or A > 90:
                            return 1
                        else:
                            return 4
                    else:
                        return 3
                else:
                    if E > 50:
                        if C < 15:
                            return 4
                        else:
                            return 3
                    else:
                        if B > 60:
                            return 1
                        else:
                            return 3