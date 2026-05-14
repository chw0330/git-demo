from pathlib import Path
import sys


LOCAL_PACKAGES = Path(__file__).resolve().parent / ".python-packages"
if sys.prefix == sys.base_prefix and LOCAL_PACKAGES.exists():
    sys.path.insert(0, str(LOCAL_PACKAGES))
