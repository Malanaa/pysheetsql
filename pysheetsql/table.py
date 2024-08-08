import gspread
from gspread.utils import ExportFormat




def CreateTable(client,table_name,fields, primary_key=True):
    """
    Creates a table.

    Args:
        client (SheetClient): The SheetClient client instance.
        table_name (str): The name of the table.
        fields (list of str): A list of field names (the first field is considered the class name).
        primary_key (bool, optional): Whether to include a primary key field. Default is True.

    Returns:
        None: The function does not return a value.

    Raises:
        TypeError: If `table_name` is not a string or `fields` is not a list of strings.

    Example:
        CreateTable(client, "StudentRecords", ["Name", "Age", "Grade"])
    """

    #Type safety
    if type(table_name) != str:
        print("TypeError: Arg table_name only accepts string")
    if type(fields) != list:
        print("TypeError: Arg fields must be a list.")
        return None

    try:
        client.open(table_name)
        print("Table Already Exists")
    except gspread.exceptions.SpreadsheetNotFound:
        for i in range(len(fields)):
            if type(fields[i]) != str:
                print("TypeError: fields list can only contain string.")
                return None
            if "primaryID" in fields:
                return None
            if len(fields) != len(set(fields)):
                return None
        else:
            sh = client.create(table_name)
            ws = sh.sheet1
            if primary_key:
                fields.insert(0, "primaryID")
            for i in range(len(fields)):
                ws.update_cell(1,i+1, fields[i])
            


def DeleteTable(client, table_name):
        """
        Deletes a table.

        Args:
            client (SheetClient): The SheetClient client instance.
            table_name (str): The name of the table you want to delete.

        Returns:
            None: The function does not return a value.

        Raises:
            TypeError: If `table_name` is not a string.
            gspread.exceptions.SpreadsheetNotFound: If the table does not exist.

        Example:
            DeleteTable(client, "StudentRecords")
        """

        #Type safety
        if type(table_name) != str:
            print("TypeError: Arg table_name only accepts string")

        try:
            sh = client.open(table_name)
            fileId = sh.id
            client.del_spreadsheet(fileId)
        except gspread.exceptions.SpreadsheetNotFound:
            print("This table does not exist.")


def ListTables(client):
    """
    Lists all the tables.

    Args:
        client (SheetClient): The SheetClient client instance.

    Returns:
        None: The function does not return a value.

    Example:
        ListTables(client)
    """

    spreadsheets = client.list_spreadsheet_files()

    if len(spreadsheets) > 0:
        for i in range(len(spreadsheets)):
            print(f" {i+1}: {spreadsheets[i]['name']}")
    else:
        print("No tables were found.")


def ExportTable(client, table_name):
    """
    Exports a table as a CSV file.

    Args:
        client (SheetClient): The SheetClient client instance.
        table_name (str): The name of the table you want to export.

    Returns:
        None: The function does not return a value.

    Raises:
        TypeError: If `table_name` is not a string.
        gspread.exceptions.SpreadsheetNotFound: If the table does not exist.

    Example:
        ExportTable(client, "StudentRecords")
    """

    #Type safety
    if type(table_name) != str:
        print("TypeError: Arg table_name only accepts string")
    
    try:
        sh = client.open(table_name)
        fileId = sh.id
        file = client.export(fileId, format=ExportFormat.CSV)
        with open(f'{table_name}.csv', 'w') as exported_file:
            exported_file.write(file.decode("utf-8"))
    except gspread.exceptions.SpreadsheetNotFound:
            print("This table does not exist.")


def ShareTables(client, emails, table_name=None):
    ''' 
    Share Tables:
    
    Args:
    client: sheet client you built with the SheetClient function
    emails: A lists of string specifiying the user email(each element)
    table_name: Default=None, gives user permission to the specific table. if table_name is not specificed every table under the service account will be given permission.

    Raises:
    gspread.exceptions.SpreadsheetNotFound if spreadsheet not found.
    error defined

    Return:
    None

    '''

    if table_name:
        try:
            sh = client.open(table_name)
            for email in emails:
                sh.share(email, perm_type='user', role='writer') #read docs add a veiwer role too. accepted params       
        except gspread.exceptions.SpreadsheetNotFound:
                print("This table does not exist.")
                return None
    else:
        try:
            tables = ListTables(client)
            if tables:
                for table in tables:
                    sh = client.open(table_name)
                    for email in emails:
                        sh.share(email, perm_type='user', role='writer')
            else:
                print("No tables found.")
                return None
        except BaseException as e:
            print(f"{e}")
            return None
        