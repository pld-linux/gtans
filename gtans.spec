Summary:	Tangram puzzle
Summary(pl):	Uk³adanka - tangramy
Name:		gtans
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.sourceforge.net/gtans/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	http://gtans.sourceforge.net/alpha.figures.gz
Source3:	http://gtans.sourceforge.net/%{name}-ru.tar.gz
Source4:	http://gtans.sourceforge.net/%{name}-uk.tar.gz
Source5:	%{name}-pl.tar.gz
URL:		http://altern.org/bwt/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_datadir	%{_prefix}/share/gtans

%description
The Tangram is a chinese puzzle. The object is to put seven geometric
shapes together so as to form a given outline. All the pieces must be
used and are laid next to one another. The pieces are five triangles,
a square and a parallelogram.

%description -l pl
Tangramy to chiñska uk³adanka. Celem gry jest u³o¿enie siedmiu figur
geometrycznych tak, by uzyskaæ zadany kszta³t. Wszystkie kawa³ki musz±
zostaæ u¿yte oraz u³o¿one obok siebie. Dostêpne figury to piêæ
trójk±tów, kwadrat i równoleg³obok.

%prep
%setup -q -a3 -a4 -a5

%build
cat makefile | sed 's@/usr@%{_prefix}/@' > m.new
cat m.new | sed 's@-O2 -Wall@%{rpmcflags}@' > makefile
cat makefile | sed 's@gcc@%{__cc}@' > m.new
cat m.new | sed 's@-lm@& %{rpmldflags}@' > makefile

cp gtans-ru/gtanshelpru.txt .
cp gtans-uk/gtanshelpuk.txt .
cp gtans-pl/gtanshelppl.txt .
cp gtans-ru/ru.po po/gtans.po-ru
cp gtans-uk/uk.po po/gtans.po-uk
cp gtans-pl/pl.po po/gtans.po-pl

cd po
cat Makefile | sed 's@es fr@& ru uk pl@' > m.new
mv -f m.new Makefile

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games

cat makefile | sed 's@/%{_prefix}@%$(DESTDIR)%{_prefix}/@' > m.new
mv -f m.new makefile
%{__make} install DESTDIR=$RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT/usr/share
mv -f $RPM_BUILD_ROOT%{_prefix}/share/locale $RPM_BUILD_ROOT/usr/share/

install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/figures
gunzip $RPM_BUILD_ROOT%{_datadir}/figures/*.gz

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install misc/gtans_icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/gtans.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%dir %{_datadir}
%{_datadir}/figures
%{_datadir}/pixmaps
%{_datadir}/gtansrc
%{_datadir}/gtanshelp.txt
%lang(es) %{_datadir}/gtanshelpes.txt
%lang(fr) %{_datadir}/gtanshelpfr.txt
%lang(ru) %{_datadir}/gtanshelpru.txt
%lang(uk) %{_datadir}/gtanshelpuk.txt
%lang(pl) %{_datadir}/gtanshelppl.txt
%{_pixmapsdir}/%{name}.png
%{_applnkdir}/Games/*
