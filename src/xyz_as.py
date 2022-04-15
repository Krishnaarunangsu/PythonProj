# Python Best Practices Examples
from src.utilities import constants as CONSTANTS


class PythonManipulation:
    """

    """
    def __init__(self):
        """

        """
    @classmethod
    def show_for_loop_examples(cls, size_in_bytes):
        """
        for loop
        :return:
        """
        # size_limit = 1024.0
        # sizes = ['bytes', 'KB', 'MB', 'GB']
        # for x in sizes:
        #     if size_in_bytes < size_limit:
        #         return "%3.1f %s" % (size_in_bytes, x)
        #     size_in_bytes /= size_limit
        size_limit = CONSTANTS.SIZE_LIMIT
        for x in CONSTANTS.SIZES:
            if size_in_bytes < size_limit:
                return "%3.1f %s" % (size_in_bytes, x)
            size_in_bytes /= size_limit


if __name__ == '__main__':
    size_formatted = PythonManipulation.show_for_loop_examples(2048)
    print(f"Size:{size_formatted}")


