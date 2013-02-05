neuroim_flavour
===============

A CloudBioLinux (CBL) flavour for installing extras needed by
neuroimaging clusters. For the nectar cloud.

Based on Enis' GVL flavour.

Installation
------------
To install, first clone CBL from [its Git repository][4] (if you have already
done that). Then, change into ``cloudbiolinux/contrib/flavor/`` directory and
clone this flavor:

    $ cd <project_home>
    $ git clone https://github.com/chapmanb/cloudbiolinux.git
    $ cd cloudbiolinux/contrib/flavor
    $ git clone https://github.com/richardbeare/neuroim_flavor.git neuroim

The two repositories will be kept separate (depending on the contents of
your ``.gitignore`` file in the cloudbiolinux repository root directory
(i.e., ``<project_home>``), git may mark ``contrib/flavor/neuroim`` as
untracked files, but no need to worry about that - you can add that
directory to your ``.gitignore`` or leave it as is. However, do not add/commit
gvl flavor files into the cloudbiolinux repository).

The reason for having separate repositories is because
``neuroim_flavor`` code depends on CBL, but CBL code does not depend
on the ``neuroim_flavor`` code.  As a result, having these two
repositories separate and independently versioned, it allows them to
be managed independently (i.e., ``neuroim_flavor`` can be versioned
but does not have to become part of the main CBL source).

Use
---
The flavor is used as part of invoking CBL scripts. To adjust the settings the flavor defines,
edit the following files (all in ``<project_home>/cloudbiolinux/contrib/flavor/neuroim`` directory):

* ``main.yaml`` - to define the list of meta-packages to be
  installed
* ``packages.yaml`` - to define the exact list of system packages to be
  installed (this is in part defined by the list from ``main.yaml``)
* ``*-libs.yaml`` - to define specific language libraries to be installed
  (this is in part defined by the list from ``main.yaml``)
* ``tools.yaml`` - to define a list of tools and their versions that will be
  installed as Galaxy-dependencies
* ``fabricrc.txt`` - to define the paths where software should be installed on
  the remote system

Once all the configuration has been done run the CBL scripts:

    $ fab -i <key> -H ubuntu@<IP> -c contrib/flavor/neuroim/fabricrc.txt install_biolinux:flavor=neuroim

Once all the packages and libraries have been installed, clean the image and
then create a snapshot from it via the cloud console:

    $ fab -i <key> -H ubuntu@<IP> install_biolinux:target=cleanup

[1]: http://cloudbiolinux.org/
[2]: http://nectar.org.au/research-cloud
[3]: https://github.com/chapmanb/cloudbiolinux

