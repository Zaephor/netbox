#!/bin/bash

apk add --no-cache \
	git \
	python3 python3-dev \
	jpeg-dev libevent-dev libffi-dev libxslt-dev \
	postgresql-dev \
	openldap-dev openssl-dev

apk add --no-cache --virtual .build-dependencies build-base g++ make

git clone --single-branch --branch ${RELEASE} --depth 1 https://github.com/netbox-community/netbox.git /app

for x in 'napalm' 'django-storages' 'django-auth-ldap'; do
	echo "${x}" >> /app/local_requirements.txt
done

cd /app
pip3 install --upgrade pip
pip3 install wheel
pip3 install -r requirements.txt
if [[ -e local_requirements.txt ]]; then
	pip3 install -r local_requirements.txt
fi

apk del .build-dependencies

echo "${RELEASE}" > /app/.version

