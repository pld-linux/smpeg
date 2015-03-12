Summary:	SDL MPEG Library
Summary(pl.UTF-8):	Biblioteka SDL MPEG
Summary(pt_BR.UTF-8):	Biblioteca MPEG SDL
Summary(ru.UTF-8):	SDL MPEG библиотека и проигрыватель
Summary(uk.UTF-8):	SDL MPEG бібліотека та програвач
Name:		smpeg
Version:	0.4.5
Release:	3
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_mixer/libs/old/%{name}-%{version}.zip
# Source0-md5:	ab48e149eed296072efd8865e53ec374
Source1:	gtv.desktop
Source2:	gtv.png
Patch0:		%{name}-acfix.patch
Patch1:		%{name}-optimize.patch
Patch2:		format-security.patch
URL:		http://icculus.org/smpeg/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	libsmpeg0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder and
SPLAY, an mpeg audio decoder created by Woo-jae Jung. We have
completed the initial work to wed these two projects in order to
create a general purpose MPEG video/audio player for the Linux OS.

%description -l pl.UTF-8
SMPEG jest opartym na mpeg_play z UC Berkeley programowym dekoderem
MPEG. SMPLAY jest dekoderem audio stworzonym przez Woo-jae Jung.
Skompletowano prace tych dwóch projektów, aby stworzyć odtwarzacz MPEG
video/audio ogólnego przeznaczenia dla systemu Linux.

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
Summary:	Shared smpeg library
Summary(pl.UTF-8):	Współdzielona biblioteka smpeg
Group:		Libraries
Conflicts:	smpeg < 0.4.4-14

%description libs
Shared smpeg library.

%description libs -l pl.UTF-8
Współdzielona biblioteka smpeg.

%package devel
Summary:	Smpeg header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki smpeg
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações SMPEG
Summary(ru.UTF-8):	Файлы, необходимые для разработки программ, использующих SMPEG
Summary(uk.UTF-8):	Файли, необхідні для розробки програм, що використовують SMPEG
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	SDL-devel
Obsoletes:	libsmpeg0.4-devel

%description devel
Header files for smpeg library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki smpeg.

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
Summary:	Smpeg static library
Summary(pl.UTF-8):	Biblioteka statyczna smpeg
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento de aplicações SMPEG
Summary(ru.UTF-8):	Статические библиотеки для разработки с использованием SMPEG
Summary(uk.UTF-8):	Статичні бібліотеки для розробки з використанням SMPEG
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Smpeg static library.

%description static -l pl.UTF-8
Biblioteka statyczna smpeg.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento de aplicações SMPEG.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки для разработки программ,
использующих SMPEG.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки для розробки програм, що
використовують SMPEG.

%package glmovie
Summary:	glmovie - OpenGL based MPEG player
Summary(pl.UTF-8):	glmovie - odtwarzacz MPEG oparty na OpenGL-u
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description glmovie
glmovie - OpenGL based MPEG player.

%description glmovie -l pl.UTF-8
glmovie - odtwarzacz MPEG oparty na OpenGL-u.

%package gtv
Summary:	gtv - GTK+ based MPEG player
Summary(pl.UTF-8):	gtv - odtwarzacz MPEG oparty na GTK+
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description gtv
gtv - GTK+ based MPEG player.

%description gtv -l pl.UTF-8
gtv - odtwarzacz MPEG oparty na GTK+.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%{__rm} acinclude/{libtool,lt*}.m4

%build
%{__libtoolize}
%{__aclocal} -I acinclude
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcxxflags} -fno-rtti -fno-exceptions"
%configure \
%ifarch %{ix86}
	--enable-mmx \
%endif
	--disable-debug

%{__make}

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
%doc CHANGES README README.SDL_mixer TODO
%attr(755,root,root) %{_bindir}/plaympeg
%{_mandir}/man1/plaympeg.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmpeg-0.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmpeg-0.4.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/smpeg-config
%attr(755,root,root) %{_libdir}/libsmpeg.so
%{_libdir}/libsmpeg.la
%{_includedir}/smpeg
%{_aclocaldir}/smpeg.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libsmpeg.a

%files glmovie
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glmovie

%files gtv
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtv
%{_desktopdir}/gtv.desktop
%{_pixmapsdir}/gtv.png
%{_mandir}/man1/gtv.1*
