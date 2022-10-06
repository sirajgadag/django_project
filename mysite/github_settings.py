
# Copy this file to github_settings.py (don't check it into github)

# Go to https://github.com/settings/developers

# Add a New OAuth2 App

# Using ngrok is hard because the url changes every time you start ngrok

# If you are running on localhost, here are some settings:

# Application name: Siraj Local
# Homepage Url: http://localhost:8000
# Application Description: Whatever
# Authorization callback URL: http://127.0.0.1:8000/oauth/complete/github/


# Using PythonAnywhere here are some settings:

# Application name: sirajgadag PythonAnywhere
# Homepage Url: https://sirajgadag.pythonanywhere.com
# Application Description: Whatever
# Authorization callback URL: https://sirajgadag.pythonanywhere.com/oauth/complete/github/

# Also on PythonAnywhere, go into the Web tab and enable "Force HTTPS"
# so you don't get a redirect URI mismatch.

# Then copy the client_key and secret to this file

SOCIAL_AUTH_GITHUB_KEY = '89cd8bb82502e3a8a015'
SOCIAL_AUTH_GITHUB_SECRET = '794c357e421f0c1199ce74048c6688b4f5a6567c'

# For detail: https://readthedocs.org/projects/python-social-auth/downloads/pdf/latest/

