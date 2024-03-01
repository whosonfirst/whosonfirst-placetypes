#!/usr/bin/env python

import sys
import os.path
import json

if __name__ == '__main__':

    whoami = sys.argv[0]
    whoami = os.path.abspath(whoami)
    
    bin = os.path.dirname(whoami)
    root = os.path.dirname(bin)

    placetypes = os.path.join(root, 'placetypes')

    tmp = {}
    placetype_map = {}

    for (root, dirs, files) in os.walk(placetypes):

        for f in files:
    
            path = os.path.join(root, f)

            if not path.endswith('.json'):
                continue

            fh = open(path, 'r')
            data = json.load(fh)

            id = data.get('wof:id', None)
            placetype = data.get('wof:name', None)
            role = data.get('wof:role', None)
            parent = data.get('wof:parent', [])

            placetype_map[placetype] = id

            tmp[placetype] = {
                'role': role,
                'parent': parent,
                'name': placetype,
                'names': {}
            }

            for k, v in data.items():

                if not k.startswith("name:"):
                    continue
                    
                ignore, lang = k.split("name:")
                tmp[ placetype ]['names'][ lang ] = v

    spec = {}

    for placetype, details in tmp.items():

        id = placetype_map[ placetype ]
        parent = []

        for p_placetype in details.get('parent', []):

            p_id = placetype_map[ p_placetype ]
            parent.append(p_id)
        
        details['parent'] = parent
        spec[id] = details

    # print pprint.pformat(spec)
    
    print(json.dumps(spec))
    sys.exit()
