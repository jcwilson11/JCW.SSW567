def classify_triangle(a: float, b: float, c: float) -> str:
    # Check validity
    if a <= 0 or b <= 0 or c <= 0:
        return "not a triangle"
    if a + b <= c or a + c <= b or b + c <= a:
        return "not a triangle"
    
    # Classification by sides
    if a == b == c:
        triangle_type = "equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "isosceles"
    else:
        triangle_type = "scalene"
    
    # Right triangle check
    sides = sorted([a, b, c])
    if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9:
        triangle_type += " right"
    
    return triangle_type + " triangle"
