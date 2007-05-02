%define name nautilus-actions
%define version 1.4.1
%define rel 1
%define release %mkrel %rel
#fixed2
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}

Summary: Configurable context menu for Nautilus
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp2.grumz.net/grumz/%{name}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/GNOME
Url: http://www.grumz.net/?q=taxonomy/term/2/9
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: nautilus-devel >= 2.8.0
BuildRequires: e2fsprogs-devel
BuildRequires: intltool
Requires: nautilus

%description
Nautilus actions is an extension for Nautilus, the gnome file
manager. It allow to configure program to be launch on files selected
into Nautilus interface.

%prep
%setup -q

%build
%configure2_5x --with-nautilus-extdir=%_libdir/nautilus/extensions-1.0/ \
%if %mdkversion <= 1020
--disable-commandline-tool
%endif

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/nautilus/extensions-1.0/libnautilus-actions.la
%find_lang %name
%clean
rm -rf $RPM_BUILD_ROOT

%post
gtk-update-icon-cache --force --quiet %{_datadir}/icons/hicolor
%postun
if [ -x %{_bindir}/gtk-update-icon-cache ]; then 
  gtk-update-icon-cache --force --quiet %{_datadir}/icons/hicolor
fi

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%if %mdkversion > 1020
%_bindir/nautilus-actions-convert
%_bindir/nautilus-actions-new-config
%endif
%_bindir/nautilus-actions-config
%_datadir/applications/nact.desktop
%_libdir/nautilus/extensions-1.0/libnautilus-actions.so
%_datadir/%name
%_datadir/icons/hicolor/*/apps/%name.*
