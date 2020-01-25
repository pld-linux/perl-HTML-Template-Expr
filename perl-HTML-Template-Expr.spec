#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	HTML
%define		pnam	Template-Expr
Summary:	HTML::Template::Expr - HTML::Template extension adding expression support
Summary(pl.UTF-8):	HTML::Template::Expr - rozszerzenie HTML::Template dodające obsługę wyrażeń
Name:		perl-HTML-Template-Expr
Version:	0.07
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	717ea56c2244b6e2d26a0e477a4d069c
URL:		http://search.cpan.org/dist/HTML-Template-Expr/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Template >= 2.4
BuildRequires:	perl-Parse-RecDescent
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an extension to HTML::Template which allows
expressions in the template syntax. This is purely an addition - all
the normal HTML::Template options, syntax and behaviors will still
work. See HTML::Template for details.

%description -l pl.UTF-8
Ten moduł dostarcza rozszerzenie do HTML::Template, pozwalające na
używanie wyrażeń w składni szablonów. Jest to czysty dodatek -
wszystkie normalne opcje HTML::Template, składnia i zachowanie nadal
działa. Więcej szczegółów w HTML::Template.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/HTML/Template/*.pm
%{_mandir}/man3/*
