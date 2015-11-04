#!/bin/bash

set -xe

source ~/.gimme/envs/go1.5.env

export GOPATH="/go"
GTK_VERSION=$(pkg-config --modversion gtk+-3.0 | tr . _ | cut -d '_' -f 1-2)
go get -u -tags "nocli gtk_${GTK_VERSION}" github.com/twstrike/coyim

cp $GOPATH/bin/coyim /src/coyim-bin

