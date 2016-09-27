FROM elyase/staticpython
ADD www /var/www
EXPOSE 8080
CMD python /var/www/cpu_mem_gen.py
