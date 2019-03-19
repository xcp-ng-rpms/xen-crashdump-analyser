Name: xen-crashdump-analyser
Summary: Xen crashdump analyser
Version: 2.5.2
Release: 1
License: GPL
Group: Applications/System
Source: https://code.citrite.net/rest/archive/latest/projects/XS/repos/%{name}/archive?at=v%{version}&format=tar.gz&prefix=%{name}-%{version}#/%{name}.tar.gz
BuildRequires: gcc-c++

%description
                      * Xen Crashdump Analyser *
                   --------------------------------
                   a tool for analysing Xen crashes
                   --------------------------------

See http://xenbits.xen.org/people/andrewcoop/ for detailed usage
instructions, examples and more.

%prep
%autosetup -p1

%build
%{?cov_wrap} %{__make}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m755 %{name} %{buildroot}%{_libdir}/xen/bin/%{name}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/xen/bin/%{name}

%changelog
* Tue Nov 07 2017 Simon Rowe <simon.rowe@citrix.com> - 2.5.2-1
- CA-263292: Make error a warning instead
- CA-263292: Copy vCPU state earlier

* Wed May 08 2013 Andrew Cooper <andrew.cooper3@citrix.com>
Version 2.4.1
- Find VCPU state on IST stacks when appropriate

* Fri Apr 12 2013 Andrew Cooper <andrew.cooper3@citrix.com>
Version 2.4.0
- Various bug fixes
- Add debugging info for console rings
- Allow detection of a Xen debug build
- Doxygen updates
- Move classes into namespaces

* Mon Oct 08 2012 Andrew Cooper <andrew.cooper3@citrix.com>
Version 2.3.0
- Improve error messages and logging support
- Try to leave a meaningful log when the filesystem is out of space
- Print PCPU numbers in decimal rather than hex
- Various bug fixes and cleanups

* Wed Aug 22 2012 Andrew Cooper <andrew.cooper3@citrix.com>
Version 2.2.0
- Add checks for domain paging support
- Collect CPU information for decoding vendor-specific data
- Add option to dump Xen domain and vcpu structures
- Various bug fixes and cleanups

* Tue Jun 12 2012 Andrew Cooper <andrew.cooper3@citrix.com>
Version 2.1.0
- Print domain handles from Xen (includes VM UUID)

* Thu Jun 07 2012 Andrew Cooper <andrew.cooper3@citrix.com>
Version 2.0.0
- Change to GPLv2
- Significant refactoring

* Tue Mar 27 2012 Andrew Cooper <andrew.cooper3@citrix.com>
Version 1.1.0
- Numerous minor fixes

* Thu Jan 19 2012 Andrew Cooper <andrew.cooper3@citrix.com>
Version 1.0.0
- Initial version.
