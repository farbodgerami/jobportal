FROM nginx:stable

 

COPY default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

 
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]