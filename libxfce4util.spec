%define url_ver %(echo %{version} | cut -c 1-3)
%define major 4
%define libname %mklibname xfce4util %{major}
%define develname %mklibname xfce4util -d

Summary:	Utility library for the Xfce desktop environment
Name:		libxfce4util
Version:	4.8.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-4.4.2-config-dirs.patch
BuildRequires:	glib2-devel >= 2.14.0
BuildRequires:	xfce4-dev-tools >= 4.6.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Basic utility non-GUI functions for Xfce desktop environment.

%package -n %{libname}
Summary:	Utility library for the Xfce desktop environment
Group:		Graphical desktop/Xfce
Requires:	xdg-user-dirs

%description -n %{libname}
Utility library for the Xfce desktop environment.

%package -n %{develname}
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	gtk-doc
Requires:	xfce4-dev-tools >= 4.6.0
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname xfce4util 4 -d

%description -n %{develname}
Libraries and header files for the %{name} library.

%package -n xfce-kiosk
Summary:	Kiosk support for the Xfce desktop environment
Group:		Graphical desktop/Xfce
Requires:	%{libname} = %{version}-%{release}

%description -n xfce-kiosk
Kiosk support for the Xfce desktop environment.

%prep
%setup -q
%if %mdkversion < 200900
%patch0 -p1
%endif

%build
%configure2_5x \
%if %mdkversion < 200900
	--sysconfdir=%{_sysconfdir}/X11
%endif

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname} -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog TODO
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/*a
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/xfce4
%{_includedir}/xfce4/%{name}
%{_datadir}/gtk-doc/html/*

%files -n xfce-kiosk
%defattr(-,root,root)
%{_sbindir}/xfce4-kiosk-query
