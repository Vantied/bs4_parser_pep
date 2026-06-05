class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class ParserVersionsNotFoundException(Exception):
    """Вызывается, когда парсер
    не может найти блок со списком версий Python."""
    pass
