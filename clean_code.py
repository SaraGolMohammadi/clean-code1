import math


def calculate_circles_total_area(radius_a: float, radius_b: float) -> float:
  """محاسبه مجموع مساحت دو دایره"""
  area_a = math.pi * (radius_a**2)
  area_b = math.pi * (radius_b**2)
  return area_a + area_b


if __name__ == "__main__":
  r1, r2 = 5.0, 10.0
  total = calculate_circles_total_area(r1, r2)
  print(f"Total area is: {total:.2f}")