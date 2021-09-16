%global debug_package %{nil}

Name: python-chardet
Epoch: 100
Version: 3.0.4
Release: 1%{?dist}
BuildArch: noarch
Summary: Character encoding auto-detection in Python
License: LGPL-2.1-only
URL: https://github.com/chardet/chardet/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Character encoding auto-detection in Python. As smart as your browser.
Open source.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
%if 0%{?centos_version} == 700
mv %{buildroot}%{_bindir}/chardetect %{buildroot}%{_bindir}/chardetect3
%endif
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500 || 0%{?centos_version} == 700
%package -n python%{python3_version_nodots}-chardet
Summary: Character encoding auto-detection in Python
Requires: python3
Provides: python3-chardet = %{epoch}:%{version}-%{release}
Provides: python3dist(chardet) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-chardet = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(chardet) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-chardet = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(chardet) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-chardet
Character encoding auto-detection in Python. As smart as your browser.
Open source.

%files -n python%{python3_version_nodots}-chardet
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?centos_version} == 700)
%package -n python3-chardet
Summary: Character encoding auto-detection in Python
Requires: python3
Provides: python3-chardet = %{epoch}:%{version}-%{release}
Provides: python3dist(chardet) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-chardet = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(chardet) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-chardet = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(chardet) = %{epoch}:%{version}-%{release}

%description -n python3-chardet
Character encoding auto-detection in Python. As smart as your browser.
Open source.

%files -n python3-chardet
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
