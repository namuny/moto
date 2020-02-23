from __future__ import unicode_literals
from .responses import IoTResponse

url_bases = ["https?://iot.(.+).amazonaws.com"]

url_paths = {
    '{0}/endpoint$': IoTResponse.dispatch,
    '{0}/keys-and-certificate$': IoTResponse.dispatch,
    '{0}/certificates$': IoTResponse.dispatch,
    '{0}/certificates/<certificateId>$': IoTResponse.dispatch,
    '{0}/jobs$': IoTResponse.dispatch,
    '{0}/jobs/<jobId>$': IoTResponse.dispatch,
    '{0}/jobs/<jobId>/job-document$': IoTResponse.dispatch,
    '{0}/policies$': IoTResponse.dispatch,
    '{0}/policies/<policyName>$': IoTResponse.dispatch,
    '{0}/principals/things$': IoTResponse.dispatch,
    '{0}/principal-policies$': IoTResponse.dispatch,
    '{0}/principal-policies/<policyName>$': IoTResponse.dispatch,
    '{0}/things$': IoTResponse.dispatch,
    '{0}/things/<thingName>$': IoTResponse.dispatch,
    '{0}/things/<thingName>/principals$': IoTResponse.dispatch,
    '{0}/things/<thingName>/thing-groups$': IoTResponse.dispatch,
    '{0}/thing-groups$': IoTResponse.dispatch,
    '{0}/thing-groups/addThingToThingGroup$': IoTResponse.dispatch,
    '{0}/thing-groups/removeThingFromThingGroup': IoTResponse.dispatch,
    '{0}/thing-groups/<thingGroupName>$': IoTResponse.dispatch,
    '{0}/thing-groups/<thingGroupName>/things$': IoTResponse.dispatch,
    '{0}/thing-types$': IoTResponse.dispatch,
    '{0}/thing-types/<thingTypeName>$': IoTResponse.dispatch,
}
