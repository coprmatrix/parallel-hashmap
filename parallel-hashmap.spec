Name: parallel-hashmap
Version: 1.3.12
Release: 1
Summary: Header-only hashmap and btree containers
URL: https://greg7mdp.github.io/parallel-hashmap
License: Apache-2.0
BuildArch: noarch
BuildRequires: cmake make gcc-c++
Source: https://github.com/greg7mdp/parallel-hashmap/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%package devel
Summary: %{summary}.

%description devel
%{summary}.

%description
%{summary}.


%prep
%autosetup

%build
export CMAKE_CXX_COMPILER=%{_bindir}/true
%cmake -DPHMAP_BUILD_TESTS=OFF -DPHMAP_BUILD_EXAMPLES=OFF
%cmake_build

%install
%cmake_install

%files devel
%_includedir/parallel_hashmap



