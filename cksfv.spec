Summary:	Test archives using information from .sfv
Summary(pl):	Testowanie archiwów z u¿yciem informacji z plików .sfv
Name:		cksfv
Version:	1.3
Release:	3
License:	GPL
Vendor:		Bryan Call <bc@fodder.org>
Group:		Applications/Archiving
Source0:	http://www.fodder.org/cksfv/%{name}-%{version}.tar.gz
# Source0-md5:	e00cf6a80a566539eb6f3432f2282c38
Patch0:		%{name}-LFS.patch
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
%patch0 -p1

%build
%{__make} -C src \
	CFLAGS="%{rpmcflags} -D_LARGEFILE64_SOURCE" \
	VERSION=%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/cksfv $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
