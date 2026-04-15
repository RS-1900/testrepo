
FROM node:18-alpine AS builder

# directorio
WORKDIR /app

#  archivos de dependencias
COPY package*.json ./

#  intala dependencias
RUN npm install

COPY . .


FROM nginx:stable-alpine


COPY --from=builder /app /usr/share/nginx/html

EXPOSE 80

#comando para que Nginx se mantenga corriendo
CMD ["nginx", "-g", "daemon off;"]