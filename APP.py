#!/usr/bin/env python3

import sys  # Provides access to system-specific parameters and functions

def print_app_version():
    """
    Prints the current application version and exits the application.
    """
    app_version = "1.0.0"  # Define the current version of the application; update this as needed
    print(f"Current Application Version: {app_version}")  # Display the application version to the user
    sys.exit()  # Terminate the program immediately after displaying the version

print_app_version()  # Call the function to print the app version and exit