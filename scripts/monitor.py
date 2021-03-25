# This script executes actions to monitor and initiate changes to the abaco/docker containers it's assigned.
from . import abaco_abstract_tools as abacoAT
import json


actorId_original = abacoAT.get_container_vars()["target_actor"]
tapis_token = abacoAT.get_container_vars()["tapis_token"]

abacoAT.update_actor(actorId=actorId_original, tapis_token=tapis_token)
