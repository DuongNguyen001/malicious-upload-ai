patterns = [
    b"<?php",
    b"eval(",
    b"base64_decode",
    b"shell_exec",
    b"system("
]

def detect_patterns(data):

    score = 0

    for p in patterns:
        if p in data:
            score += 1

    return score
