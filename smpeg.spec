Summary:	SDL MPEG Library
Summary(pl):	Biblioteka SDL MPEG
Summary(pt_BR):	Biblioteca MPEG SDL
Name:		smpeg
Version:	0.4.4
Release:	7
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.lokigames.com/pub/open-source/smpeg/%{name}-%{version}.tar.gz
Source1:	gtv.desktop
Source2:	gtv.png
Patch0:		%{name}-acfix.patch
URL:		http://www.lokigames.com/development/smpeg.php3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	gtk+-devel >= 1.2.1
BuildRequires:	libstdc++-devel
BuildRequires:	esound-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libsmpeg0.4

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
Skompletowali¶my prace tych dwóch projektów, aby stworzyæ MPEG
video/audio player ogólnego przeznaczenia dla systemu Linux.

%description -l pt_BR
A SMPEG é baseada no software de decodificação MPEG mpeg_play da
Universidade de Berkeley e no SPLAY, um decodificador de áudio mpeg
criado por Woo-jae Jung. Completamos o trabalho inicial de casar estes
dois projetos para criar um reprodutor MPEG de vídeo e áudio de
propósito geral para o sistema operacional Linux.

%package devel
Summary:	Smpeg header files and development documentation
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja do smpeg
Summary(pt_BR):	Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações SMPEG
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	SDL-devel
Obsoletes:	libsmpeg0.4-devel

%description devel
Header files and development documentation for smpeg.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja do biblioteki smpeg.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações
SMPEG.

%package static
Summary:	Smpeg static libraries
Summary(pl):	Biblioteki statyczne smpeg
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento de aplicações SMPEG
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Smpeg static libraries.

%description static -l pl
Biblioteki statyczne smpeg.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento de aplicações SMPEG.

%prep
%setup -q
%patch -p1

%build
rm -f missing
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

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
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
