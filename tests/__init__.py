"""
lyricswelove test suite

The test suite requires the following::

    easy_install nose WebTest http://nose-gae.googlecode.com/svn/trunk/

The last one is a path to the noseGAE plugin (see http://code.google.com/p/nose-gae/) and it must be revision 25 or higher (currently 0.1.3a).
noseGAE sets up everything you need to run the pypione app in a simulated Google App Engine environment.

NOTE: as of this writing, issue6 (http://code.google.com/p/nose-gae/issues/detail?id=6) means you'll have to manually delete WebOb from your site-packages to get noseGAE to work.

Run the test suite with the nosetests (or nosetests-2.5) command from the root directory.
"""