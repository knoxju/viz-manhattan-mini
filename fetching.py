import json
import pandas as pd
import requests

MTA_API_KEY = "8c9aa77a-eb79-41be-a77c-909d8fc9ffc9"
MTA_API_BASE = "http://bustime.mta.info/api/siri/vehicle-monitoring.json"


def _flatten_dict(root_key, nested_dict, flattened_dict):
    for key, value in nested_dict.iteritems():
        next_key = root_key + "_" + key if root_key != "" else key
        if isinstance(value, dict):
            _flatten_dict(next_key, value, flattened_dict)
        else:
            flattened_dict[next_key] = value
    return flattened_dict
    

params = {"key": MTA_API_KEY, "MaximumStopVisits":2}


#This is useful for the live MTA Data
def nyc_current():
    resp = requests.get(MTA_API_BASE, params=params).json()
    info = resp['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    return pd.DataFrame([_flatten_dict('', i, {}) for i in info])
