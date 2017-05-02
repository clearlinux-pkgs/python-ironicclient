#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEB6CCA1483FA74EC (infra-root@openstack.org)
#
Name     : python-ironicclient
Version  : 1.12.0
Release  : 36
URL      : http://tarballs.openstack.org/python-ironicclient/python-ironicclient-1.12.0.tar.gz
Source0  : http://tarballs.openstack.org/python-ironicclient/python-ironicclient-1.12.0.tar.gz
Source99 : http://tarballs.openstack.org/python-ironicclient/python-ironicclient-1.12.0.tar.gz.asc
Summary  : OpenStack Bare Metal Provisioning API Client Library
Group    : Development/Tools
License  : Apache-2.0
Requires: python-ironicclient-bin
Requires: python-ironicclient-python
Requires: PyYAML
Requires: appdirs
Requires: dogpile.cache
Requires: jsonschema
Requires: keystoneauth1
Requires: osc-lib
Requires: oslo.i18n
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: python-openstackclient
Requires: requests
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/badges/python-ironicclient.svg
:target: http://governance.openstack.org/reference/tags/index.html

%package bin
Summary: bin components for the python-ironicclient package.
Group: Binaries

%description bin
bin components for the python-ironicclient package.


%package python
Summary: python components for the python-ironicclient package.
Group: Default

%description python
python components for the python-ironicclient package.


%prep
%setup -q -n python-ironicclient-1.12.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1490890830
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1490890830
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ironic

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
