from app.modules.string.stringProcessor import StringProcessor
from flask import Blueprint, jsonify

stringProcessorAPI = Blueprint('stringProcessorAPI', __name__, url_prefix='/api/string')


@stringProcessorAPI.route('/reverse_and_merge/<original_string>', methods=['GET'])
def reverse_and_merge_string(original_string):

    result_string = StringProcessor.reverse_and_merge(original_string)
    # result = {
    #     "original": original_string,
    #     "result": result_string,
    #     "action": 'reverse_and_merge'
    # }

    return result_string
    # return jsonify(result)