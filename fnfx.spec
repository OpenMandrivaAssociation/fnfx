%define name	fnfx
%define ver 	0.3
%define rel	%mkrel 1

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

