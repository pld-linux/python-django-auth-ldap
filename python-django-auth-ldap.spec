#
# Conditional build:
%bcond_with	doc	# Sphinx documentation (TODO)
%bcond_with	tests	# unit tests (TODO)
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%define 	module		django_auth_ldap
%define 	egg_name	django_auth_ldap
%define		pypi_name	django-auth-ldap
Summary:	Django LDAP authentication backend
Summary(pl.UTF-8):	Backend uwierzytelniający LDAP dla Django
Name:		python-%{pypi_name}
Version:	1.2.8
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/django-auth-ldap/
Source0:	https://files.pythonhosted.org/packages/source/d/django-auth-ldap/%{pypi_name}-%{version}.tar.gz
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
BuildRequires:	python-setuptools >= 1:0.6-0.c11
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-mockldap >= 0.2.7
BuildRequires:	python3-setuptools >= 1:0.6-0.c11
%endif
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
