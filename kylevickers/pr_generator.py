def create_pull_request(ticket_number, ticket_title, ticket_url, summary, review_a, review_b, setup, test, verify):
    """ Create the pull request description string

    :param str summary: summary of what this PR includes
    :param str ticket_number: ticket number string
    :param str ticket_title: title of ticket
    :param str reviews: list of review tickets
    :param str setup: description of setup required
    :param test: description of testing steps
    :param verify: description of verifying
    """
    pull_request_format = """
    [{ticket_number}] {ticket_title}

    # Summary
    {summary}

    # Ticket
    {ticket_url}

    # Reviews
    - {review_a}
    - {review_b}

    # Setup
    {setup}

    # Test
    {test}

    # Verify
    {verify}
    """

    return pull_request_format.format(summary=summary, ticket=ticket)

