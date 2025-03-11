#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (require slapd and some configuration)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module		django_auth_ldap
%define 	egg_name	django_auth_ldap
%define		pypi_name	django-auth-ldap
Summary:	Django LDAP authentication backend
Summary(pl.UTF-8):	Backend uwierzytelniający LDAP dla Django
Name:		python-%{pypi_name}
# keep 1.x here for python2 support
Version:	1.7.0
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/django-auth-ldap/
Source0:	https://files.pythonhosted.org/packages/source/d/django-auth-ldap/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	bb85e5e50ea179781244df580ee5b0f0
Patch0:		django-auth-ldap-mock.patch
URL:		http://bitbucket.org/psagers/django-auth-ldap/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 1:0.6-0.c11
%endif
%if %{with tests}
BuildRequires:	openldap-servers
BuildRequires:	python-django >= 1.11
BuildRequires:	python-ldap >= 3.1
BuildRequires:	python-mock >= 2.0.0
BuildRequires:	python-slapdtest
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools >= 1:0.6-0.c11
%if %{with tests}
BuildRequires:	openldap-servers
BuildRequires:	python3-django >= 1.11
BuildRequires:	python3-ldap >= 3.1
BuildRequires:	python3-slapdtest
%endif
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg-2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Django authentication backend that authenticates against an
LDAP service.

%description -l pl.UTF-8
Ten pakiet to backend uwierzytelniający Django uwierzytelniający
względem usługi LDAP.

%package -n python3-%{pypi_name}
Summary:	Django LDAP authentication backend
Summary(pl.UTF-8):	Backend uwierzytelniający LDAP dla Django
Group:		Libraries/Python

%description -n python3-%{pypi_name}
This is a Django authentication backend that authenticates against an
LDAP service.

%description -n python3-%{pypi_name} -l pl.UTF-8
Ten pakiet to backend uwierzytelniający Django uwierzytelniający
względem usługi LDAP.

%package apidocs
Summary:	API documentation for django-auth-ldap module
Summary(pl.UTF-8):	Dokumentacja API modułu django-auth-ldap
Group:		Documentation

%description apidocs
API documentation for django-auth-ldap module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu django-auth-ldap.

%prep
%setup -q -n %{pypi_name}-%{version}
%patch -P 0 -p1

%{__rm} -r %{egg_name}.egg-info

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
sphinx-build-2 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
