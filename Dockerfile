FROM elyase/staticpython
ADD www /var/www
EXPOSE 8080
CMD nohup python /var/www/cpu_mem_gen.py > cpu_mem_gen.log 2>&1
