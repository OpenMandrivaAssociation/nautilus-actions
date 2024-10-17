%define major 1
Summary: Configurable context menu for Nautilus
Name:    nautilus-actions
Version: 3.2.2
Release: 2
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://www.nautilus-actions.org/
BuildRequires: nautilus-devel >= 2.8.0
BuildRequires: unique-devel
BuildRequires: libgtop2.0-devel
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(libSM)
BuildRequires: pkgconfig(uuid)
BuildRequires: intltool
BuildRequires: pkgconfig(gnome-doc-utils)
BuildRequires: gnome-common
BuildRequires: rarian
BuildRequires: docbook-dtd45-xml
Requires: nautilus

%description
Nautilus actions is an extension for Nautilus, the gnome file
manager. It allow to configure program to be launch on files selected
into Nautilus interface.

%package devel
Group: Development/C
Summary: Development files of %name
Requires: %name = %version-%release

%description devel
Install this if you want to build extensions for %name.


%prep
%setup -q
%autopatch -p1

%build
%configure2_5x --disable-schemas-install
%make

%install
rm -rf %{buildroot} %name.lang
%makeinstall_std
rm -f %buildroot%_libdir/{nautilus/extensions-3.0,%name}/lib*.la
rm -rf %buildroot%_datadir/doc/%{name}*
%find_lang %name 
%find_lang nautilus-actions-config-tool --with-gnome
cat nautilus-actions-config-tool.lang >> %name.lang

%triggerun -- %name < 3.1.0
%_libdir/%name/na-gconf2key.sh -delete -nodummy &>/dev/null ||:

%files -f %name.lang
%doc AUTHORS README TODO NEWS MAINTAINERS
%doc docs/objects-hierarchy.odg
%_bindir/*
%_datadir/applications/*.desktop
%_libdir/nautilus/extensions-3.0/libnautilus-actions-menu.so
%_libdir/nautilus/extensions-3.0/libnautilus-actions-tracker.so
%_datadir/%name
%_datadir/icons/hicolor/*/apps/%name.*
%_libdir/%name

%files devel
%_includedir/%name
%_datadir/gtk-doc/html/nautilus-actions-3/
