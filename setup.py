from setuptools import setup

requirements = [l.strip() for l in open('requirements.txt').readlines()]

setup(
    name='spell-tutor',
    version='0.1',
    description='Spellings learning tool',
    license="Proprietary",
    classifiers=['License :: Other/Proprietary License'],
    packages=['spelltutor'],
    install_requires=requirements,
    include_package_data=True,
    test_suite="tests",
    author="Dheeraj Kumar YMV",
    author_email="dheeruymv1212@gmail.com"
)
