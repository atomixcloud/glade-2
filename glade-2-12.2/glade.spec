%define name    glade2
%define ver      2.12.2
%define  RELEASE SNAP
%define  rel     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}
%define prefix   /usr
%define sysconfdir	/etc
%define skreq           0.1.4

Summary: GUI builder for GTK+ and GNOME
Name: %{name}
Version: %ver
Release: %rel
License: GPL
Group: Development/Tools
Source: glade-%{ver}.tar.bz2
BuildRoot: %{_tmppath}/glade-%{ver}-root
URL: http://glade.gnome.org/
Docdir: %{prefix}/doc
Prefix: %prefix
BuildRequires: scrollkeeper >= %skreq

%description
Glade is a GUI builder for GTK+ and GNOME.

%prep
%setup -q -n glade-%{ver}

# The ALPHA architecture variable that was here should be fed in by the
# RPM-provided %configure macro
%configure

%build

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
# This checks a highly-unlikely scenario but ... what the heck ... it was
# already there.
[ %{buildroot} != "/" ] && rm -rf %{buildroot}

make DESTDIR=%{buildroot} PACKAGE_PIXMAPS_DIR=%{buildroot}%{_datadir}/pixmaps install

%clean
# ditto here
[ %{buildroot} != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README

%{_bindir}/glade-2
%{_datadir}/glade-2/gtk/*
%{_datadir}/gnome/help/glade-2/C/glade-faq.*
%{_datadir}/gnome/help/glade-2/C/glade-user-guide.*
%{_datadir}/gnome/help/glade-2/C/figures/*
%{_datadir}/gnome/help/glade-2/C/legal.xml
%{_datadir}/gnome/help/glade-2/ro/*.xml
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/omf/glade-2/*
%{_datadir}/pixmaps/glade-2/*
%{_datadir}/pixmaps/*.*
%{_datadir}/applications/glade-2.desktop

%post
if which scrollkeeper-update>/dev/null 2>&1; then scrollkeeper-update; fi

%postun
if which scrollkeeper-update>/dev/null 2>&1; then scrollkeeper-update; fi


%changelog
* Tue May 20 2003 Rolando Nieves <rjnieves@earthlink.net>
- Updated file locations in order to use the RPM-provided macros.
- Made use of other RPM-provided macros (such as %configure).

* Tue Oct 08 2002 Damon Chaplin <damon@kendo.fsnet.co.uk>
- Updated description and URL.

* Fri Sep 20 2002 Dermot Musgrove <dermot.musgrove@virgin.net>
- Changes to find doc files in new place

* Mon May 20 2002 Dermot Musgrove <dermot.musgrove@virgin.net>
- Changes to build glade-2

* Sun Mar 25 2001 Dan Mueth <dan@eazel.com>
- Added ScrollKeeper/OMF stuff

* Thu Jul 22 1999 Herbert Valerio Riedel <hvr@hvrlab.dhs.org>
- changed configure options in order to build on all alphas

* Wed Jun 23 1999 Jose Mercado <jmercado@mit.edu>
- Changed the Source variable to use %{var}.
- Fixed glade.desktop's path so rpm will find it.
