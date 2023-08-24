FROM ubuntu:18.04
LABEL maintainer="Ignacio Vizzo <ivizzo@uni-bonn.de>"

# Install bare minimum utils
RUN apt-get update && apt-get install -y \
  curl \
  git \
  && rm -rf /var/lib/apt/lists/*

# Get nodejs V10.0
RUN curl -fsSL https://deb.nodesource.com/setup_10.x | bash -

# Install NodeJS and npm package manager
RUN apt-get update && apt-get install -y \
  nodejs \
  && rm -rf /var/lib/apt/lists/*

RUN npm install -g \
  doctoc \
  github-wiki-sidebar \
  markdown-link-check@3.8.5 \
  prettier
