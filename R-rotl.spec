#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rotl
Version  : 3.0.7
Release  : 11
URL      : https://cran.r-project.org/src/contrib/rotl_3.0.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rotl_3.0.7.tar.gz
Summary  : Interface to the 'Open Tree of Life' API
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : R-ape
BuildRequires : R-assertthat
BuildRequires : R-httr
BuildRequires : R-progress
BuildRequires : R-rentrez
BuildRequires : R-rncl
BuildRequires : buildreq-R

%description
---
output: github_document
---
[![Build Status](https://travis-ci.org/ropensci/rotl.svg?branch=master)](https://travis-ci.org/ropensci/rotl)
[![Build status](https://ci.appveyor.com/api/projects/status/qr4k9a8wlrjl65rp?svg=true)](https://ci.appveyor.com/project/ropensci/rotl)
[![codecov.io](https://codecov.io/github/ropensci/rotl/coverage.svg?branch=master)](https://codecov.io/github/ropensci/rotl?branch=master)
[![](http://www.r-pkg.org/badges/version/rotl)](http://www.r-pkg.org/pkg/rotl)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/rotl)](http://www.r-pkg.org/pkg/rotl)
[![Research software impact](http://depsy.org/api/package/cran/rotl/badge.svg)](http://depsy.org/package/r/rotl)
[![](https://badges.ropensci.org/17_status.svg)](https://github.com/ropensci/onboarding/issues/17)
[![Project Status: Active â The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

%prep
%setup -q -c -n rotl

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552863148

%install
export SOURCE_DATE_EPOCH=1552863148
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rotl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rotl
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rotl
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  rotl || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rotl/CITATION
/usr/lib64/R/library/rotl/DESCRIPTION
/usr/lib64/R/library/rotl/INDEX
/usr/lib64/R/library/rotl/LICENSE
/usr/lib64/R/library/rotl/Meta/Rd.rds
/usr/lib64/R/library/rotl/Meta/features.rds
/usr/lib64/R/library/rotl/Meta/hsearch.rds
/usr/lib64/R/library/rotl/Meta/links.rds
/usr/lib64/R/library/rotl/Meta/nsInfo.rds
/usr/lib64/R/library/rotl/Meta/package.rds
/usr/lib64/R/library/rotl/Meta/vignette.rds
/usr/lib64/R/library/rotl/NAMESPACE
/usr/lib64/R/library/rotl/NEWS.md
/usr/lib64/R/library/rotl/R/rotl
/usr/lib64/R/library/rotl/R/rotl.rdb
/usr/lib64/R/library/rotl/R/rotl.rdx
/usr/lib64/R/library/rotl/doc/data_mashups.R
/usr/lib64/R/library/rotl/doc/data_mashups.Rmd
/usr/lib64/R/library/rotl/doc/data_mashups.html
/usr/lib64/R/library/rotl/doc/how-to-use-rotl.R
/usr/lib64/R/library/rotl/doc/how-to-use-rotl.Rmd
/usr/lib64/R/library/rotl/doc/how-to-use-rotl.html
/usr/lib64/R/library/rotl/doc/index.html
/usr/lib64/R/library/rotl/doc/meta-analysis.R
/usr/lib64/R/library/rotl/doc/meta-analysis.Rmd
/usr/lib64/R/library/rotl/doc/meta-analysis.html
/usr/lib64/R/library/rotl/extdata/egg.csv
/usr/lib64/R/library/rotl/extdata/mcmcglmm_model.rds
/usr/lib64/R/library/rotl/extdata/protist_mutation_rates.csv
/usr/lib64/R/library/rotl/help/AnIndex
/usr/lib64/R/library/rotl/help/aliases.rds
/usr/lib64/R/library/rotl/help/paths.rds
/usr/lib64/R/library/rotl/help/rotl.rdb
/usr/lib64/R/library/rotl/help/rotl.rdx
/usr/lib64/R/library/rotl/html/00Index.html
/usr/lib64/R/library/rotl/html/R.css
/usr/lib64/R/library/rotl/tests/test-all.R
/usr/lib64/R/library/rotl/tests/testthat/test-API.R
/usr/lib64/R/library/rotl/tests/testthat/test-api-studies.R
/usr/lib64/R/library/rotl/tests/testthat/test-api-taxonomy.R
/usr/lib64/R/library/rotl/tests/testthat/test-api-tnrs.R
/usr/lib64/R/library/rotl/tests/testthat/test-api-tol.R
/usr/lib64/R/library/rotl/tests/testthat/test-base.R
/usr/lib64/R/library/rotl/tests/testthat/test-deduplicate_labels.R
/usr/lib64/R/library/rotl/tests/testthat/test-external.R
/usr/lib64/R/library/rotl/tests/testthat/test-match_names.R
/usr/lib64/R/library/rotl/tests/testthat/test-studies.R
/usr/lib64/R/library/rotl/tests/testthat/test-taxonomy.R
/usr/lib64/R/library/rotl/tests/testthat/test-tnrs.R
/usr/lib64/R/library/rotl/tests/testthat/test-tol.R
/usr/lib64/R/library/rotl/tests/testthat/test-tree_to_labels.R
/usr/lib64/R/library/rotl/tests/tree_of_life.json
