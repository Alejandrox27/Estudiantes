from setuptools import setup

setup(name = 'notas estudiantes',version = '1.0.0',packages = ['notas_estudiantes'], 
      entry_points = {'console_scripts': ['notas estudiantes = notas_estudiantes.__main__:main']})