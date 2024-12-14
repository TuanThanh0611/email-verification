# Sử dụng Node.js 18.x để build ứng dụng
FROM node:18 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build --prod

# Sử dụng NGINX để phục vụ ứng dụng
FROM nginx:1.21
COPY --from=build /app/dist/frontend /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
