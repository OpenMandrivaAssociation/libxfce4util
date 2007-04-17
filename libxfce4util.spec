%define lib_major	4
%define lib_name	%mklibname xfce4util %{lib_major} 
%define version 	4.4.1
%define release 	1
%define __libtoolize	/bin/true
%define __cputoolize	/bin/true

Summary: 	Utility library for the Xfce4 desktop environment
Name: 		libxfce4util
Version: 	%{version}
Release: 	%mkrel %{release}
License:	BSD
URL: 		http://www.xfce.org/
Source0: 	%{name}-%{version}.tar.bz2
Group: 		Graphical desktop/Xfce
BuildRoot: 	%{_tmppath}/%{name}-root
BuildRequires: 	glib2-devel >= 2.0.0
BuildRequires:	gtk-doc

%description
Basic utility non-GUI functions for Xfce4.

%package -n %{lib_name}
Summary:	Utility library for the Xfce4 desktop environment
Group:		Graphical desktop/Xfce

%description -n %{lib_name}
Utility library for the Xfce4 desktop environment.

%package -n %{lib_name}-devel
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	gtk-doc
Requires:	xfce-dev-tools
Requires:	%{lib_name} = %{version}
Provides:       libxfce4util-devel = %{version}-%{release}

%description -n %{lib_name}-devel
Libraries and header files for the %{name} library.


%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --sysconfdir=%_sysconfdir/X11
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# (mpol) 4.1.99.1: remove for now
rm -f $RPM_BUILD_ROOT%{_sbindir}/xfce4-kiosk-query

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post  -n %{lib_name} -p /sbin/ldconfig

%postun  -n %{lib_name} -p /sbin/ldconfig


%files -n %{lib_name}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING TODO
%{_libdir}/lib*.so.*
%{_datadir}/gtk-doc/html/*
%files -n %{lib_name}-devel -f%{name}.lang
%defattr(-, root, root)
%{_libdir}/lib*.so
%{_libdir}/*a
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/xfce4
%{_includedir}/xfce4/%{name}


