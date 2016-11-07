#
# Conditional build:
%bcond_with	doc	# don't build doc
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%define 	module		django_auth_ldap
%define 	egg_name	django_auth_ldap
%define		pypi_name	django-auth-ldap
Summary:	Django LDAP authentication backend
Name:		python-%{pypi_name}
Version:	1.2.8
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	88db539ca8492c91a8adaca68d70129b
URL:		http://bitbucket.org/psagers/django-auth-ldap/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	sphinx-pdg
%endif
%if %{with tests}
BuildRequires:	python-mockldap >= 0.2.7
BuildRequires:	python-setuptools >= 0.6c11
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-mockldap >= 0.2.7
BuildRequires:	python3-setuptools >= 0.6c11
%endif
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Django authentication backend that authenticates against an
LDAP service.

%package -n python3-%{pypi_name}
Summary:	Django LDAP authentication backend
Group:		Libraries/Python

%description -n python3-%{pypi_name}
This is a Django authentication backend that authenticates against an
LDAP service.

%prep
%setup -q -n %{pypi_name}-%{version}

%{__rm} -r %{egg_name}.egg-info

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
sphinx-build-2 docs/source html
%{__rm} -r html/.{doctrees,buildinfo}
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
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
