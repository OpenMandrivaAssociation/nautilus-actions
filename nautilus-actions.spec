%define name nautilus-actions
%define version 1.12.0
%define release %mkrel 1

Summary: Configurable context menu for Nautilus
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0: nautilus-actions-1.11.2-fix-str-fmt.patch
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.nautilus-actions.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: nautilus-devel >= 2.8.0
BuildRequires: unique-devel
BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
%if %mdvver >= 201000
BuildRequires: libuuid-devel
%else
BuildRequires: e2fsprogs-devel
%endif
BuildRequires: intltool
BuildRequires: gnome-common
Requires: nautilus

%description
Nautilus actions is an extension for Nautilus, the gnome file
manager. It allow to configure program to be launch on files selected
into Nautilus interface.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --disable-schemas-install
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/nautilus/extensions-2.0/libnautilus-actions.la
rm -rf %buildroot%_datadir/doc/%{name}*
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_icon_cache hicolor
%postun
%clean_icon_cache hicolor
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS README TODO NEWS MAINTAINERS
%doc doc/objects-hierarchy.odg
%_bindir/*
%_datadir/applications/*.desktop
%_libdir/nautilus/extensions-2.0/libnautilus-actions.so
%_datadir/%name
%_datadir/icons/hicolor/*/apps/%name.*
