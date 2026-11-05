class PriceTrackerException(Exception):
    """Base exception for the price tracker."""
    pass


class ScraperException(PriceTrackerException):
    """Raised when scraping fails."""
    pass


class ParserException(PriceTrackerException):
    """Raised when price parsing fails."""
    pass


class ProductNotFoundException(PriceTrackerException):
    """Raised when a product is not found."""
    pass


class DatabaseException(PriceTrackerException):
    """Raised when a database operation fails."""
    pass


class ExportException(PriceTrackerException):
    """Raised when report export fails."""
    pass


class ConfigurationException(PriceTrackerException):
    """Raised when configuration is invalid."""
    pass