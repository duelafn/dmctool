# Author: Dean Serenevy  <dean@serenevy.net>
# This software is Copyright (c) 2017 Dean Serenevy.
# This software is Copyright (c) 2013 APCI, LLC.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

PKGNAME = dmctool
PKG_VERSION = $(shell perl -ne 'print $$1 if /^__version__\s*=\s*"([\d.]+(?:[\-\+~.]\w+)*)"/' dmctool/__init__.py)


.PHONY: all sdist dist debbuild clean build test

all: test build

zip: test
	python setup.py sdist --format=zip

sdist: test
	python setup.py sdist

dist: test debbuild
	mv -f debbuild/${PKGNAME}_* debbuild/*.deb dist/
	rm -rf debbuild

debbuild: test sdist
	rm -rf debbuild
	mkdir -p debbuild
	grep "(${PKG_VERSION}-1)" debian/changelog || (echo "** debian/changelog requires update **" && false)
	mv -f dist/${PKGNAME}-${PKG_VERSION}.tar.gz debbuild/${PKGNAME}_${PKG_VERSION}.orig.tar.gz
	cd debbuild && tar -xzf ${PKGNAME}_${PKG_VERSION}.orig.tar.gz
	cp -r debian debbuild/${PKGNAME}-${PKG_VERSION}/
	cd debbuild/${PKGNAME}-${PKG_VERSION} && dpkg-buildpackage -rfakeroot -uc -us -tc -i

build:
	python setup.py build_ext --inplace

test: build
	python2 setup.py test >/dev/null
	python3 setup.py test >/dev/null

clean:
	pyclean .
	rm -rf build debbuild dmctool.egg-info
	rm -f MANIFEST
