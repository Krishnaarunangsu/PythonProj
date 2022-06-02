class KeyErrorDesc(Exception):
    """

    """

    def __init__(self, f, *args):
        super().__init__(args)
        self.f = f

    def __str__(self):
        return f'The Birthday of{self.f} is not found'
