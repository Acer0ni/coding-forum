FROM node:14-stretch

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm i
COPY src /app/src
COPY public /app/public

EXPOSE 3000
CMD npm start