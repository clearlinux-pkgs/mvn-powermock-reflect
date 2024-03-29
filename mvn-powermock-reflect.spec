#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-powermock-reflect
Version  : 1.7.4
Release  : 1
URL      : https://repo1.maven.org/maven2/org/powermock/powermock-reflect/1.7.4/powermock-reflect-1.7.4.jar
Source0  : https://repo1.maven.org/maven2/org/powermock/powermock-reflect/1.7.4/powermock-reflect-1.7.4.jar
Source1  : https://repo1.maven.org/maven2/org/powermock/powermock-reflect/1.7.4/powermock-reflect-1.7.4.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-powermock-reflect-data = %{version}-%{release}
Requires: mvn-powermock-reflect-license = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-powermock-reflect package.
Group: Data

%description data
data components for the mvn-powermock-reflect package.


%package license
Summary: license components for the mvn-powermock-reflect package.
Group: Default

%description license
license components for the mvn-powermock-reflect package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-powermock-reflect
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-powermock-reflect/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/powermock/powermock-reflect/1.7.4
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/powermock/powermock-reflect/1.7.4/powermock-reflect-1.7.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/powermock/powermock-reflect/1.7.4
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/powermock/powermock-reflect/1.7.4/powermock-reflect-1.7.4.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/powermock/powermock-reflect/1.7.4/powermock-reflect-1.7.4.jar
/usr/share/java/.m2/repository/org/powermock/powermock-reflect/1.7.4/powermock-reflect-1.7.4.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-powermock-reflect/LICENSE.txt
