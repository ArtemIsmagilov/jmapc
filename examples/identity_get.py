#!/usr/bin/env python3

# Example output:
#
# Identity 12345 is for Ness at ness@onett.example.com
# Identity 67890 is for Ness at ness-alternate@onett.example.com

import os

from jmapc import Client
from jmapc.methods import IdentityGet


def main() -> None:
    # Create and configure client
    j = Client(
        host=os.environ["JMAP_HOST"],
        user=os.environ["JMAP_USER"],
        password=os.environ["JMAP_PASSWORD"],
    )

    # Prepare Identity/get request
    # To retrieve all of the user's identities, no arguments are required.
    method = IdentityGet()

    # Call JMAP API with the prepared request
    result = j.call_method(method)

    # Print some information about each retrieved identity
    for identity in result.data:
        print(
            f"Identity {identity.id} is for "
            f"{identity.name} at {identity.email}"
        )


if __name__ == "__main__":
    main()
