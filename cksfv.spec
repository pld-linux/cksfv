Summary:	Test archives using information from .sfv
Summary(pl):	Testuje archiwa u¿ywaj±c infomacji z .sfv
Name:		cksfv
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Archiving
Vendor:		Bryan Call <bc@fodder.org>
URL:		http://www.fodder.org/cksfv/
Source0:	http://www.fodder.org/cksfv/%{name}-%{version}.tar.gz
# Source0-md5:	e00cf6a80a566539eb6f3432f2282c38
Patch0:		%{name}-alpha.patch
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
%{__make} CFLAGS="%{rpmcflags}" VERSION=%{version} -C src

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
