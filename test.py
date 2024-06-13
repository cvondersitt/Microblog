import sys
print(sys.executable)

try:
    from flask_login import LoginManager
    print("flask_login imported successfully")
except ImportError as e:
    print(f"Error: {e}")
