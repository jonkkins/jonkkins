FROM nginx:1.17.8-alpine

# Copy config
COPY nginx/conf.d /etc/nginx/conf.d

# Copy pages
COPY error /home/error
COPY pages /home/pages