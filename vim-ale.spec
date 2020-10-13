%global         upstream_name   ale
%global         vimfiles        %{_datadir}/vim/vimfiles

Name:           vim-%{upstream_name}
Version:        3.0.0
Release:        1%{?dist}
Summary:        Asynchronous Vim Lint Engine
License:        BSD

URL:            https://github.com/dense-analysis/ale
Source0:        https://github.com/dense-analysis/%upstream_name/archive/v%version/%upstream_name-%version.tar.gz

BuildArch:      noarch

Requires:       vim


%description
ALE (Asynchronous Lint Engine) is a plugin providing linting (syntax checking
and semantic errors) in NeoVim 0.2.0+ and Vim 8 while you edit your text files,
and acts as a Vim Language Server Protocol client.

ALE makes use of NeoVim and Vim 8 job control functions and timers to run
linters on the contents of text buffers and return errors as text is changed in
Vim. This allows for displaying warnings and errors in files being edited in Vim
before files have been saved back to a filesystem.

In other words, this plugin allows you to lint while you type.


%prep
%autosetup -p1 -n %upstream_name-%version


%install
mkdir -p %buildroot%vimfiles
cp -r ale_linters %buildroot%vimfiles
cp -r autoload %buildroot%vimfiles
cp -r doc %buildroot%vimfiles
cp -r ftplugin %buildroot%vimfiles
cp -r plugin %buildroot%vimfiles
cp -r rplugin %buildroot%vimfiles
cp -r syntax %buildroot%vimfiles


%files
%license LICENSE
%doc %vimfiles/doc/*
%vimfiles/ale_linters
%vimfiles/autoload/*
%vimfiles/rplugin
%vimfiles/plugin/*
%vimfiles/ftplugin/*
%vimfiles/syntax/*


%changelog
* Sun Oct 11 2020 Pavel Raiskup <praiskup@redhat.com> - 3.0.0-1
- preparations for a copr build

* Tue Apr 21 2020 Pavel Raiskup <praiskup@redhat.com> - 2.6.0-1
- initial packaging
