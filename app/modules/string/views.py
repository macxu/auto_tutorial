

__author__    = "Copyright (c) 2017>"
__copyright__ = "Licensed under GPLv2 or later."


from flask import Blueprint, jsonify

stringProcessorAPI = Blueprint('stringProcessorAPI', __name__, url_prefix='/api/string')


@stringProcessorAPI.route('/reverse/<string_to_reverse>', methods=['GET'])
def reverse_string(string_to_reverse):

    reversed_string = string_to_reverse[::-1]
    result = {
        "original": string_to_reverse,
        "result": reversed_string
    }

    return jsonify(result)
