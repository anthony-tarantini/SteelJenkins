import requests
import time
import json
from xml.etree import ElementTree

gameName = "RES"
eventName = "ASD"

def start():
    with open("/Library/Application Support/SteelSeries Engine 3/coreProps.json", "r") as properties:
        engineServer = json.load(properties)['address']

    with open("../json/properties.json", "r") as jsonFile:
        properties = json.load(jsonFile)
        jenkinsServer = properties['location']
        jenkinsProject = properties['title']

    with open("../json/gameMetadata.json", "r") as jsonFile:
        game = json.load(jsonFile)
        game['game'] = gameName

    with open("../json/eventBinding.json", "r") as jsonFile:
        eventBind = json.load(jsonFile)
        eventBind['game'] = gameName
        eventBind['event'] = eventName

    requests.post(
        'http://{}/game_metadata'.format(engineServer),
        json=game
    )

    requests.post(
        'http://{}/bind_game_event'.format(engineServer),
        json=eventBind
    )

    while True:
        resp = requests.get(jenkinsServer)
        tree = ElementTree.fromstring(resp.content)
        if resp.status_code == 200:
            for child in tree:
                if child.attrib['name'] == jenkinsProject:
                    if child.attrib['activity'] == 'Building':
                        requests.post(
                            'http://{}/game_event'.format(engineServer),
                            json={"game": gameName, "event": eventName, "data": {"value": 50}}
                        )
                    else:
                        if child.attrib['lastBuildStatus'] == 'Success':
                            requests.post(
                                'http://{}/game_event'.format(engineServer),
                                json={"game": gameName, "event": eventName, "data": {"value": 100}}
                            )
                        else:
                            requests.post(
                                'http://{}/game_event'.format(engineServer),
                                json={"game": gameName, "event": eventName, "data": {"value": 0}}
                            )

                    print('{}'.format(child.attrib))

        time.sleep(5)

if __name__ == '__main__':
    start()
