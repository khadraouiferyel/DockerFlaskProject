FROM node:18-alpine as build

RUN mkdir -p /app

WORKDIR /app

COPY package.json /app/

RUN npm install

COPY . /app/

RUN npm run build --prod

# Server

FROM nginx:alpine
COPY --from=build /app/dist/frontend /usr/share/nginx/html