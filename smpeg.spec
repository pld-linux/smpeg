# $Revison:$
Summary:	SDL MPEG Library
Name:		smpeg
Version:	0.3.1
Release:	1
Copyright:	LGPL
Group:		Libraries
Source0:	smpeg-%{version}.tar.gz
URL:		http://www.lokigames.com/development/smpeg.php3
Requires:	SDL
BuildRoot:	/tmp/%{name}-root
BuildRequires:	SDL-devel

%define		_prefix	/usr/X11R6
%define		_mandir	%{_prefix}/man

%description
SMPEG is based on UC Berkeley's mpeg_play software MPEG decoder
and SPLAY, an mpeg audio decoder created by Woo-jae Jung. We have
completed the initial work to wed these two projects in order to 
create a general purpose MPEG video/audio player for the Linux OS. 

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS"
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

make install prefix=$RPM_BUILD_ROOT%{_prefix}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/*/* CHANGES README COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {CHANGES,COPYING,README}.gz
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root)%{_includedir}/*
%attr(755,root,root)%{_libdir}/*
%attr(644,root,root)%{_mandir}/*
