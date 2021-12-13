import random


def generate_discount_code(prefix: str, letters: str, code_length: int):
    return prefix + ''.join(random.choice(letters) for _ in range(code_length - len(prefix)))