Summary:	SDL MPEG Library
Summary(pl):	Biblioteka SDL MPEG
Summary(pt_BR):	Biblioteca MPEG SDL
Summary(ru):	SDL MPEG библиотека и проигрыватель
Summary(uk):	SDL MPEG б╕бл╕отека та програвач
Name:		smpeg
Version:	0.4.4
Release:	12
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.lokigames.com/pub/open-source/smpeg/%{name}-%{version}.tar.gz
# Source0-md5: 59c76ac704088ef5539210190c4e1fe3
Source1:	gtv.desktop
Source2:	gtv.png
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-gcc.patch
Patch2:		%{name}-optimize.patch
URL:		http://www.lokigames.com/development/smpeg.php3
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libsmpeg0.4

%description
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder and
SPLAY, an mpeg audio decoder created by Woo-jae Jung. We have
completed the initial work to wed these two projects in order to
create a general purpose MPEG video/audio player for the Linux OS.

%description -l pl
SMPEG jest bazowanym na mpeg_play z UC Berkeley programowym dekoderem
MPEG. SMPLAY jest dekoderem audio stworzonym przez Woo-jae Jung.
Skompletowali╤my prace tych dwСch projektСw, aby stworzyФ MPEG
video/audio player ogСlnego przeznaczenia dla systemu Linux.

%description -l pt_BR
A SMPEG И baseada no software de decodificaГЦo MPEG mpeg_play da
Universidade de Berkeley e no SPLAY, um decodificador de Аudio mpeg
criado por Woo-jae Jung. Completamos o trabalho inicial de casar estes
dois projetos para criar um reprodutor MPEG de vМdeo e Аudio de
propСsito geral para o sistema operacional Linux.

%description -l ru
SMPEG основывается на программном MPEG декодере mpeg_play,
разработанном в UCB (Университете Беркли) и SPLAY, аудио-декодере,
созданном Woo-jae Jung. Эти два проекта были объединены для создания
MPEG-аудио/видео проигрывателя для Linux.

%description -l uk
SMPEG базу╓ться на програмному MPEG декодер╕ mpeg_play, розробленому в
UCB (Ун╕верситет╕ Беркл╕) та SPLAY, ауд╕о-декодер╕, який створив
Woo-jae Jung. Ц╕ два проекти були об'╓днан╕ для створення
MPEG-ауд╕о/в╕део програвача для Linux.

%package devel
Summary:	Smpeg header files and development documentation
Summary(pl):	Pliki nagЁСwkowe oraz dokumentacja do smpeg
Summary(pt_BR):	Bibliotecas e arquivos de inclusЦo para desenvolvimento de aplicaГУes SMPEG
Summary(ru):	Файлы, необходимые для разработки программ, использующих SMPEG
Summary(uk):	Файли, необх╕дн╕ для розробки програм, що використовують SMPEG
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	SDL-devel
Obsoletes:	libsmpeg0.4-devel

%description devel
Header files and development documentation for smpeg.

%description devel -l pl
Pliki nagЁСwkowe oraz dokumentacja do biblioteki smpeg.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusЦo para desenvolvimento de aplicaГУes
SMPEG.

%description devel -l uk
Цей пакет м╕стить файли, необх╕дн╕ для розробки програм, що
використовують SMPEG.

%description devel -l ru
Этот пакет содержит файлы, необходимые для разработки программ,
использующих SMPEG.

%package static
Summary:	Smpeg static libraries
Summary(pl):	Biblioteki statyczne smpeg
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento de aplicaГУes SMPEG
Summary(ru):	Статические библиотеки для разработки с использованием SMPEG
Summary(uk):	Статичн╕ б╕бл╕отеки для розробки з використанням SMPEG
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Smpeg static libraries.

%description static -l pl
Biblioteki statyczne smpeg.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento de aplicaГУes SMPEG.


%description static -l ru
Этот пакет содержит статические библиотеки для разработки программ,
использующих SMPEG.

%description static -l uk
Цей пакет м╕стить статичн╕ б╕бл╕отеки для розробки програм, що
використовують SMPEG.

%package gtv
Summary:	gtv MPEG player
Summary(pl):	Odtwarzacz MPEG gtv
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description gtv
gtv MPEG player.

%description gtv -l pl
Odtwarzacz MPEG gtv.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
# remove libtool.m4 from acinclude.m4
head -168 acinclude.m4 > acinc.tmp
tail -23 acinclude.m4 >> acinc.tmp
mv -f acinc.tmp acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure \
%ifarch %{ix86}
	--enable-mmx \
%endif
	--disable-debug \
	--disable-opengl-player

%{__make} CC=%{__cxx}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Multimedia,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/plaympeg
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/plaympeg.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/smpeg-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files gtv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtv
%{_applnkdir}/Multimedia/*
%{_pixmapsdir}/*
%{_mandir}/man1/gtv.1*
