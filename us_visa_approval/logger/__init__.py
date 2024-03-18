import logging
import os

from from_root import from_root  # Corrected import statement
from datetime import datetime

# Corrected LOG_FILE format to avoid using slashes
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

# Correct usage of the absolute path for logs_path
logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

# Ensure the directory is created at the absolute path
os.makedirs(os.path.join(from_root(), log_dir), exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    level=logging.DEBUG,
    format='[ %(asctime)s] %(name)s- %(levelname)s - %(message)s',
)
