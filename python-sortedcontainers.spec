#
# Conditional build:
%bcond_with	tests	# tests (tox based)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sorted Containers - Sorted List, Sorted Dict, Sorted Set
Summary(pl.UTF-8):	Posortowane kontenery - lista, słownik, zbiór
Name:		python-sortedcontainers
Version:	2.4.0
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sortedcontainers/
Source0:	https://files.pythonhosted.org/packages/source/s/sortedcontainers/sortedcontainers-%{version}.tar.gz
# Source0-md5:	50eeb6cb739568b590b28f9a3f445c78
URL:		https://pypi.org/project/sortedcontainers/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-tox
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-tox
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sorted Containers is an Apache2 licensed sorted collections library,
written in pure-Python, and fast as C-extensions.

%description -l pl.UTF-8
Sorted Containers to wydana na licencji Apache2 biblioteka sortowanych
kolekcji, napisana w czystym Pythonie, szybka jak rozszerzenia w C.

%package -n python3-sortedcontainers
Summary:	Sorted Containers - Sorted List, Sorted Dict, Sorted Set
Summary(pl.UTF-8):	Posortowane kontenery - lista, słownik, zbiór
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-sortedcontainers
Sorted Containers is an Apache2 licensed sorted collections library,
written in pure-Python, and fast as C-extensions.

%description -n python3-sortedcontainers -l pl.UTF-8
Sorted Containers to wydana na licencji Apache2 biblioteka sortowanych
kolekcji, napisana w czystym Pythonie, szybka jak rozszerzenia w C.

%prep
%setup -q -n sortedcontainers-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
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
%doc LICENSE README.rst
%{py_sitescriptdir}/sortedcontainers
%{py_sitescriptdir}/sortedcontainers-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sortedcontainers
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/sortedcontainers
%{py3_sitescriptdir}/sortedcontainers-%{version}-py*.egg-info
%endif
