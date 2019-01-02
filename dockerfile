FROM node

MAINTAINER 李俊君 21851172@zju.edu.cn

RUN npm config set unsafe-perm true
RUN npm install -g cnpm --registry=https://registry.npm.taobao.org
RUN cnpm install -g http-server

RUN mkdir -p /usr/src/node
WORKDIR /usr/src/node
COPY . /usr/src/node

RUN cnpm install

EXPOSE 80

CMD ["http-server","./","-p","80"]