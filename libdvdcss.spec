Summary:	A library for transparent DVD device access with on-the-fly CSS decryption
Name:		libdvdcss
Version:	1.2.10
Release:	1%{?dist}
License:	GPLv2+
Group:		System Environment/Libraries
URL:		http://www.videolan.org/developers/libdvdcss.html
Source0:	http://download.videolan.org/pub/libdvdcss/%{version}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
BuildRequires:	doxygen

%package devel
Summary:	Development files for the libdvdcss
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description
libdvdcss is a cross-platform library for transparent DVD device
access with on-the-fly CSS decryption. It currently runs under Linux,
FreeBSD, NetBSD, OpenBSD, BSD/OS, Solaris, BeOS, Win95/Win98,
Win2k/WinXP, MacOS X, HP-UX, QNX, and OS/2. It is used by libdvdread
and most DVD players such as VLC because of its portability and
because, unlike similar libraries, it does not require your DVD drive
to be region locked.

%description devel
libdvdcss is a cross-platform library for transparent DVD device
access with on-the-fly CSS decryption. 
This package contains files to develop with libdvdcss.

%prep
%setup -q
pushd src/dvdcss
iconv -f iso8859-1 -t utf8 dvdcss.h > dvdcss.h.utf && mv dvdcss.h.utf dvdcss.h
popd
iconv -f iso8859-1 -t utf8 AUTHORS > AUTHORS.utf && mv AUTHORS.utf AUTHORS

%build
%configure --disable-dependency-tracking --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/libdvdcss.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_libdir}/libdvdcss.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/html/*
%{_includedir}/dvdcss
%{_libdir}/libdvdcss.so
%{_libdir}/pkgconfig/libdvdcss.pc

%changelog
* Tue Feb 15 2011 Arkady L. Shane <ashejn@yandex-team.ru> 1.2.10-1
- update to 1.2.10

* Sun Jan 13 2008 Dominik Mierzejewski <rpm [AT] greysector [DOT] net> 1.2.9-5
- dropped static library
- updated License tag
- fixed building docs
- updated URL
- fixed rpmlint warnings

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.2.9-4
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.2.9-3
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Mar 13 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info> 1.2.9-2
- Drop Epoch completely

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field
- drop Epoch

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Mon Oct 17 2005 Dams <anvil[AT]livna.org> 0:1.2.9-0.lvn.1
- Updated to 1.2.9

* Mon May 17 2004 Dams <anvil[AT]livna.org> 0:1.2.8-0.lvn.5
- Added URL to Source0

* Mon Oct 13 2003 Dams <anvil[AT]livna.org> 0:1.2.8-0.fdr.4
- Using fedora buildroot

* Mon Oct 13 2003 Dams <anvil[AT]livna.org> 0:1.2.8-0.fdr.3
- Building and including developer doc

* Sun Sep 28 2003 Dams <anvil[AT]livna.org> 0:1.2.8-0.fdr.2
- Removed comment after scriptlets

* Sun Jun 29 2003 Dams <anvil[AT]livna.org> 0:1.2.7-0.fdr.3
- Modified Source0

* Fri Jun 27 2003 Dams <anvil[AT]livna.org> 0:1.2.7-0.fdr.2
- Package now own _includedir/dvdcss

* Mon Jun 23 2003 Dams <anvil[AT]livna.org> 0:1.2.7-0.fdr.1
- Updated to 1.2.7
- buildroot -> RPM_BUILD_ROOT

* Mon Apr  7 2003 Dams <anvil[AT]livna.org> 0:1.2.6-0.fdr.2
- Added post and postun scriptlet
- Switched to .tar.bz source.

* Fri Apr  4 2003 Dams <anvil[AT]livna.org> 
- Initial build.
