import math

def cosine_sim(v1, v2):
    dot_product = sum(a*b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a*a for a in v1))
    mag2 = math.sqrt(sum(b*b for b in v2))
    if not mag1 or not mag2:
        return 0
    return dot_product / (mag1 * mag2)

if __name__ == '__main__':
    vec1 = [1, 2, 3]
    vec2 = [1, 2, 4]
    print(f'Cosine similarity between {vec1} and {vec2} is: {cosine_sim(vec1, vec2):.4f}')