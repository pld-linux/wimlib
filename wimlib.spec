# Conditional build:
%bcond_without	ntfs_3g		# build without ntfs-3g (avoid GPLv2 dependency)

Summary:	Open source Windows Imaging (WIM) library
Name:		wimlib
Version:	1.13.4
Release:	2
License:	GPL v3+ or LGPL v3+
Group:		Libraries
Source0:	https://wimlib.net/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	3e73d06fd78d6541ba98478ac9cc295e
URL:		https://wimlib.net/
BuildRequires:	libfuse-devel
BuildRequires:	libxml2-devel
%{?with_ntfs_3g:BuildRequires:	ntfs-3g-devel >= 1:2011.4.12}
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
Requires:	libfuse-tools
%{?with_ntfs_3g:Requires:	ntfs-3g-libs >= 1:2011.4.12}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wimlib is an open source, cross-platform library for creating,
extracting, and modifying Windows Imaging (WIM) archives. WIM is a
file archiving format, somewhat comparable to ZIP (and many other file
archiving formats); but unlike ZIP, it allows storing various
Windows-specific metadata, allows storing multiple "images" in a
single archive, automatically deduplicates all file contents, and
supports optional solid compression to get a better compression ratio.
wimlib and its command-line frontend wimlib-imagex provide a free and
cross-platform alternative to Microsoft's WIMGAPI, ImageX, and DISM.

%package devel
Summary:	Development files for wimlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for wimlib.

%package static
Summary:	Static wimlib library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static wimlib library.

%package tools
Summary:	Tools for creating, modifying, extracting, and mounting WIM files
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Suggests:	mkisofs

%description tools
Tools for creating, modifying, extracting, and mounting WIM files.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env bash,%{__bash},' programs/mkwinpeimg.in

%build
%configure \
	--disable-silent-rules \
	%{!?with_ntfs_3g:--without-ntfs-3g}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libwim.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README
%attr(755,root,root) %{_libdir}/libwim.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwim.so.15

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwim.so
%{_includedir}/wimlib.h
%{_pkgconfigdir}/wimlib.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libwim.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mkwinpeimg
%attr(755,root,root) %{_bindir}/wimappend
%attr(755,root,root) %{_bindir}/wimapply
%attr(755,root,root) %{_bindir}/wimcapture
%attr(755,root,root) %{_bindir}/wimdelete
%attr(755,root,root) %{_bindir}/wimdir
%attr(755,root,root) %{_bindir}/wimexport
%attr(755,root,root) %{_bindir}/wimextract
%attr(755,root,root) %{_bindir}/wiminfo
%attr(755,root,root) %{_bindir}/wimjoin
%attr(755,root,root) %{_bindir}/wimlib-imagex
%attr(755,root,root) %{_bindir}/wimmount
%attr(755,root,root) %{_bindir}/wimmountrw
%attr(755,root,root) %{_bindir}/wimoptimize
%attr(755,root,root) %{_bindir}/wimsplit
%attr(755,root,root) %{_bindir}/wimunmount
%attr(755,root,root) %{_bindir}/wimupdate
%attr(755,root,root) %{_bindir}/wimverify
%{_mandir}/man1/mkwinpeimg.1*
%{_mandir}/man1/wimappend.1*
%{_mandir}/man1/wimapply.1*
%{_mandir}/man1/wimcapture.1*
%{_mandir}/man1/wimdelete.1*
%{_mandir}/man1/wimdir.1*
%{_mandir}/man1/wimexport.1*
%{_mandir}/man1/wimextract.1*
%{_mandir}/man1/wiminfo.1*
%{_mandir}/man1/wimjoin.1*
%{_mandir}/man1/wimlib-imagex-append.1*
%{_mandir}/man1/wimlib-imagex-apply.1*
%{_mandir}/man1/wimlib-imagex-capture.1*
%{_mandir}/man1/wimlib-imagex-delete.1*
%{_mandir}/man1/wimlib-imagex-dir.1*
%{_mandir}/man1/wimlib-imagex-export.1*
%{_mandir}/man1/wimlib-imagex-extract.1*
%{_mandir}/man1/wimlib-imagex-info.1*
%{_mandir}/man1/wimlib-imagex-join.1*
%{_mandir}/man1/wimlib-imagex-mount.1*
%{_mandir}/man1/wimlib-imagex-mountrw.1*
%{_mandir}/man1/wimlib-imagex-optimize.1*
%{_mandir}/man1/wimlib-imagex-split.1*
%{_mandir}/man1/wimlib-imagex-unmount.1*
%{_mandir}/man1/wimlib-imagex-update.1*
%{_mandir}/man1/wimlib-imagex-verify.1*
%{_mandir}/man1/wimlib-imagex.1*
%{_mandir}/man1/wimmount.1*
%{_mandir}/man1/wimmountrw.1*
%{_mandir}/man1/wimoptimize.1*
%{_mandir}/man1/wimsplit.1*
%{_mandir}/man1/wimunmount.1*
%{_mandir}/man1/wimupdate.1*
%{_mandir}/man1/wimverify.1*
