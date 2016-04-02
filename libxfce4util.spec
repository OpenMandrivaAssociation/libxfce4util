%define url_ver %(echo %{version} | cut -d. -f1,2)
%define major 7
%define libname %mklibname xfce4util %{major}
%define develname %mklibname xfce4util -d

Summary:	Utility library for the Xfce desktop environment
Name:		libxfce4util
Version:	4.12.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	gtk-doc
BuildRequires:	xfce4-dev-tools >= 4.12.0

%description
Basic utility non-GUI functions for Xfce desktop environment.

%package -n %{libname}
Summary:	Utility library for the Xfce desktop environment
Group:		Graphical desktop/Xfce
Requires:	xdg-user-dirs
Requires:	%{name}-common = %{version}-%{release}
Conflicts:	xfce-utils <= 4.8.3-1

%description -n %{libname}
Utility library for the Xfce desktop environment.

%package common
Summary:	Common files for Xfce utility library
Group:		Graphical desktop/Xfce
BuildArch:	noarch
Conflicts:	%{mklibname xfce4util} < 4.8.2-3
Conflicts:	libxfce4util4 < 4.8.2-3
Conflicts:	lib64xfce4util4 < 4.8.2-3
Conflicts:	libxfce4util4-common < 4.8.2-3
Conflicts:	lib64xfce4util4-common < 4.8.2-3
Conflicts:	xfce-utils <= 4.8.3-1
Obsoletes:	%{name}4-common < 4.8.2-3

%description common
Common files for %{name}.

%package -n %{develname}
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	xfce4-dev-tools >= 4.9.0
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname xfce4util 4 -d}

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

%build
%configure \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files common -f %{name}.lang
%doc AUTHORS ChangeLog TODO

%files -n %{develname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/xfce4
%{_includedir}/xfce4/%{name}
%{_datadir}/gtk-doc/html/*

%files -n xfce-kiosk
%{_sbindir}/xfce4-kiosk-query
