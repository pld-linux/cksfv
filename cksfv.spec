Summary:	Test archives using information from .sfv
Summary(pl):	Testuje archiwa u¿ywaj±c infomacji z .sfv
Name:		cksfv
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Vendor:		Bryan Call <bc@fodder.org>
Source0:	http://www.fodder.org/cksfv/%{name}-%{version}.tar.gz
URL:		http://www.fodder.org/cksfv/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to test .sfv files. These files are commonly used to ensure
the correct retrieval or storage of data.

%description -l pl
Narzêdzie do testowania plików .sfv. Te pliki s± czêsto u¿ywane w celu
upewnienia siê o poprawnym przesyle danych poprzez sieæ.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}" -C src

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/cksfv $RPM_BUILD_ROOT%{_bindir}

gzip -9nf ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz 
%attr(755,root,root) %{_bindir}/*
