Summary:	Test archives using information from .sfv
Summary(pl):	Testowanie archiw�w z u�yciem informacji z plik�w .sfv
Name:		cksfv
Version:	1.3.4
Release:	1
License:	GPL
Vendor:		Bryan Call <bc@fodder.org>
Group:		Applications/Archiving
Source0:	http://www.modeemi.fi/~shd/foss/cksfv/files/%{name}-%{version}.tar.bz2
# Source0-md5:	1330d656fdf70a8744f0e6014b295d3c
URL:		http://www.modeemi.fi/~shd/foss/cksfv/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to test .sfv files. These files are commonly used to ensure
the correct retrieval or storage of data.

%description -l pl
Narz�dzie do testowania plik�w .sfv. Te pliki s� cz�sto u�ywane w celu
upewnienia si� o poprawnym przesyle danych poprzez sie�.

%prep
%setup -q

%build
./configure \
	--prefix=/usr \
	--package-prefix=$RPM_BUILD_ROOT

%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
