# Copyright 2026 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
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

%global source_date_epoch_from_changelog 0

Name: python-python-discovery
Epoch: 100
Version: 1.3.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Python interpreter discovery
License: MIT
URL: https://github.com/tox-dev/python-discovery/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip

%description
Python interpreter discovery.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
pip wheel \
    --no-deps \
    --no-build-isolation \
    --wheel-dir=dist \
    .

%install
pip install \
    --no-deps \
    --ignore-installed \
    --root=%{buildroot} \
    --prefix=%{_prefix} \
    dist/*.whl
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} >= 1600
%package -n python%{python3_version_nodots}-python-discovery
Summary: Python interpreter discovery
Requires: python3
Requires: python3-filelock >= 3.15.4
Requires: python3-platformdirs >= 4.3.6
Provides: python3-python-discovery = %{epoch}:%{version}-%{release}
Provides: python3dist(python-discovery) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-python-discovery = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(python-discovery) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-python-discovery = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(python-discovery) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-python-discovery
Python interpreter discovery.

%files -n python%{python3_version_nodots}-python-discovery
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} >= 1600)
%package -n python3-python-discovery
Summary: Python interpreter discovery
Requires: python3
Requires: python3-filelock >= 3.15.4
Requires: python3-platformdirs >= 4.3.6
Provides: python3-python-discovery = %{epoch}:%{version}-%{release}
Provides: python3dist(python-discovery) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-python-discovery = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(python-discovery) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-python-discovery = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(python-discovery) = %{epoch}:%{version}-%{release}

%description -n python3-python-discovery
Python interpreter discovery.

%files -n python3-python-discovery
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
