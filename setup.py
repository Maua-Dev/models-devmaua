from distutils.core import setup

setup(
    name='models-devmaua',
    version='0.0.8',
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
