""" Write a function that when given a URL as a string,
parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""


def domain_name(url:str):

    """
    >>> domain_name("http://github.com/carbonfive/raygun")
    'github'
    >>> domain_name("http://www.zombie-bites.com")
    'zombie-bites'
    >>> domain_name("https://www.cnet.com")
    'cnet'
    """
    startindex = 0
    if url.find('www') != -1:
        startindex = url.find('www') +4
    elif url.find('//') != -1:
        startindex =url.find('//') +2

    middle = url[startindex:len(url)]

    return middle[:middle.find('.')]




if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)