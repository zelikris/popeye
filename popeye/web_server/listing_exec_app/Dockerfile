FROM ubuntu:latest

# Update the stuff
RUN \
    sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y build-essential && \
    apt-get install -y software-properties-common && \
    apt-get install -y byobu curl git htop man unzip vim wget && \
    add-apt-repository ppa:mc3man/trusty-media && \
    apt-get update && \
    apt-get install -y ffmpeg gstreamer0.10-ffmpeg && \
    apt-get install -y imagemagick && \
    rm -rf /var/lib/apt/lists/*

# Install git and anaconda
RUN apt-get -y install wget
RUN wget https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda-2.3.0-Linux-x86_64.sh
RUN bash /Anaconda-2.3.0-Linux-x86_64.sh -b -p /usr/lib/anaconda
RUN mkdir /png
RUN mkdir /gif
ADD lib /listing_exec_app/lib
ADD objects /listing_exec_app/objects

ENV PATH /usr/lib/anaconda/bin:$PATH

ENV HOME /listing_exec_app

WORKDIR /listing_exec_app

RUN mkdir /listing_exec_app/input_images
RUN mv /listing_exec_app/lib/default_code/ch_13/input_images/* /listing_exec_app/input_images

CMD ["bash"]

EXPOSE 22
