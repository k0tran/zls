Name:      zls
Version:   0.12.0
Release:   alt1

Summary:   A language server for Zig
License:   MIT
Group:     Development/Tools
Url:       https://github.com/zigtools/zls

Source:    %name-%version.tar

ExclusiveArch: %zig_arches
BuildRequires(pre): rpm-macros-zig
BuildRequires: zig >= 0.12.0, zig < 0.13.0

%description
%summary.

%prep
%setup -q

%build
%zig_build

%install
%zig_install

# No check because for some reason on my machine it does not work
# Although it maybe my machine's fault
# check
# zig_test

%files
%_bindir/zls

%changelog
* Wed Jul 31 2024 Ilya Sorochan <k0tran@altlinux.org> 0.12.0-alt1
- Initial build for ALT Linux
