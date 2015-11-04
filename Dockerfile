FROM ubuntu:wily

RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
  python python-pip python-dogtail

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
  --no-install-recommends xvfb mate-desktop-environment-core

RUN pip install behave

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD run-tests.sh /bin/run-tests

VOLUME /src
WORKDIR /src
CMD /bin/run-tests