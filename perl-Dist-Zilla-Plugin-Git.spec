%define upstream_name    Dist-Zilla-Plugin-Git
%define upstream_version 1.110500

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Commit dist.ini and changelog
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Dist::Zilla::Role::AfterRelease)
BuildRequires:	perl(Dist::Zilla::Role::BeforeRelease)
BuildRequires:	perl(Dist::Zilla::Role::PluginBundle)
BuildRequires:	perl(English)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Git::Wrapper)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(MooseX::Has::Sugar)
BuildRequires:	perl(MooseX::Types::Moose)
BuildRequires:	perl(String::Formatter)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More) >= 0.940.0
BuildRequires:	perl(Module::Build)

BuildArch:	noarch

%description
This set of plugins for the Dist::Zilla manpage can do interesting
things for module authors using git to track their work. The following
plugins are provided in this distribution:
 * Dist::Zilla::Plugin::Git::Check
 * Dist::Zilla::Plugin::Git::Commit
 * Dist::Zilla::Plugin::Git::Tag
 * Dist::Zilla::Plugin::Git::Push

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

