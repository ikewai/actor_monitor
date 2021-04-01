# This script executes actions to monitor and initiate changes to the abaco/docker containers it's assigned.
from . import abaco_abstract_tools as ab
import json

actorId_original = ab.get_container_vars()["target_actor"]
tapis_token = ab.get_container_vars()["tapis_token"]

ab.update_actor(actorId=actorId_original, tapis_token=tapis_token)