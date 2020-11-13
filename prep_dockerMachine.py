import subprocess


def dockerMachine():
    nodes = ["node1", "node2", "node3"]

    for node in nodes:
            createNodes = ("docker-machine create --driver virtualbox {node}".format(node=node))
            subprocess.call([createNodes], shell=True)

dockerMachine()    