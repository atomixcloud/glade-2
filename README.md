Glade-2
=======
GUI builder for the GTK and GNOME versions 2.
This repository is built from the source [Glade-2.12](https://download.gnome.org/sources/glade/2.12/glade-2.12.2.tar.gz)

Build from source
-----------------
**Dependencies:**<br>
`libxml2-dev` and `scrollkeeper`.

**Make and Install:**<br>
Follow below steps inside `glade-2-12.2` directory.
1. Configure package `./configure`
2. Compile package `make`
3. Install package `sudo make install`
4. Uninstall package `sudo make uninstall`

Build Debian Package
--------------------
Follow below steps inside `glade-2-12.2` directory.
1. Debianizes the source with `debmake -t -p glade-2 -u 12.2 -r 0 -x 1`
2. Build Debian package from the debianized source with `debuild -b -uc -us`
