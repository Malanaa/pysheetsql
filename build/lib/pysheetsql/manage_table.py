import gspread

def AddData(client, table_name, data):
    """
    Adds data to a table.

    Args:
        client (SheetClient): The SheetClient client instance.
        table_name (str): The name of the table to add data to.
        data (list): A list of values to add to the table. If the table has a primary key, data should exclude the primary key value.

    Returns:
        None: The function does not return a value.

    Raises:
        TypeError: If `table_name` is not a string.
        gspread.exceptions.SpreadsheetNotFound: If the table does not exist.

    Example:
        AddData(client, "StudentRecords", ["John Doe", 20, "A"])
    """

    try:
        sh = client.open(table_name)
        ws = sh.sheet1
    except gspread.exceptions.SpreadsheetNotFound:
         print('Table not found.')

    field_values = ws.row_values(1)

    if type(table_name) != str:
        print("TypeError: Arg table_name only accepts string")

    #use primaryID identifier to  check if it has primary key or not
    if "primaryID" in field_values:
            if len(field_values) - 1 == len(data):
                    id_values = ws.col_values(1)
                    if len(id_values) > 1:
                        primaryKeyId = int(id_values[len(id_values) - 1]) + 1
                        cell = ws.find(id_values[len(id_values) - 1])
                        ws.update_cell(cell.row + 1, 1, primaryKeyId)
                        for i in range(2, len(data) + 2):
                            ws.update_cell(cell.row + 1, i, data[i - 2])
                    else:
                        ws.update_cell(2,1, 0) #Updating first ID because this is FIRST set of infomation.
                        for i in range(2, len(data) + 2):
                            ws.update_cell(2, i, data[i - 2])
    else:
        if len(field_values) == len(data):
                    values = ws.col_values(1)
                    if len(values) > 1:
                        cell = ws.find(values[len(values) - 1])
                        for i in range(1, len(data) + 1):
                            ws.update_cell(cell.row + 1, i, data[i - 1])
                    else:
                        for i in range(1, len(data) + 1):
                            ws.update_cell(2, i, data[i - 1])


def GetDataName(client, table_name, target_main_field_name):
    """
    Retrieves a row of data from a table based on the main field name.

    Args:
        client (SheetClient): The SheetClient client instance.
        table_name (str): The name of the table to retrieve data from.
        target_main_field_name (str): The value in the main field to identify the row to retrieve.

    Returns:
        list: A list of values from the specified row, or None if the table or main field name is not found.

    Raises:
        TypeError: If `table_name` or `target_main_field_name` is not a string.
        gspread.exceptions.SpreadsheetNotFound: If the table does not exist.

    Example:
        GetDataName(client, "StudentRecords", "John Doe")
    """

    if type(table_name) != str or type(target_main_field_name) != str:
        print("TypeError: name Args only accepts string.")

    try:
        sh = client.open(table_name)
        ws = sh.sheet1
        cell = ws.find(target_main_field_name)
        print(ws.row_values(1)) #printing the headers for refernence
        row_values = ws.row_values(cell.row)
        return row_values
    except:
         print("Table not found.")


def GetDataID(client, table_name, target_id):
    """
    Retrieves a row of data from a table based on the primary ID.

    Args:
        client (SheetClient): The SheetClient client instance.
        table_name (str): The name of the table to retrieve data from.
        target_id (int): The primary ID value to identify the row to retrieve.

    Returns:
        list: A list of values from the specified row, or None if the table or ID is not found.

    Raises:
        TypeError: If `table_name` is not a string.
        ValueError: If `target_id` cannot be converted to an integer.
        gspread.exceptions.SpreadsheetNotFound: If the table does not exist.

    Example:
        GetDataID(client, "StudentRecords", 1)
    """

    if type(table_name) != str:
        print("TypeError: name Args only accepts string.")

    id_int = int(target_id)

    try:
        sh = client.open(table_name)
        ws = sh.sheet1
        cell = ws.find(id_int)
        print(ws.row_values(1)) #printing the headers for refernence
        row_values = ws.row_values(cell.row)
        return row_values
    except:
         print("Table Not found")


def UpdateDataName(client, table_name, target_main_field_name, target_change_field_name, target_change_value): #only works with primaryID tabes
    """
    Updates a value in a row based on the main field name in a table with a primary key.

    Args:
        client (SheetClient): The SheetClient client instance.
        table_name (str): The name of the table to update.
        target_main_field_name (str): The value in the main field to identify the row to update.
        target_change_field_name (str): The field name in which to update the value.
        target_change_value (str): The new value to set in the specified field.

    Returns:
        None: The function does not return a value.

    Raises:
        TypeError: If `table_name`, `target_main_field_name`, `target_change_field_name`, or `target_change_value` is not a string.
        gspread.exceptions.SpreadsheetNotFound: If the table does not exist.

    Example:
        UpdateDataMain(client, "StudentRecords", "John Doe", "Age", "21")
    """

    if type(table_name) != str or type(target_main_field_name) != str or type(target_change_field_name) != str or type(target_change_value) != str:
        print("TypeError: name Args only accepts string.")
    
    try:
        sh = client.open(table_name)
        ws = sh.sheet1
    except gspread.exceptions.SpreadsheetNotFound:
         print('Table not found.')

    
    cell_main = ws.find(target_main_field_name)
    cell_target = ws.find(target_change_field_name)
    ws.update_cell(cell_main.row, cell_target.col, target_change_value)


