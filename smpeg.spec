Summary:	SDL MPEG Library
Summary(pl):	Biblioteka SDL MPEG
Name:		smpeg
Version:	0.4.4
Release:	4
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.lokigames.com/pub/open-source/smpeg/%{name}-%{version}.tar.gz
Source1:	gtv.desktop
Source2:	gtv.png
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	gtk+-devel >= 1.2.1
BuildRequires:	libstdc++-devel
BuildRequires:	esound-devel
URL:		http://www.lokigames.com/development/smpeg.php3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6
%define		_mandir	%{_prefix}/man

%description
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder and
SPLAY, an mpeg audio decoder created by Woo-jae Jung. We have
completed the initial work to wed these two projects in order to
create a general purpose MPEG video/audio player for the Linux OS.

%description -l pl
SMPEG jest bazowanym na mpeg_play z UC Berkeley programowym dekoderem
MPEG. SMPLAY jest dekoderem audio stworzonym przez Woo-jae Jung.
Skompletowali�my prace tych dw�ch projekt�w, aby stworzy� MPEG
video/audio player og�lnego przeznaczenia dla systemu Linux.

%package devel
Summary:	Smpeg header files and development documentation
Summary(pl):	Pliki nag��wkowe oraz dokumentacja do smpeg
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	SDL-devel

%description devel
Header files and development documentation for smpeg.

%description devel -l pl
Pliki nag��wkowe oraz dokumentacja do biblioteki smpeg.

%package static
Summary:	Smpeg static libraries
Summary(pl):	Biblioteki statyczne smpeg
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Smpeg static libraries.

%description devel -l pl
Biblioteki statyczne smpeg.

%prep
%setup -q

%build
aclocal
autoconf
automake -a -c
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure \
	--disable-debug \
	--disable-opengl-player
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Multimedia,%{_datadir}/pixmaps}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

gzip -9nf CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {CHANGES,README}.gz
%attr(755,root,root) %{_bindir}/gtv
%attr(755,root,root) %{_bindir}/plaympeg
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_applnkdir}/Multimedia/*
%{_pixmapsdir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/smpeg-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
