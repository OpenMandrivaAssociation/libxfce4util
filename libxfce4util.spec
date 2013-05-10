%define url_ver %(echo %{version} | cut -d. -f1,2)
%define major 6
%define libname %mklibname xfce4util %{major}
%define develname %mklibname xfce4util -d

Summary:	Utility library for the Xfce desktop environment
Name:		libxfce4util
Version:	4.10.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://www.xfce.org
Source0:	http://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	glib2-devel >= 2.14.0
BuildRequires:	xfce4-dev-tools >= 4.9.0

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
%configure2_5x \
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

%changelog
* Mon Apr 30 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.10.0-1
+ Revision: 794635
- update to new version 4.10.0

* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.1-1
+ Revision: 791035
- update to new version 4.9.1

* Sat Apr 07 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.0-3
+ Revision: 789636
- add conflicts on xfce-utils

* Tue Apr 03 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.0-2
+ Revision: 789086
- do not require gtk-doc

* Mon Apr 02 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.9.0-1
+ Revision: 788880
- bump major to 6
- drop patch0
- bump requires on xfce4-dev-tools to 4.9.0 version
- update to new version 4.9.0
- bump requires to 4.9.0 on xfce4-dev-tools
- remole old stuff from spec file

* Tue Dec 27 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.2-3
+ Revision: 745794
- make common subpackage noarch (this forces to add Conflicts on old common subpackage)

* Tue Dec 27 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.2-2
+ Revision: 745779
- move locales and doc files from libname to a common subpackage
- disable build of static libraries
- spec file clean

* Thu Sep 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.2-1
+ Revision: 700789
- update to new version 4.8.2

* Tue Jan 18 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.8.1-1
+ Revision: 631568
- update to new version 4.8.1
- update to new version 4.8.0

* Thu Jan 06 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.5-1mdv2011.0
+ Revision: 629086
- update to new version 4.7.5

* Sat Dec 04 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.4-1mdv2011.0
+ Revision: 609272
- update to new version 4.7.4

* Sat Nov 06 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.3-1mdv2011.0
+ Revision: 593793
- update to new version 4.7.3

* Fri Sep 17 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.7.2-1mdv2011.0
+ Revision: 579266
- update to new version 4.7.2
- handle new url for SOurce0

* Sun Jul 11 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.2-1mdv2011.0
+ Revision: 551020
- update to new version 4.6.2

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-2mdv2010.1
+ Revision: 543214
- rebuild for mdv 2010.1

* Tue Apr 21 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.1-1mdv2010.0
+ Revision: 368569
- update to new version 4.6.1

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.6.0-2mdv2009.1
+ Revision: 349159
- rebuild whole xfce

* Fri Feb 27 2009 Jérôme Soyer <saispo@mandriva.org> 4.6.0-1mdv2009.1
+ Revision: 345519
- New upstream release

* Mon Jan 26 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.99.1-1mdv2009.1
+ Revision: 333846
- update to new version 4.5.99.1

* Wed Jan 14 2009 Jérôme Soyer <saispo@mandriva.org> 4.5.93-1mdv2009.1
+ Revision: 329495
- New upstream release

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - add full path for the Source0

* Sat Nov 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.92-1mdv2009.1
+ Revision: 303460
- update to new version 4.5.92 (Xfce 4.6 Beta 2 Hopper)

* Tue Nov 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-2mdv2009.1
+ Revision: 302180
- rebuild

* Wed Oct 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.5.91-1mdv2009.1
+ Revision: 294012
- versioned requires
- Xfce4.6 beta1 is landing on cooker

* Thu Sep 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-10mdv2009.0
+ Revision: 285642
- drop patch 1, not needed anymore

* Sun Sep 14 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-9mdv2009.0
+ Revision: 284702
- Patch1: new version (from xfce upstream bug #4365)

* Mon Sep 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-8mdv2009.0
+ Revision: 282567
- Patch1: add support for XDG user dirs
- raise glib2-devel minimal version to 2.14.0

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 4.4.2-7mdv2009.0
+ Revision: 268060
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun May 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-6mdv2009.0
+ Revision: 205575
- change sysconfdir from /etc/X11/xdg to /etc/xdg only for Mandriva releases newer than 2008.1

* Sun May 04 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-5mdv2009.0
+ Revision: 201026
- Patch0: add /etc/X11/xdg to config dirs

* Sun Jan 27 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-4mdv2008.1
+ Revision: 158499
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-3mdv2008.1
+ Revision: 110710
- remove buildrequires on gtk-doc
- update summary and description
- do not package COPYING
- move gtk docs to the devel package

* Sun Nov 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-2mdv2008.1
+ Revision: 109940
- requires now xfce4-dev-tools

* Sun Nov 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.2-1mdv2008.1
+ Revision: 109928
- Xfce 4.4.2 is landing on Mandriva repositories ;)
- add missing requires for kiosk

