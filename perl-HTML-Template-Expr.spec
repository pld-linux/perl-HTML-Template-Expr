#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Template-Expr
Summary:	HTML::Template::Expr - HTML::Template extension adding expression support
Summary(pl):	HTML::Template::Expr - rozszerzenie HTML::Template dodaj±ce obs³ugê wyra¿eñ
Name:		perl-HTML-Template-Expr
Version:	0.04
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-HTML-Template >= 2.4
BuildRequires:	perl-Parse-RecDescent
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an extension to HTML::Template which allows
expressions in the template syntax.  This is purely an addition - all
the normal HTML::Template options, syntax and behaviors will still
work. See HTML::Template for details.

%description -l pl
Ten modu³ dostarcza rozszerzenie do HTML::Template, pozwalaj±ce na
u¿ywanie wyra¿eñ w sk³adni szablonów. Jest to czysty dodatek -
wszystkie normalne opcje HTML::Template, sk³adnia i zachowanie nadal
dzia³a. Wiêcej szczegó³ów w HTML::Template.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/HTML/Template/*.pm
%{_mandir}/man3/*
