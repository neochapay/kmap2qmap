Name:       kmap2qmap
Version:    5.12.9
Summary:    The kmap2qmap tool
Release:    0
License:    GPLv3
Group:      Qt/Qt
Source:     %{name}-%{version}.tar.bz2
Requires:   %{name} = %{version}-%{release}
Provides:   qt5-qttools-%{name}

BuildRequires:  qt5-qtdbus-devel
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qmake

%description
This package contains the kmap2qmap tool

%prep
%setup -q -n %{name}-%{version}

%build
export QTDIR=/usr/share/qt5
touch .git
%qmake5
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_qt5_bindir}
cp kmap2qmap %{buildroot}%{_qt5_bindir}/

%files
%defattr(-,root,root,-)
%{_qt5_bindir}/kmap2qmap