* Mon Jun 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-3mdv2008.0
+ Revision: 44110
- move translation files to the main library
- enable kiosk support
- new devel library policy
- correct provides/obsoletes

* Mon May 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.4.1-2mdv2008.0
+ Revision: 32205
- drop __libtoolize and __cputoolize
- spec file clean

* Tue Apr 17 2007 Jérôme Soyer <saispo@mandriva.org> 4.4.1-1mdv2007.1
+ Revision: 13607
- new release 4.4.1


* Tue Jan 23 2007 plouf <plouf> 4.4.0-1mdv2007.0
+ Revision: 112306
- New release 4.4.0

* Wed Dec 06 2006 Jérôme Soyer <saispo@mandriva.org> 4.3.99.2-1mdv2007.1
+ Revision: 91664
- update to 4.3.99.2

* Wed Dec 06 2006 Jérôme Soyer <saispo@mandriva.org> 4.3.90.2-1mdv2007.1
+ Revision: 91637
- Import libxfce4util

* Tue Jul 11 2006 Charles A Edwards <eslrahc@mandriva.org> 4.3.90.2-1mdv2006.0
- 4.3.90.2 (Xfce-4.4 beta2)
- bump major
- add lang

* Wed Apr 26 2006 Jerome Soyer <saispo@mandriva.or> 4.3.90.1-1mdk
- Tue Apr 18 2006 trem <trem@mandriva.org> 4.3.90.1-1mdk
- 4.3.90.1

* Mon Mar 06 2006 Marcel Pol <mpol@mandriva.org> 4.3.0-0.svn_r20246.1mdk
- svn r20246

* Sat Feb 04 2006 Marcel Pol <mpol@mandriva.org> 4.3.0-0.svn_r19739.2mdk
- devel package requires xfce-dev-tools for now

* Sat Feb 04 2006 Marcel Pol <mpol@mandriva.org> 4.3.0-0.svn_r19739.1mdk
- 4.3.0 svn r19739
- new major
- don't run libtoolize
- update filelist

* Fri Jan 13 2006 Marcel Pol <mpol@mandriva.org> 4.2.3.2-1mdk
- 4.2.3.2

* Wed May 25 2005 Marcel Pol <mpol@mandriva.org> 4.2.2-1mdk
- 4.2.2
- %%mkrel

* Wed Mar 16 2005 Charles A Edwards <eslrahc@mandrake.org> 4.2.1-1mdk
- 4.2.1

* Sat Jan 22 2005 Marcel Pol <mpol@mandrake.org> 4.2.0-2mdk
- group: Graphical desktop/Xfce

* Tue Jan 18 2005 Charles A Edwards <eslrahc@mandrake.org> 4.2.0-1mdk
- 4.2.0 Final

* Sat Dec 25 2004 Marcel Pol <mpol@mandrake.org> 4.1.99.3-1mdk
- 4.1.99.3 (4.2.0 RC 3)

* Sun Dec 12 2004 Charles A Edwards <eslrahc@mandrake.org> 4.1.99.2-1mdk
- 4.1.99.2 (4.2.0 RC 2)

* Tue Nov 16 2004 Marcel Pol <mpol@mandrake.org> 4.1.99.1-1mdk
- 4.1.99.1
- s/XFce/Xfce
- remove %%{_sbindir}/xfce4-kiosk-query for now
- add (build)requires for gtk-doc
- sysconfdir=%%_sysconfdir/X11

* Tue Jul 13 2004 Charles A Edwards <eslrahc@mandrake.org> 4.0.6-1mdk
- 4.0.6
- reenable libtoolize

* Sun Apr 18 2004 Charles A Edwards <eslrahc@mandrake.org> 4.0.5-1mdk
- 4.0.5

* Sat Apr 10 2004 Charles A Edwards <eslrahc@mandrake.org> 4.0.4-1mdk
- 4.0.4

