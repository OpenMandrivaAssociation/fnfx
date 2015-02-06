Name:		fnfx
Version:	0.3
Release:	8
Summary:	Toshiba laptop function key utility
License:	GPL
URL:		http://fnfx.sf.net
Group:		System/Configuration/Hardware
Source0:	downloads.sourceforge.net/project/fnfx/fnfx/fnfx%20v0.3/fnfx-0.3.tar.bz2
Source1:	%{name}.service
Source2:	fnfxd_check.sh
Requires(pre):	rpm-helper
Requires(post):	rpm-helper
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

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
%makeinstall_std

install -D -m0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m0755 %{SOURCE2} %{buildroot}%{_sbindir}/fnfxd_check

%clean

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_bindir}/%{name}
%{_sbindir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_unitdir}/%{name}.service

%doc ChangeLog INSTALL AUTHORS README
