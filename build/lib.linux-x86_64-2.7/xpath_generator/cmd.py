import sys
from .xpath_generator import XPATHGenerator


def execute(args = sys.argv[1:]):
    generator = XPATHGenerator()

    for rg in [arg.split('=') for arg in args]:
        generator = getattr(generator, rg[0])(rg[1])
    return generator.generate()
