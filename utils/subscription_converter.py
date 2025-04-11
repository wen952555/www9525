import re

def convert_subscription(link: str) -> str:
    """
    Convert a subscription link to a different format.
    :param link: Original subscription link.
    :return: Converted subscription link.
    """
    if not link.startswith("http"):
        raise ValueError("Invalid subscription link. Must start with 'http'.")

    # Example: Convert "example.com/old_format" to "example.com/new_format"
    # You can customize the logic here to handle different formats.
    converted_link = re.sub(r'/old_format', '/new_format', link)
    return converted_link

def is_valid_subscription(link: str) -> bool:
    """
    Validate if the provided link is a valid subscription URL.
    :param link: Subscription link to validate.
    :return: True if valid, False otherwise.
    """
    # Example validation logic: Check if the URL contains a specific pattern
    pattern = re.compile(r"https?://[^\s/$.?#].[^\s]*")
    return bool(pattern.match(link))

def extract_subscription_details(link: str) -> dict:
    """
    Extract details from the subscription link.
    :param link: Subscription link to extract details from.
    :return: A dictionary with extracted details.
    """
    # Example logic: Parse the URL and extract meaningful components
    if "example.com" in link:
        return {
            "type": "example",
            "original_link": link,
            "converted_link": convert_subscription(link)
        }
    else:
        return {
            "type": "unknown",
            "original_link": link,
            "converted_link": None
        }