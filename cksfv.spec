Summary:	Test archives using information from .sfv
Summary(pl.UTF-8):   Testowanie archiwów z użyciem informacji z plików .sfv
Name:		cksfv
Version:	1.3.9
Release:	1
License:	GPL
Vendor:		Bryan Call <bc@fodder.org>
Group:		Applications/Archiving
Source0:	http://zakalwe.virtuaalipalvelin.net/~shd/foss/cksfv/files/%{name}-%{version}.tar.bz2
# Source0-md5:	33c1ab4f1ea7e9a194e12b2aedb4741b
URL:		http://zakalwe.virtuaalipalvelin.net/~shd/foss/cksfv/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to test .sfv files. These files are commonly used to ensure
the correct retrieval or storage of data.

%description -l pl.UTF-8
Narzędzie do testowania plików .sfv. Te pliki są często używane w celu
upewnienia się o poprawnym przesyle danych poprzez sieć.

%prep
%setup -q

%build
./configure \
	--prefix=/usr \
	--package-prefix=$RPM_BUILD_ROOT

%{__make} all check \
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
