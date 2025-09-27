"""
Predictor 344
Generated on: 2025-09-09 08:57:49
Accuracy: 29.45%
"""


# PREDICTOR 344 - Accuracy: 29.45%
# Correct predictions: 2945/10000 (29.45%)

def predict_output(A, B, C, D, E):
    # Check if A is the largest
    if A >= B and A >= C and A >= D and A >= E:
        return 3
    # Check if B is the largest
    elif B >= A and B >= C and B >= D and B >= E:
        # Find second largest
        if A >= C and A >= D and A >= E:
            second = A
        elif C >= A and C >= D and C >= E:
            second = C
        elif D >= A and D >= C and D >= E:
            second = D
        else:
            second = E
        if second == A:
            return 1
        else:
            if second == D:
                if C < 50:
                    return 1
                else:
                    return 2
            else:
                return 2
    # Check if C is the largest
    elif C >= A and C >= B and C >= D and C >= E:
        return 2
    # Check if D is the largest
    elif D >= A and D >= B and D >= C and D >= E:
        if B < 20:
            return 3
        else:
            return 1
    # E is the largest
    else:
        return 4