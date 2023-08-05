import os
import sys
from dotenv import load_dotenv

class EnvironnementVariable:
    load_dotenv()
    required_variables = {
        'SPOTIFY_CLIENT_ID': os.getenv('SPOTIFY_CLIENT_ID'),
        'SPOTIFY_CLIENT_SECRET': os.getenv('SPOTIFY_CLIENT_SECRET'),
        'SPOTIFY_APP_REDIRECT_URI': os.getenv("REDIRECT_URI"),
        'SPOTIFY_SCOPE': os.getenv('SCOPE'),
        'YOUTUBE_API_KEY': os.getenv('YOUTUBE_API_KEY')
    }
    
    #Validation for variable of .env config file
    def check_valid_variable(self):
        for key, value in self.required_variables.items():
            if not isinstance(value, str) or not value.strip():
                print(f"Error: The value for {key} must be a non-empty string")
                sys.exit(1)