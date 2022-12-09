def openReadFile(nameFile):
    """Read the content of a file

    Args:
        nameFile (str): Name of the file

    Returns:
        str: Content of the file
    """
    return open(nameFile, "r")
    

def openWriteFile(namefile):
    """Write the content of a file

    Args:
        nameFile (str): Name of the file

    Returns:
        str: New file
    """
    return open(namefile, "w")


def closeFile(file):
    """Close open file

    Args:
        file: Open file
    """
    file.close()