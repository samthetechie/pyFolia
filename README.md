pyFolia
=======

description
-----------
a fun tool to help nerdy gardeners win at life

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

