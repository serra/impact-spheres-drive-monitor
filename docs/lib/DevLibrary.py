import pkg_resources


class DevLibrary:

    def __init__(sefl):
        pass

    def all_dependencies_should_be_installed(self):
        with open('requirements.txt') as reqs:
            pkg_resources.require(reqs)
