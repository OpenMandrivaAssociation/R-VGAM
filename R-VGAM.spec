%global packname  VGAM
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.8_4
Release:          1
Summary:          Vector Generalized Linear and Additive Models
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-4.tar.gz
Requires:         R-splines R-methods R-stats R-stats4
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-splines R-methods R-stats R-stats4

%description
Vector generalized linear and additive models, and associated models
(Reduced-Rank VGLMs, Quadratic RR-VGLMs, Reduced-Rank VGAMs). This package
fits many models and distribution by maximum likelihood estimation (MLE)
or penalized MLE. Also fits constrained ordination models in ecology.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
