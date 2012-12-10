%define name	fnfx
%define ver 	0.3
%define rel	%mkrel 6

Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Summary:	Toshiba laptop function key utility
License:	GPL
URL:		http://fnfx.sf.net
Group:		System/Configuration/Hardware
Source:		%{name}-%{version}.tar.bz2
Source1:	%{name}.init
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires(pre):	rpm-helper
Requires(post):	rpm-helper

%description
FnFX enables owners of Toshiba laptops to change the LCD brightness,
control, the internal fan and use the special keys on their keyboard
(Fn-x combinations, hot-keys). The internal functions will give the
possibility to map the Fn-Keys to functions like volume up/down, mute,
suspend to disk, suspend to ram and switch LCD/CRT/TV-out. These
functions heavily depend on the system and/or kernel configuration.
You will need at least a kernel (v2.4.x, v2.5.x, v2.6.x) with ACPI and
Toshiba support (CONFIG_ACPI and CONFIG_ACPI_TOSHIBA).

%prep
%setup -q

%build
%configure
%make

%install
rm -Rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}/%{_initrddir}
install %{SOURCE1} %{buildroot}/%{_initrddir}/%{name}

%clean
rm -Rf %{buildroot}

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_sbindir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%config(noreplace) %{_initrddir}/%{name}

%doc ChangeLog INSTALL AUTHORS README



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-6mdv2011.0
+ Revision: 618310
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.3-5mdv2010.0
+ Revision: 428824
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.3-4mdv2009.0
+ Revision: 245245
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.3-2mdv2008.1
+ Revision: 140730
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 0.3-2mdv2008.0
+ Revision: 70235
- use %%mkrel


* Thu Nov 25 2004 Buchan Milne <bgmilne@linux-mandrake.com> 0.3-1mdk
- 0.3

* Mon Mar 01 2004 Buchan Milne <bgmilne@linux-mandrake.com> 0.2-2mdk
- fix typo in init script

* Tue Jan 13 2004 Buchan Milne <bgmilne@linux-mandrake.com> 0.2-1mdk
- First Mandrake package

