FROM node:alpine AS base

RUN npm i -g pnpm



FROM base AS dependencies

WORKDIR /usr/src/app

COPY package.json pnpm-lock.yaml ./

RUN pnpm install



FROM base AS build

WORKDIR /usr/src/app

COPY . .
COPY package.json pnpm-lock.yaml ./
COPY --from=dependencies /usr/src/app/node_modules ./node_modules

RUN pnpm run build



FROM build AS production

ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

WORKDIR /usr/src/app

COPY --from=build /usr/src/app/dist ./dist
COPY --from=build /usr/src/app/node_modules ./node_modules

CMD ["node", "dist/apps/http-gateway/main"]