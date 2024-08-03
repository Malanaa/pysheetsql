import gspread
from google.oauth2.service_account import Credentials

def SheetClient(scopes, credentials_file_path):
    """
    Builds a client for accessing Google API.

    Args:
        scopes (list of str): An array of strings specifying the API scopes.
        credentials_file_path (str): The path to the JSON file containing your credentials.

    Returns:
        client: The client object for accessing Google APIs.

    Raises:
        Exception: If an error occurs while creating the client.

    Example:
        client = SheetClient(["https://www.googleapis.com/auth/spreadsheets"], "path/to/credentials.json")
    """
    

    try:
        creds = Credentials.from_service_account_file(credentials_file_path, scopes=scopes)
        client = gspread.authorize(creds)
    except BaseException as e:
        print("An unknown error has occured")
        print(f"Error: {e}")
        
    return client
