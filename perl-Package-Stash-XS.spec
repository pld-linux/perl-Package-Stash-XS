#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Package
%define		pnam	Stash-XS
%include	/usr/lib/rpm/macros.perl
Summary:	Package::Stash::XS - faster and more correct implementation of the Package::Stash API
Summary(pl.UTF-8):	Package::Stash::XS - szybsza i bardziej poprawna implementacja API Package::Stash
Name:		perl-Package-Stash-XS
Version:	0.28
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Package/Package-Stash-XS-%{version}.tar.gz
# Source0-md5:	9664356ec3be02626cbd3081ec246b70
URL:		http://search.cpan.org/dist/Package-Stash-XS/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.31
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a backend for Package::Stash, which provides the functionality
in a way that's less buggy and much faster. It will be used by default
if it's installed, and should be preferred in all environments with a
compiler.

%description -l pl.UTF-8
Ten moduł jest backendem dla modułu Package::Stash, udostępniającym
jego funkcjonalność w mniej błędny i szybszy sposób. Jest używany jako
domyślny backend jeśli jest zainstalowany i powinien być preferowany
we wszystkich środowiskach z kompilatorem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/Package
%dir %{perl_vendorarch}/Package/Stash
%{perl_vendorarch}/Package/Stash/XS.pm
%dir %{perl_vendorarch}/auto/Package
%dir %{perl_vendorarch}/auto/Package/Stash
%dir %{perl_vendorarch}/auto/Package/Stash/XS
%attr(755,root,root) %{perl_vendorarch}/auto/Package/Stash/XS/XS.so
%{_mandir}/man3/Package::Stash::XS.3pm*
