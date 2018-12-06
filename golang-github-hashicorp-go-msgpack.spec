# http://github.com/hashicorp/go-msgpack

%global goipath         github.com/hashicorp/go-msgpack
%global commit          fa3f63826f7c23912c15263591e65d54d080b458


%gometa -i

Name:           golang-github-hashicorp-go-msgpack
Version:        0
Release:        0.13%{?dist}
Summary:        Collection of Open-Source Go libraries and tools
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
# Missing deps: gopkg.in/vmihailenco/msgpack.v2
%gochecks -d codec

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md msgpack.org.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.gitfa3f638
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.20150819gitfa3f638
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitfa3f638
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitfa3f638
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitfa3f638
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitfa3f638
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.gitfa3f638
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.gitfa3f638
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.gitfa3f638
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.3.gitfa3f638
- Bump to upstream fa3f63826f7c23912c15263591e65d54d080b458
  related: #1250465

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git71c2886
- Update to spec-2.1
  related: #1250465

* Wed Aug 05 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.git71c2886
- Update spec file to spec-2.0
  resolves: #1250465

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git71c2886
- First package for Fedora
  resolves: #1212031

