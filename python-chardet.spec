# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-chardet
Epoch: 100
Version: 4.0.0
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
mv %{buildroot}%{_bindir}/chardetect %{buildroot}%{_bindir}/chardetect-4
%endif
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

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
