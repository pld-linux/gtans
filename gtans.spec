Summary:	Tangram puzzle
Summary(pl):	Uk³adanka - tangramy
Name:		gtans
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
# for 1.1
#Source0:	http://download.sourceforge.net/gtans/%{name}-%{version}.tar.gz
Source0:	%{name}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://altern.org/bwt/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Move the pieces until they match the figure drawn on the right of
window.

%description -l pl
Uk³adaj kawa³ki, dopóki nie u³o¿± siê w figurê pokazan± po prawej
stronie okna.

%prep
%setup -q

%build
cat makefile | sed 's@/usr/local/@%{_prefix}/@' > m.new
cat m.new | sed 's@lib/gtans@share/gtans@' > makefile
cat makefile | sed 's@-O2 -Wall@%{rpmcflags}@' > m.new
cat m.new | sed 's@-lm@& %{rpmldflags}@' > makefile

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/gtans/{figures,pixmaps},%{_pixmapsdir},%{_applnkdir}/Games}

install gtans $RPM_BUILD_ROOT%{_bindir}
install figures/* $RPM_BUILD_ROOT%{_datadir}/gtans/figures
install pixmaps/* $RPM_BUILD_ROOT%{_datadir}/gtans/pixmaps
ln -s /usr/share/doc/%{name}-%{version}/gtanshelp.txt $RPM_BUILD_ROOT%{_datadir}/gtans/gtanshelp.txt

gzip -9nf defaultconfig.gtans.ref

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

# don't gzip gtanshelp.txt!
%files
%defattr(644,root,root,755)
%doc *.gz gtanshelp.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gtans
%{_pixmapsdir}/*
%{_applnkdir}/Games/*
