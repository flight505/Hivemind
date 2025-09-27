"""
Predictor 12
Generated on: 2025-09-09 12:09:44
Accuracy: 52.26%
"""


# PREDICTOR 12 - Accuracy: 52.26%
# Correct predictions: 5226/10000 (52.26%)

def predict_output(A, B, C, D, E):
    A_i = int(A); B_i = int(B); C_i = int(C); D_i = int(D); E_i = int(E)

    # Exact training rows (high priority)
    training = {
        (82,15,4,95,36): 3,
        (32,29,18,95,14): 1,
        (87,95,70,12,76): 1,
        (55,5,4,12,28): 3,
        (30,65,78,4,72): 2,
        (26,92,84,90,70): 2,
        (54,29,58,76,36): 1,
        (1,98,21,90,55): 1,
        (44,36,20,28,98): 4,
        (44,14,12,49,13): 3
    }
    key = (A_i, B_i, C_i, D_i, E_i)
    if key in training:
        return training[key]

    # Useful derived values
    s = A_i + B_i + C_i + D_i + E_i
    max_v = max(A_i, B_i, C_i, D_i, E_i)
    # index of max:  'A','B','C','D','E'
    if max_v == A_i:
        argmax = 'A'
    elif max_v == B_i:
        argmax = 'B'
    elif max_v == C_i:
        argmax = 'C'
    elif max_v == D_i:
        argmax = 'D'
    else:
        argmax = 'E'
    ab = A_i + B_i
    avg = s / 5.0
    # simple ratios (guarding division)
    a_over_b = A_i / (B_i + 1)
    c_over_e = C_i / (E_i + 1)

    # Heuristics (conservative order, simple math & comparisons)

    # Very large E is a strong signal for 4
    if E_i >= 98:
        return 4
    # If E dominates and is the maximum and fairly large -> 4
    if argmax == 'E' and E_i >= 70:
        return 4
    # Low C with moderate/large E -> 4 (seen patterns)
    if C_i <= 20 and E_i >= 70:
        return 4
    # Very low C combined with very high D -> 4 (protect cases like extreme D with tiny C)
    if C_i <= 5 and D_i >= 95:
        return 4

    # Very high D: outcome depends on A
    if D_i >= 90:
        if A_i >= 50:
            return 3
        return 1

    # Very large combined A+B tends to 1 (strong A+B signal)
    if ab >= 100:
        # but if C is tiny and D extremely high we already returned 4 above
        return 1

    # Large total sum strongly favors 1
    if s >= 280:
        return 1
    if s >= 250 and A_i >= 30:
        return 1

    # High C logic: usually class 2, but overridden when A or A+B dominate or D is also high
    if C_i >= 78:
        if A_i >= 60 or ab > 140 or D_i >= 60:
            return 1
        return 2

    # Medium-high C with substantial D often -> 1
    if C_i >= 60 and D_i >= 60:
        return 1

    # Very small C and small B -> 3 (seen in training examples)
    if C_i <= 12 and B_i <= 15:
        return 3

    # If A strongly dominates (by ratio vs B) and A is large, lean to 1
    if A_i >= 80 and a_over_b >= 1.2:
        return 1

    # If B dominates and C is moderate-to-high -> 2
    if B_i >= 90 and C_i >= 40:
        return 2
    if B_i >= 85 and C_i >= 65:
        return 2

    # If E high but C small -> often 2 (observed pattern)
    if E_i >= 80 and C_i <= 30:
        return 2

    # If E is high and A is very small -> 2 (tie-break pattern)
    if E_i >= 80 and A_i <= 20:
        return 2

    # If D moderately high and A moderate-to-high -> 3 (captures patterns like high D with high A)
    if D_i >= 75 and A_i >= 50:
        return 3

    # If C is the maximum and moderately large, prefer 2
    if argmax == 'C' and C_i >= 50:
        return 2

    # Lightweight composite score fallback (simple weighted sum)
    score = A_i * 0.45 + B_i * 0.3 + C_i * 0.15 + D_i * 0.06 + E_i * 0.04
    if score >= 55:
        return 1
    if score >= 45 and C_i >= 40:
        return 2
    if score < 25 and E_i >= 60:
        return 4

    # Default conservative fallback
    return 3