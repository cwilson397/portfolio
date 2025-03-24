############################
# Colby Wilson
# 3/24/2025
# Password program (Main)
###########################

import gui # Imports the GUI module
from password_generation import generate_strong_password
from password_validation import check_password_strength
from breach_check import is_breached

if __name__ == "__main__":
    # Runs the GUI
    gui.root.mainloop()

