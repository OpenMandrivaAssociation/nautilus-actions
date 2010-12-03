%define name nautilus-actions
%define version 3.0.2
%define release %mkrel 1

%define major 1
Summary: Configurable context menu for Nautilus
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0: nautilus-actions-3.0-linking.patch
Patch1: nautilus-actions-2.30.0-desktop-entry.patch
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.nautilus-actions.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: nautilus-devel >= 2.8.0
BuildRequires: unique-devel
BuildRequires: libgtop2.0-devel
BuildRequires: gtk+2-devel
BuildRequires: libGConf2-devel
%if %mdvver >= 201000
BuildRequires: libuuid-devel
%else
BuildRequires: e2fsprogs-devel
%endif
BuildRequires: intltool
BuildRequires: gnome-doc-utils
BuildRequires: gnome-common
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
%apply_patches
autoreconf

%build
%configure2_5x --disable-schemas-install
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
rm -f %buildroot%_libdir/{nautilus/extensions-2.0,%name}/lib*.la
rm -rf %buildroot%_datadir/doc/%{name}*
%find_lang %name
%find_lang nautilus-actions-config-tool --with-gnome
cat nautilus-actions-config-tool.lang >> %name.lang
for omf in %buildroot%_datadir/omf/*/*-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

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
%_libdir/nautilus/extensions-2.0/libnautilus-actions-menu.so
%_libdir/nautilus/extensions-2.0/libnautilus-actions-tracker.so
%_datadir/%name
%_datadir/icons/hicolor/*/apps/%name.*
%_libdir/%name
%dir %_datadir/gnome/help/nautilus-actions-config-tool
%_datadir/gnome/help/nautilus-actions-config-tool/C
%dir %_datadir/omf/nautilus-actions-config-tool
%_datadir/omf/nautilus-actions-config-tool/nautilus-actions-config-tool-C.omf

%files devel
%defattr(-,root,root)
%_includedir/%name
%_datadir/gtk-doc/html/nautilus-actions-3
