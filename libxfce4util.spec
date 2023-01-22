%define url_ver %(echo %{version} | cut -d. -f1,2)
%define major 7
%define libname %mklibname xfce4util %{major}
%define develname %mklibname xfce4util -d
%define girname %mklibname %{name}-gir


Summary:	Utility library for the Xfce desktop environment
Name:		libxfce4util
Version:	4.18.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  gettext
#BuildRequires:	gtk-doc
BuildRequires:	xfce4-dev-tools >= 4.17.0

%description
Basic utility non-GUI functions for Xfce desktop environment.

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	Utility library for the Xfce desktop environment
Group:		Graphical desktop/Xfce
Requires:	xdg-user-dirs
Requires:	%{name}-common = %{version}-%{release}
Conflicts:	xfce-utils <= 4.8.3-1

%description -n %{libname}
Utility library for the Xfce desktop environment.

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

#---------------------------------------------------------------------------

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

%files common -f %{name}.lang
%doc AUTHORS ChangeLog TODO README.md

#---------------------------------------------------------------------------

%package -n %{develname}
Summary:	Libraries and header files for the %{name} library
Group:		Development/Other
Requires:	xfce4-dev-tools >= 4.9.0
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname xfce4util 4 -d}

%description -n %{develname}
Libraries and header files for the %{name} library.

%files -n %{develname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/xfce4
%{_includedir}/xfce4/%{name}
%{_datadir}/gtk-doc/html/*
%{_datadir}/gir-1.0/Libxfce4util-1.0.gir
%{_datadir}/vala/vapi/libxfce4util-1.0.vapi

#---------------------------------------------------------------
%package -n %{girname}
Summary: GObject Introspection interface for %{name}
Group: System/Libraries
Requires: %{libname} >= %{EVRD}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%files -n %{girname}
%{_libdir}/girepository-1.0/Libxfce4util-1.0.typelib

#---------------------------------------------------------------------------

%package -n xfce-kiosk
Summary:	Kiosk support for the Xfce desktop environment
Group:		Graphical desktop/Xfce
Requires:	%{libname} = %{version}-%{release}

%description -n xfce-kiosk
Kiosk support for the Xfce desktop environment.

%files -n xfce-kiosk
%{_sbindir}/xfce4-kiosk-query

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

# locales
%find_lang %{name} %{name}.lang
