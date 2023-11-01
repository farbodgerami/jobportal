FROM nginx:stable

RUN rm /etc/nginx/conf.d/default.conf

ADD ./nginx.conf /etc/nginx/conf.d/nginx.conf


# COPY fullchain.pem /etc/nginx/fullchain.pem
# COPY privkey.pem /etc/nginx/privkey.pem
# COPY options-ssl-nginx.conf /etc/nginx/options-ssl-nginx.conf
# COPY ssl-dhparams.pem /etc/nginx/ssl-dhparams.pem
CMD ["nginx", "-g", "daemon off;"]