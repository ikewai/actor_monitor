# This script executes actions to monitor and initiate changes to the abaco/docker containers it's assigned.
from . import abaco_abstract_tools as ab
import json

actorId_original: str = ab.get_container_vars()["target_actor"]
tapis_token: str = ab.get_container_vars()["tapis_token"]

# No need to overcomplicate, just have Abaco determine if a new pull is needed
ab.update_actor(actorId=actorId_original, tapis_token=tapis_token)