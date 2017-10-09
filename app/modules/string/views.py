

__author__    = "Copyright (c) 2017, Marin Software>"
__copyright__ = "Licensed under GPLv2 or later."


from flask import Blueprint, request, jsonify, render_template

stringProcessorAPI = Blueprint('stringProcessorAPI', __name__, url_prefix='/api/string')

# API
@stringProcessorAPI.route('/reverse/<string_to_reverse>', methods=['GET'])
# retrieves/adds polls from/to the database
def reverse_string(string_to_reverse):
    return string_to_reverse
