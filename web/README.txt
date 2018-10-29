http://47.98.143.170/algorithm2/6137-3972-6021-4360-4745-3208-5528-4009-6771-4716-7974-5932/

params : 'algorithm1' or 'algorithm2'
	 6137-3972-6021-4360-4745-3208-5528-4009-6771-4716-7974-5932
	


return:
	   Json({'input': param, 
		 'statue':int,
		 'statue_battery':int,
		 'statue_meachine':int,
		 })


Not consider net communication time
lr  run time :0.25 ms
svm run time :0.05 ms







#Docker

Install https://docs.docker.com/install/linux/docker-ce/ubuntu/

Docker with Django https://docs.docker.com/compose/django/
Docker with Flask in github https://github.com/docker/labs/blob/master/beginner/chapters/webapps.md













Deploy Django web server with uWSGI and nginx
https://uwsgi.readthedocs.io/en/latest/tutorials/Django_and_nginx.html





$ pip install uwsgi


change dir to the base
$ uwsgi --http :8000 --module my_api.wsgi




start nginx: 
$ sudo /etc/init.d/nginx restart

start uwsgi
$ uwsgi --socket :8001 --module my_api.wsgi