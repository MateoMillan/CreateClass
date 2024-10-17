from setuptools import setup, find_packages

setup(
    name='mi_modulo',
    version='0.1',
    packages=find_packages(),
    description='Una descripción breve de tu módulo',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MateoMillan',  # URL de tu proyecto
    author='Tu Nombre',
    author_email='mateo4millan@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)