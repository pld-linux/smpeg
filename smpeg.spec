Summary:	SDL MPEG Library
Summary(pl.UTF-8):   Biblioteka SDL MPEG
Summary(pt_BR.UTF-8):   Biblioteca MPEG SDL
Summary(ru.UTF-8):   SDL MPEG библиотека и проигрыватель
Summary(uk.UTF-8):   SDL MPEG бібліотека та програвач
Name:		smpeg
Version:	0.4.4
Release:	16
License:	LGPL
Group:		Libraries
# currently developed at http://icculus.org/smpeg/ but no release yet
Source0:	ftp://sunsite.dk/pub/os/linux/loki/open-source/smpeg/%{name}-%{version}.tar.gz
# Source0-md5:	59c76ac704088ef5539210190c4e1fe3
Source1:	gtv.desktop
Source2:	gtv.png
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-gcc.patch
Patch2:		%{name}-optimize.patch
Patch3:		%{name}-am18.patch
Patch4:		%{name}-gcc4.patch
Patch5:		%{name}-gnu-stack.patch
Patch6:		%{name}-fPIC.patch
URL:		http://www.lokigames.com/development/smpeg.php3
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	libsmpeg0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder and
SPLAY, an mpeg audio decoder created by Woo-jae Jung. We have
completed the initial work to wed these two projects in order to
create a general purpose MPEG video/audio player for the Linux OS.

%description -l pl.UTF-8
SMPEG jest bazowanym na mpeg_play z UC Berkeley programowym dekoderem
MPEG. SMPLAY jest dekoderem audio stworzonym przez Woo-jae Jung.
Skompletowaliśmy prace tych dwóch projektów, aby stworzyć MPEG
video/audio player ogólnego przeznaczenia dla systemu Linux.

%description -l pt_BR.UTF-8
A SMPEG é baseada no software de decodificação MPEG mpeg_play da
Universidade de Berkeley e no SPLAY, um decodificador de áudio mpeg
criado por Woo-jae Jung. Completamos o trabalho inicial de casar estes
dois projetos para criar um reprodutor MPEG de vídeo e áudio de
propósito geral para o sistema operacional Linux.

%description -l ru.UTF-8
SMPEG основывается на программном MPEG декодере mpeg_play,
разработанном в UCB (Университете Беркли) и SPLAY, аудио-декодере,
созданном Woo-jae Jung. Эти два проекта были объединены для создания
MPEG-аудио/видео проигрывателя для Linux.

%description -l uk.UTF-8
SMPEG базується на програмному MPEG декодері mpeg_play, розробленому в
UCB (Університеті Берклі) та SPLAY, аудіо-декодері, який створив
Woo-jae Jung. Ці два проекти були об'єднані для створення
MPEG-аудіо/відео програвача для Linux.

%package libs
Summary:	Shared smpeg libraries
Summary(pl.UTF-8):   Współdzielone biblioteki smpeg
Group:		Libraries
Conflicts:	smpeg < 0.4.4-14

%description libs
Shared smpeg libraries.

%description libs -l pl.UTF-8
Współdzielone biblioteki smpeg.

%package devel
Summary:	Smpeg header files and development documentation
Summary(pl.UTF-8):   Pliki nagłówkowe oraz dokumentacja do smpeg
Summary(pt_BR.UTF-8):   Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações SMPEG
Summary(ru.UTF-8):   Файлы, необходимые для разработки программ, использующих SMPEG
Summary(uk.UTF-8):   Файли, необхідні для розробки програм, що використовують SMPEG
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	SDL-devel
Obsoletes:	libsmpeg0.4-devel

%description devel
Header files and development documentation for smpeg.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz dokumentacja do biblioteki smpeg.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações
SMPEG.

%description devel -l uk.UTF-8
Цей пакет містить файли, необхідні для розробки програм, що
використовують SMPEG.

%description devel -l ru.UTF-8
Этот пакет содержит файлы, необходимые для разработки программ,
использующих SMPEG.

%package static
Summary:	Smpeg static libraries
Summary(pl.UTF-8):   Biblioteki statyczne smpeg
Summary(pt_BR.UTF-8):   Bibliotecas estáticas para desenvolvimento de aplicações SMPEG
Summary(ru.UTF-8):   Статические библиотеки для разработки с использованием SMPEG
Summary(uk.UTF-8):   Статичні бібліотеки для розробки з використанням SMPEG
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Smpeg static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne smpeg.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento de aplicações SMPEG.


%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки для разработки программ,
использующих SMPEG.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки для розробки програм, що
використовують SMPEG.

%package gtv
Summary:	gtv MPEG player
Summary(pl.UTF-8):   Odtwarzacz MPEG gtv
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description gtv
gtv MPEG player.

%description gtv -l pl.UTF-8
Odtwarzacz MPEG gtv.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0

# get only AC_TYPE_SOCKLEN_T, kill the rest (libtool.m4 in particular)
tail -n 23 acinclude.m4 > acinc.tmp
mv -f acinc.tmp acinclude.m4

%build
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

%{__make} \
	CC="%{__cxx}" \
	CCASFLAGS="\$(CFLAGS)"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/plaympeg
%{_mandir}/man1/plaympeg.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

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
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/gtv.1*
