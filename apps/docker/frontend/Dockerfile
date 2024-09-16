FROM node:alpine

WORKDIR /apps/frontend/my-app

COPY ./apps/frontend/my-app .

RUN npm install

CMD [ "npm", "run", "deploy" ]