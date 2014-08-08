pyFolia
=======

description
-----------
a fun tool to help nerdy gardeners win at life

geocoder
--------
usage:

$ python geocode.py "oranienstrasse 183"

sample output: 

52.5007674, 13.4206237

revese geocoder
---------------
usage:

$ reverse.py "oranienstrasse 183"

sample output: 

Oranienstraße 184, 10999 Berlin, Germany

myFolia scraper
---------------
usage:

$ python myFolia.py carrot

sample output:

{u'Bloom Time': u'Help build our wiki!',
 u'Can Sow Direct?': u'Yes',
 u'Category': u'Biennial',
 u'Country of Origin': u'Afghanistan',
 u'Difficulty': u'Easy 2/5',
 u'Growing Temperatures': u'Help build our wiki!',
 u'Growth Habit': u'Erect',
 u'Hardiness': u'Very Hardy',
 u'Harvest Time': u'Late Spring',
 u'Ideal Germination Temperature Range': u'16\xb0C / 61\xb0F',
 u'Lifecycle': u'Biennial',
 u'Mature Height': u'15.0 cm / 5.85 inches',
 u'Mature Spread': u'2.5 cm / 0.98 inches',
 u'Nitrogen Requirements': u'Medium',
 u'Planting Distance Apart': u'5.0 cm / 1.95 inches',
 u'Planting Row Distance Apart': u'5.0 cm / 1.95 inches',
 u'Pruning Time': u'Late Spring',
 u'Soil': u'Loam',
 u'Sowing Depth': u'0.6 cm / 0.23 inches',
 u'Sowing Distance Apart': u'1.0 cm / 0.39 inches',
 u'Sowing Row Distance Apart': u'Help build our wiki!',
 u'Sun': u'Full Sun',
 u'USDA Zone Range': u'Zone 3\n          \n          to\n          \n          Zone 11',
 u'Water Requirements': u'High',
 'dislike': [u'/plants/856-parsnip-pastinaca-sativa'],
 'like': [u'/plants/10-tomato-solanum-lycopersicum',
          u'/plants/35-bean-phaseolus-vulgaris',
          u'/plants/3325-flax-linum-usitatissimum',
          u'/plants/911-onion-allium-cepa-var-cepa',
          u'/plants/3585-allium-allium'],
 'love': [u'/plants/40-rosemary-rosmarinus-officinalis',
          u'/plants/29-sage-salvia-officinalis',
          u'/plants/81-french-marigold-tagetes-patula',
          u'/plants/6-lettuce-lactuca-sativa',
          u'/plants/920-chives-allium-schoenoprasum',
          u'/plants/523-radish-raphanus-sativus',
          u'/plants/82134-african-wormwood-artemisia-afra'],
 u'pH Range': u'6.0 - 6.5'}


virtualenv
----------

Virtualenv to the rescue! Virtualenv enables multiple side-by-side installations of Python, one for each project. It doesn’t actually install separate copies of Python, but it does provide a clever way to keep different project environments isolated. Let’s see how virtualenv works.

If you are on Mac OS X or Linux, chances are that one of the following two commands will work for you:

$ sudo easy_install virtualenv

or even better:

$ sudo pip install virtualenv

One of these will probably install virtualenv on your system. Maybe it’s even in your package manager. If you use Ubuntu, try:

$ sudo apt-get install python-virtualenv

If you are on Windows and don’t have the easy_install command, you must install it first. Check the pip and distribute on Windows section for more information about how to do that. Once you have it installed, run the same commands as above, but without the sudo prefix.

Once you have virtualenv installed, just fire up a shell and create your own environment. I usually create a project folder and a venv folder within:

$ mkdir myproject
$ cd myproject
$ virtualenv venv
New python executable in venv/bin/python
Installing distribute............done.

Now, whenever you want to work on a project, you only have to activate the corresponding environment. On OS X and Linux, do the following:

$ . venv/bin/activate

If you are a Windows user, the following command is for you:

$ venv\scripts\activate

Installing Requirements
-----------------------
pip install -r requirements.txt

