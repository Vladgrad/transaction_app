FROM node:20-alpine

WORKDIR /vite

COPY package.json package-lock.json ./
RUN npm install

COPY . .

EXPOSE 5173

# Запуск Vite с доступом снаружи
CMD ["npm", "run", "dev", "--", "--host"]
