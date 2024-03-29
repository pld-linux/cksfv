Summary:	Test archives using information from .sfv
Summary(pl.UTF-8):	Testowanie archiwów z użyciem informacji z plików .sfv
Name:		cksfv
Version:	1.3.14
Release:	1
License:	GPL
Vendor:		Bryan Call <bc@fodder.org>
Group:		Applications/Archiving
Source0:	http://zakalwe.virtuaalipalvelin.net/~shd/foss/cksfv/files/%{name}-%{version}.tar.bz2
# Source0-md5:	138bff42ab23fbba8cca0ae14b2d9e52
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
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE64_SOURCE"

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
