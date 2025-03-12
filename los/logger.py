import os
import logging

# Ensure logs directory exists
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Define log file path
log_file = os.path.join(log_dir, "data_analysis.log")
# Configure logging
log_file = "data_analysis.log"  # Use a relative or absolute path
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",  # Overwrites existing log file each run
)

# Function to log messages
def log_message(message):
    logging.info(message)
    print(message)  # Also print message for visibility
