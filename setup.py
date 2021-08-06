import json
from distutils.core import setup

def getConfig():
    with open("config.json") as configFile:
        configJson = json.load(configFile)
        configFile.close()
        return configJson


def getVersaoMerge():
    configJson = getConfig()
    return configJson["mergeVersion"]

setup(
    name='models-devmaua',
    version=f'0.0.{getVersaoMerge()}',
    packages=['devmaua', 'devmaua.src', 'devmaua.src.enum', 'devmaua.src.main', 'devmaua.src.models', 'devmaua.test',
              'devmaua.test.models', 'devmaua.src.models.erros'],
    url='https://github.com/Maua-Dev/models-devmaua',
    license='',
    author='Dev Comunity Mauá',
    install_requires=[
          'pydantic',
      ],

    author_email='',
    description=''
)
