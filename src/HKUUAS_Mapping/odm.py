"""
ODM module

Communicates with NodeODM node opened in a docker container
Command to start a NodeODM node
    docker run -ti -p 3000:3000 opendronemap/nodeodm

Documentation:
    https://pyodm.readthedocs.io/en/latest/
Code Example:
    https://github.com/OpenDroneMap/PyODM/blob/master/examples/create_task.py
"""

import os
from pathlib import Path
# import sys
# sys.path.append('..')
from pyodm import Node, exceptions

default_parameters = {
    "fast-orthophoto": True,
    "feature-quality": "lowest",
    "max-concurrency": 4,
    "pc-quality": "lowest",
    "orthophoto-resolution": 4,
    "pc-tile": True,
    "skip-report": True
}


def run(images_path, parameters = default_parameters):
    # Add resized images into a list
    images = []
    dirs = os.listdir(images_path)
    for item in dirs:
        if os.path.isfile(images_path + item):
            images.append(images_path + item)
    
    # Save path for results: parent directory of images_path
    path = Path(images_path)
    results_path = path.parent.absolute()

    node = Node("localhost", 3000)

    try:
        # Start a task
        print("Uploading images...")
        task = node.create_task(images, parameters)
        print(task.info())

        try:
            # This will block until the task is finished
            # or will raise an exception
            task.wait_for_completion()

            print("Task completed, downloading results...")

            # Retrieve results
            task.download_assets(results_path)

            print("Assets saved in {}".format(results_path))
        except exceptions.TaskFailedError as e:
            print("\n".join(task.output()))

    except exceptions.NodeConnectionError as e:
        print("Cannot connect: %s" % e)
    except exceptions.NodeResponseError as e:
        print("Error: %s" % e)