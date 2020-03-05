import platform

from flask import jsonify


def get_python_version():

    p = platform.python_version()

    pinfo = {"python version": p}

    return jsonify(pinfo)