from distutils.core import setup
setup(
  name = 'openstreetmap_mapping',         # How you named your package folder (MyLib)
  packages = ['openstreetmap_mapping'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='BSD License',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This library allows you to pull data from OpenStreetMap and plot it',   # Give a short description about your library
  author = 'Charlie Plumley',                   # Type in your name
  author_email = 'charlie.plumley@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/charlie9578/openstreetmap-mapping',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/charlie9578/openstreetmap-mapping/*****',    # Found under the release version on GitHub
  keywords = ['openstreetmap','google earth', 'kml','map','geospatial'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'pandas',
          'numpy',
          'bokeh',
          'pyproj',
          'simplekml',
          'matplotlib'
          'scipy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: BSD License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)