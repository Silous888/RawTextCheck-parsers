"""Template parser for RawTextCheck."""

# == Imports ==================================================================

from logging import Logger

from rawtextcheck.logger import get_logger
from rawtextcheck.newtype import ParserArgument


# == Constants ================================================================

# examples of arguments
# ARG_1 = ParserArgument(name="arg1", optional=False)
# ARG_2 = ParserArgument(name="arg2", optional=True)

# Fill the list with arguments (ARG_1, ARG_2...) you have.
LIST_ARGUMENTS: list[ParserArgument] = []


# == Global Variables =========================================================

logger: Logger = get_logger(__name__)
# You can use it like this:
# logger.error("Error when parsing the file %s : %s", filepath, e)
# logger.error, logger.warning, logger.info


# == Functions ================================================================


# Implement is_filepath_valid only if needed. If your file is an offline file,
# you probably don't need this function. Used to check if the file can be parsed
# by this parser and if the the file exists.

# def is_filepath_valid(filepath: str) -> bool:
#     """check if the filepath is a valid file for this parser

#     Args:
#         filepath (str): path of the file

#     Returns:
#         bool: True if valid, False otherwise
#     """
#     return False


# implement get_filename only if needed. If your file is an offline file, you probably don't need
# this function. Used for for saving the results.

# def get_filename(filepath: str) -> str:
#     """get the filename of the filepath

#     Args:
#         filepath (str): path of the file

#     Returns:
#         str: name of the file
#     """
#     return filepath


def parse_file(filepath: str, arguments: dict[str, str]) -> list[tuple[str, str]]:
    """Parse a file and return each non-empty line with identifier (line number
    or something else)

    Args:
        filepath (str): Path to the file
        arguments (dict[str, str]): arguments of the parser

    Returns:
        list[tuple[str, str]]: List of (id, line).
    """
    return []
