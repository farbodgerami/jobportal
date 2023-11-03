FROM nginx:stable

 

COPY default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf


COPY fullchain.pem /etc/nginx/fullchain.pem
COPY privkey.pem /etc/nginx/privkey.pem
COPY options-ssl-nginx.conf /etc/nginx/options-ssl-nginx.conf
COPY ssl-dhparams.pem /etc/nginx/ssl-dhparams.pem
EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]