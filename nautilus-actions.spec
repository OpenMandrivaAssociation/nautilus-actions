%define name nautilus-actions
%define version 1.10.1
%define release %mkrel 1

Summary: Configurable context menu for Nautilus
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://pwi.dyndns.biz/tarballs/nautilus-actions/%{name}-%{version}.tar.gz
Patch2: nautilus-actions-r510-fix-desktop-entry.patch
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.nautilus-actions.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: nautilus-devel >= 2.8.0
BuildRequires: libgnomeui2-devel
BuildRequires: e2fsprogs-devel
BuildRequires: intltool
BuildRequires: gnome-common
Requires: nautilus

%description
Nautilus actions is an extension for Nautilus, the gnome file
manager. It allow to configure program to be launch on files selected
into Nautilus interface.

%prep
%setup -q
%patch2 -p0

%build
%configure2_5x --enable-commandline-tool
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/nautilus/extensions-2.0/libnautilus-actions.la
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%postun
%clean_icon_cache hicolor

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%_bindir/nautilus-actions-check-actions-change
%_bindir/nautilus-actions-new-config
%_bindir/nautilus-actions-config
%_datadir/applications/nact.desktop
%_libdir/nautilus/extensions-2.0/libnautilus-actions.so
%_datadir/%name
%_datadir/icons/hicolor/*/apps/%name.*
