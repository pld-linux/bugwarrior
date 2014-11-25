#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

Summary:	Sync github, bitbucket, and trac issues with taskwarrior
Name:		bugwarrior
Version:	1.0.2
Release:	0.1
License:	GPL v3+
Group:		Applications/Databases
Source0:	http://pypi.python.org/packages/source/b/bugwarrior/%{name}-%{version}.tar.gz
# Source0-md5:	09c93f86a27ffc092e69b46889a3bf50
URL:		http://pypi.python.org/pypi/bugwarrior
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with tests}
BuildRequires:	python-bitlyapi
BuildRequires:	python-bugzilla
BuildRequires:	python-click
BuildRequires:	python-dateutil
BuildRequires:	python-devel
BuildRequires:	python-dogpile-cache
BuildRequires:	python-jinja2
BuildRequires:	python-keyring
BuildRequires:	python-lockfile
BuildRequires:	python-offtrac
BuildRequires:	python-pycurl
BuildRequires:	python-pytz
BuildRequires:	python-requests
BuildRequires:	python-setuptools
BuildRequires:	python-six
BuildRequires:	python-taskw
BuildRequires:	python-twiggy
%endif
Requires:	python-bitlyapi
Requires:	python-bugzilla
Requires:	python-click
Requires:	python-dateutil
Requires:	python-dogpile-cache
Requires:	python-jinja2
Requires:	python-keyring
Requires:	python-lockfile
Requires:	python-offtrac
Requires:	python-pycurl
Requires:	python-pytz
Requires:	python-requests
Requires:	python-setuptools
Requires:	python-six
Requires:	python-taskw
Requires:	python-twiggy
BuildArch:	noarch
# See https://bugzilla.redhat.com/show_bug.cgi?id=1036078
#BuildRequires:      python-jira
#Requires:           python-jira
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bugwarrior is a command line utility for updating your local
taskwarrior database from your forge issue trackers.

It currently supports pulling issues from github, bitbucket, trac,
bugzilla, megaplan, teamlab, redmine, and activecollab

%prep
%setup -q

# Remove bundled egg-info in case it exists
rm -r %{name}.egg-info

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/README.rst
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{name}/docs

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc bugwarrior/README.rst LICENSE.txt bugwarrior/docs
%attr(755,root,root) %{_bindir}/bugwarrior-pull
%attr(755,root,root) %{_bindir}/bugwarrior-vault
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/bugwarrior-%{version}-py*.egg-info
