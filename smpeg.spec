Summary:	SDL MPEG Library
Name:		smpeg
Version:	0.4.0
Release:	1
License:	LGPL
Group:		Libraries
Group(fr):	Development/Librairies
Source0:	ftp://ftp.lokigames.com/pub/open-source/smpeg/%{name}-%{version}.tar.gz
Source1:	gtv.desktop
Source2:	gtv.png
BuildRequires:	SDL-devel >= 1.1.3
BuildRequires:	gtk+-devel >= 1.2.1
BuildRequires:	libstdc++-devel
BuildRequires:	esound-devel
URL:		http://www.lokigames.com/development/smpeg.php3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6
%define		_mandir	%{_prefix}/man

%description
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder and SPLAY,
an mpeg audio decoder created by Woo-jae Jung. We have completed the
initial work to wed these two projects in order to  create a general
purpose MPEG video/audio player for the Linux OS.

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
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
LDFLAGS="-s"
export CXXFLAGS LDLAGS
%configure \
	--disable-opengl-player
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_applnkdir}/Multimedia,%{_datadir}/pixmaps}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/*/* CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {CHANGES,README}.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_applnkdir}/Multimedia/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
