FROM ubuntu:wily

RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"

# Python env for dogtail
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
  python python-pip python-dogtail

# Minimum Gnome environment
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
  --no-install-recommends xvfb mate-desktop-environment-core

# Env for building coy
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
  --no-install-recommends libgtk-3-dev curl git

RUN pip install behave

# Required for TCNode in dogtail
# build-dep python-imaging
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
    python-dev \
    libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev &&\
    pip install Pillow

# Install go 1.5
RUN curl -sL https://raw.githubusercontent.com/travis-ci/gimme/master/gimme | GIMME_GO_VERSION=1.5 bash

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD build-coy.sh /bin/build-coy
ADD dogtail-wrapper.sh /bin/dogtail-wrapper

VOLUME /src
VOLUME /tmp/dogtail-root

WORKDIR /src

ENTRYPOINT ["/bin/dogtail-wrapper"]
CMD ["behave"]