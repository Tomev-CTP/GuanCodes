__author__ = "Tomasz Rybotycki"

"""
    This script contains quick test ground of the generator. These are NOT unit tests.
"""

from guancodes.GuanCodeGenerator import GuanCodeGenerator

for code in GuanCodeGenerator.generate_guan_codes([4, 0, 3, 3, 3]):
    print(code)

