from setuptools import setup


setup(
    name='mezzanine-slides',
    version='1.1.0',
    license='Simplified BSD',

    install_requires=[
        'Mezzanine >= 1.4.16',
        'six >= 1.5.2'],

    description='Easily plug a slideshow into your mezzanine website on all pages.',
    long_description=open('README.rst').read(),

    author='James Pells',
    author_email='jimmy@jamespells.com',

    url='http://github.com/jpells/mezzanine-slides',

    include_package_data=True,

    packages=['mezzanine_slides'],

    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django'])