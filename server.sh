#!/bin/bash

export FLASK_APP=sensor
export FLASK_DEBUG=false
export SENSOR_SETTINGS=config.py

pushd /opt/Sensor

waitress-serve --port=8080 sensor:app

popd
