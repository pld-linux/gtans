Summary:	Tangram puzzle
Summary(pl):	Uk�adanka - tangramy
Name:		gtans
Version:	1.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/gtans/%{name}-%{version}.tar.gz
# Source0-md5:	067d8bd1d5534b39316bdb4e689a6c40
Source1:	%{name}.desktop
URL:		http://gtans.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%{_prefix}/share/gtans

%description
The Tangram is a chinese puzzle. The object is to put seven geometric
shapes together so as to form a given outline. All the pieces must be
used and are laid next to one another. The pieces are five triangles,
a square and a parallelogram.

%description -l pl
Tangramy to chi�ska uk�adanka. Celem gry jest u�o�enie siedmiu figur
geometrycznych tak, by uzyska� zadany kszta�t. Wszystkie kawa�ki musz�
zosta� u�yte oraz u�o�one obok siebie. Dost�pne figury to pi��
tr�jk�t�w, kwadrat i r�wnoleg�obok.

%prep
%setup -q

%build
sed -e 's@-O2 -Wall@%{rpmcflags}@;s@gcc@%{__cc}@;s@-lm@& %{rpmldflags}@' \
	makefile > m.new
mv -f m.new makefile

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_mandir}/man6}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT/usr/man/man6/* $RPM_BUILD_ROOT%{_mandir}/man6

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install misc/gtans_icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/gtans.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS HISTORY
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%dir %{_datadir}
%{_datadir}/figures
%{_datadir}/pixmaps
%{_datadir}/gtansrc
%{_datadir}/gtanshelp.txt
%lang(es) %{_datadir}/gtanshelpes.txt
%lang(fr) %{_datadir}/gtanshelpfr.txt
%lang(pl) %{_datadir}/gtanshelppl.txt
%lang(ru) %{_datadir}/gtanshelpru.txt
%lang(uk) %{_datadir}/gtanshelpuk.txt
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/*.desktop
