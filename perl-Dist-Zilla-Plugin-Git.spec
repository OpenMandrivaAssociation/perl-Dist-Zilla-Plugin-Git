%define upstream_name    Dist-Zilla-Plugin-Git
%define upstream_version 1.093250

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Commit dist.ini and changelog
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Cwd)
BuildRequires: perl(Dist::Zilla::Role::AfterRelease)
BuildRequires: perl(Dist::Zilla::Role::BeforeRelease)
BuildRequires: perl(Dist::Zilla::Role::PluginBundle)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Git::Wrapper)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Autobox)
BuildRequires: perl(MooseX::Has::Sugar)
BuildRequires: perl(MooseX::Types::Moose)
BuildRequires: perl(Symbol)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This set of plugins for the Dist::Zilla manpage can do interesting things
for module authors using http://git- scm.com to track their work. The
following plugins are provided in this distribution:

* * the Dist::Zilla::Plugin::Git::Check manpage

* * the Dist::Zilla::Plugin::Git::Commit manpage

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


