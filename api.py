# This is a test repository containing secrets for Gitleaks detection

# Example API Key
API_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

# Example AWS Secret Key
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Example Password
DB_PASSWORD = "SuperSecret123!"

# Example Private Key
PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQ...\n-----END PRIVATE KEY-----"

# Example Token
github_token = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"

# Hardcoded credentials in a function
def connect_to_database():
    username = "admin"
    password = "admin123"
    return f"Connecting with {username}:{password}"

if __name__ == "__main__":
    print("This repo is for testing Gitleaks detection.")
