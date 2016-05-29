"""
Logic related to the pull request formatting operations
"""

def strip_git_info(raw_url):
    """
    Takes a github branch url ie
    https://github.com/kvickers/kylevickers_website/tree/branch_name_here
    and returns a dictionary with important elements stripped

    ['https:', '', 'github.com', 'z0mi3ie', 'kylevickers_website', 'tree', 'pr_template']
    """
    HOST = 2
    USERNAME = 3
    REPO = 4
    BRANCH = 6

    splits = raw_url.split('/')

    formatted = {
        'host': splits[HOST],
        'username': splits[USERNAME],
        'repo': splits[REPO],
        'branch': splits[BRANCH],
        'raw': raw_url,
    }

    return formatted
