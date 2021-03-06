from setuptools import setup


try:
    import pypandoc

    description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    description = open('README.md').read()

setup(
    name='restapi-logging-handler',
    version='0.2.8.2',
    description='A handler for the python logging module that sends logs \
        through any REST-ful API. With threading and Loggly support that \
        handles batch POSTS.',
    long_description=description,
    packages=['restapi_logging_handler'],

    author='James DuPont',
    author_email='james.dupont@nrg.com',
    url='https://github.com/jdrng/restapi-logging-handler.git',
    download_url=(
        'https://github.com/jdnrg/restapi-logging-handler/archive/v0.2.8.2.tar.gz'
    ),
    keywords=['rest', 'api', 'logging', 'handler', 'loggly'],
    classifiers=[],
    license='MIT',
    test_suite='nose.collector',
    tests_require=['nose'],
)
