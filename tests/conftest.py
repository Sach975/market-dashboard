import sys
from pathlib import Path

# Add project root to Python path for pytest
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))
