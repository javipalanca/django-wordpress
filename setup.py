from distutils.core import setup
import wordpress

long_description = open('README.rst').read()

setup(
    name='the-real-django-wordpress',
    version=wordpress.__version__,
    description='Django models and views for a WordPress database.',
    long_description=long_description,
    author='Javi Palanca',
    author_email='jpalanca@dsic.upv.es',
    url='http://github.com/javipalanca/django-wordpress/',
    packages=['wordpress'],
    package_data={'wordpress': ['templates/wordpress/*']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
    license='BSD License',
    platforms=["any"],
)
