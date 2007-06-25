%define major 4
%define libname %mklibname xfce4util %{major} 
%define develname %mklibname xfce4util -d

Summary:	Utility library for the Xfce4 desktop environment
Name:		libxfce4util
Version:	4.4.1
Release:	%mkrel 3
License:	BSD
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk-doc
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Basic utility non-GUI functions for Xfce4.

%package -n %{libname}
Summary:	Utility library for the Xfce4 desktop environment
Group:		Graphical desktop/Xfce

%description -n %{libname}
Utility library for the Xfce4 desktop environment.

%package -n %{develname}
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	gtk-doc
Requires:	xfce-dev-tools
Requires:	%{libname} = %{version}-%{release}
Provides:	xfce4util-devel = %{version}-%{release}
Obsoletes:	%mklibname xfce4util 4 -d

%description -n %{develname}
Libraries and header files for the %{name} library.

%prep
%setup -q

%build
%configure2_5x \
	--sysconfdir=%{_sysconfdir}/X11
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# (mpol) 4.1.99.1: remove for now
rm -f %{buildroot}%{_sbindir}/xfce4-kiosk-query

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname} -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING TODO
%{_libdir}/lib*.so.%{major}*
%{_datadir}/gtk-doc/html/*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/*a
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/xfce4
%{_includedir}/xfce4/%{name}
