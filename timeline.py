
import ctypes
import subprocess
import sys
from pathlib import Path

folder = Path(__file__).parent
c_file = folder / "calculator.c"

if sys.platform == "darwin":
    library_file = folder / "libcalculator.dylib"
    command = [
        "clang", "-dynamiclib", "-fPIC",
        str(c_file), "-o", str(library_file)
    ]
else:
    library_file = folder / "libcalculator.so"
    command = [
        "gcc", "-shared", "-fPIC",
        str(c_file), "-o", str(library_file)
    ]

if not library_file.exists():
    subprocess.run(command, check=True)

cosmic = ctypes.CDLL(str(library_file))

cosmic.cosmic_calendar_day.argtypes = [
    ctypes.c_double,
    ctypes.c_double
]
cosmic.cosmic_calendar_day.restype = ctypes.c_double


def calculate_cosmic_day(universe_age, event_age):
    result = cosmic.cosmic_calendar_day(
        universe_age, event_age
    )

    if result < 0:
        raise ValueError("Invalid cosmic age values")

    return result
