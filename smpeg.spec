Summary:	SDL MPEG Library
Name:		smpeg
Version:	0.3.1
Release:	1
Copyright:	LGPL
Group:		Libraries
Source:		http://www.lokigames.com/development/download/smpeg/%{name}-%{version}.tar.gz
BuildRequires:	SDL-devel >= 0.11.2
URL:		http://www.lokigames.com/development/smpeg.php3
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix	/usr/X11R6
%define		_mandir	%{_prefix}/man

%description
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder
and SPLAY, an mpeg audio decoder created by Woo-jae Jung. We have
completed the initial work to wed these two projects in order to 
create a general purpose MPEG video/audio player for the Linux OS. 

%package devel
Summary:	Smpeg header files and development documentation
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja do smpeg
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for smpeg.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja do biblioteki smpeg.

%package static
Summary:	Smpeg static libraries
Summary(pl):	Biblioteki statyczne smpeg
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Smpeg static libraries.

%description devel -l pl
Biblioteki statyczne smpeg.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/*/* CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {CHANGES,COPYING,README}.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*

%files devel
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a
