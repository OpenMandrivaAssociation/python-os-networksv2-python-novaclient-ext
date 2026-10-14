Name:		python-os-networksv2-python-novaclient-ext
Version:	0.26
Release:	4
Source0:	https://files.pythonhosted.org/packages/source/o/os-networksv2-python-novaclient-ext/os_networksv2_python_novaclient_ext-%{version}.tar.gz
Summary:	Adds rackspace networks support to python-novaclient
URL:		https://pypi.org/project/os-networksv2-python-novaclient-ext/
License:	Apache License, Version 2.0
Group:		Development/Python
BuildRequires:	pkgconfig(python3)
BuildSystem:	python
BuildArch:	noarch

%description
Adds rackspace networks support to python-novaclient

%files
%{py_sitedir}/os_networksv2_python_novaclient_ext.py
%{py_sitedir}/os_networksv2_python_novaclient_ext-*.*-info
