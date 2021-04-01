# A handful of abstract tools for interacting with abaco on Tapis' infrastructure.

from agavepy import Agave
from agavepy import actors

API_SERVER = 'https://api.tacc.utexas.edu'    

def update_actor(actorId: str, tapis_token: str) -> int:
    """
    Updates an actor to the latest version of its respective image.
    
    Args:
        actorId: The Abaco ID of the actor you want to update.
        tapisToken: The auth token that Tapis needs to access the actor and make a new one.

    Returns:
        0 on success, 1 on fail
    """
    ag = Agave(
        api_server=API_SERVER,
        token=tapis_token
    )
    actor_body = ag.actors.get(actorId=actorId)
    ag.actors.update(actorId=actorId, body=actor_body)

    # TODO parse response
    return 0

    #### Existing actors can be updated with a new image - no need to return a new actorId

def get_container_vars() -> dict:
    """
    Gets the environment variables from the abaco message delivered to this script's container.

    Requirements:
        This should only be used on an abaco container with a JSON message specified.

    Args:
        None.

    Returns:
        A dictionary, with content depending on the container's execution.
    """
    msg = actors.get_context()
    if "json" in msg['content_type']:
        msg_dict = msg['message_dict']
        return msg_dict
    else:
        print(msg)
        raise Exception("The message passed by abaco isn't in the expected format(JSON, with message_dict).")