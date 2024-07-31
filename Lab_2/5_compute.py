import math
angle_degrees = 60
angle_radians = math.radians(angle_degrees)
print("a) sin(60 degrees):",math.sin(angle_radians))
print("b) cos(pi):",math.cos(math.pi))
print("c) sin(0.8660254037844386):", math.sin(0.8660254037844386))

angle_degrees_90 = 90
angle_radians_90 = math.radians(angle_degrees_90)
try:
    tan_90 = math.tan(angle_radians_90)
except ValueError:
    tan_90 = float('inf') 
print("d) tan(90 degrees):", tan_90)
