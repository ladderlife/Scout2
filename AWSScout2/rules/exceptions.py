# -*- coding: utf-8 -*-
"""
Exceptions handling
"""

import json


def process_exceptions(aws_config, exceptions_filename = None):
    """
    DDDD

    :param aws_config:
    :param exceptions_filename:
    :return:
    """

    # Load exceptions
    if not exceptions_filename:
        return
    with open(exceptions_filename, 'rt') as f:
        exceptions = json.load(f)

        target = open('foo2.json', 'w')
        target.write(json.dumps(aws_config))
        target.close()

        key = 'findings' # used to be 'violations'

    # Process exceptions
        for service in exceptions['services']:
            for rule in exceptions['services'][service]['exceptions']:
                filtered_items = []
                for item in aws_config['services'][service][key][rule]['items']:
                    if item not in [
                        item if isinstance(item, basestring) else item['id']
                        for item in exceptions['services'][service]['exceptions'][rule]
                    ]:
                        filtered_items.append(item)
                aws_config['services'][service][key][rule]['items'] = filtered_items
                aws_config['services'][service][key][rule]['flagged_items'] = len(aws_config['services'][service][key][rule]['items'])