def UpdateDataID(client, table_name, target_id, target_change_field_name, target_change_value): #only works with primaryID tabes
    """
    Updates a value in a row based on the primary ID in a table with a primary key.

    Args:
        client (SheetClient): The SheetClient client instance.
        table_name (str): The name of the table to update.
        target_id (int): The primary ID value to identify the row to update.
        target_change_field_name (str): The field name in which to update the value.
        target_change_value (str): The new value to set in the specified field.

    Returns:
        None: The function does not return a value.

    Raises:
        TypeError: If `table_name`, `target_change_field_name`, or `target_change_value` is not a string.
        ValueError: If `target_id` cannot be converted to an integer.
        gspread.exceptions.SpreadsheetNotFound: If the table does not exist.

    Example:
        UpdateDataID(client, "StudentRecords", 1, "Age", "22")
    """

    if type(table_name) != str or type(target_change_field_name) != str or type(target_change_value) != str:
        print("TypeError: name Args only accepts string.")
    
    id_int = int(target_id)

    try:
        sh = client.open(table_name)
        ws = sh.sheet1
    except gspread.exceptions.SpreadsheetNotFound:
         print('Table not found.')
    
    cell_main = ws.find(id_int)
    cell_target = ws.find(target_change_field_name)
    ws.update_cell(cell_main.row, cell_target.column, target_change_value)

def getID(client, table_name, target_main_field_name): #only works with primaryID tabes
    """
    Retrieves the primary ID based on the main field name in a table with a primary key.

    Args:
        client (SheetClient): The SheetClient client instance.
        table_name (str): The name of the table to retrieve the ID from.
        target_main_field_name (str): The value in the main field to identify the row.

    Returns:
        int: The primary ID from the specified row, or None if the table or main field name is not found.

    Raises:
        TypeError: If `table_name` or `target_main_field_name` is not a string.
        gspread.exceptions.SpreadsheetNotFound: If the table does not exist.

    Example:
        primary_id = getID(client, "StudentRecords", "John Doe")
    """

    if type(table_name) != str or type(target_main_field_name) != str:
        print("TypeError: name Args only accepts string.")

    try:
        sh = client.open(table_name)
        ws = sh.sheet1
    except gspread.exceptions.SpreadsheetNotFound:
         print('Table not found.')
    cell_main = ws.find(target_main_field_name)
    row_values = ws.row_values(cell_main.row)
    return row_values[0]


def DeleteData(client, table_name, target_main_field_name):
    """
    Deletes a row based on the main field name in a table.

    Args:
        client (SheetClient): The SheetClient client instance.
        table_name (str): The name of the table to delete data from.
        target_main_field_name (str): The value in the main field to identify the row to delete.

    Returns:
        None: The function does not return a value.

    Raises:
        TypeError: If `table_name` or `target_main_field_name` is not a string.
        gspread.exceptions.SpreadsheetNotFound: If the table does not exist.

    Example:
        DeleteData(client, "StudentRecords", "John Doe")
    """

    if type(table_name) != str or type(target_main_field_name) != str:
        print("TypeError: name Args only accepts string.")

    try:
        sh = client.open(table_name)
        ws = sh.sheet1
    except gspread.exceptions.SpreadsheetNotFound:
         print('Table not found.')

    cell = ws.find(target_main_field_name)
    ws.delete_rows(cell.row)


def GetAllData(client, table_name):
    """
    Retrieves all rows of data from a table as a list of lists.

    Args:
        client (SheetClient): The SheetClient client instance.
        table_name (str): The name of the table to retrieve data from.

    Returns:
        list of list of str: A list of lists where each inner list represents a row of data.

    Raises:
        TypeError: If `table_name` is not a string.
        gspread.exceptions.SpreadsheetNotFound: If the table does not exist.

    Example:
        all_data = GetAllData(client, "StudentRecords")
    """

    if type(table_name) != str:
        print("TypeError: name Args only accepts string.")

    try:
        sh = client.open(table_name)
        ws = sh.sheet1
    except gspread.exceptions.SpreadsheetNotFound:
         print('Table not found.')

    table_values = ws.get_all_values()
    return(table_values)
