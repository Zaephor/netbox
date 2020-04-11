#FROM python:alpine3.11
FROM lsiobase/alpine:3.11
ARG RELEASE=v2.7.12
EXPOSE 8000
VOLUME /config
COPY s6/ /
RUN \
    /setup/netbox-install.sh
