## Process this file with automake to produce Makefile.in
## Created by Anjuta


uidir = $(pkgdatadir)/ui
ui_DATA = smssender_gtk.ui


## The main script
bin_SCRIPTS = smssender_gtk.py

## Directory where .class files will be installed
smssender_gtkdir = $(pythondir)/smssender_gtk


smssender_gtk_PYTHON = \
	smssender_gtk.py


EXTRA_DIST = $(ui_DATA)


# Remove ui directory on uninstall
uninstall-local:

	-rm -r $(uidir)

	-rm -r $(pkgdatadir)
